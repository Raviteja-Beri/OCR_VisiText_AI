from flask import Flask, request, render_template
import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from PIL import Image
import time

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Azure credentials
subscription_key = "<YOUR_AZURE_SUBSCRIPTION_KEY>"
endpoint = "<YOUR_AZURE_ENDPOINT>"
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files['image']
        if uploaded_file.filename != '':
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(file_path)

            with open(file_path, "rb") as image_stream:
                read_response = computervision_client.read_in_stream(image_stream, raw=True)
                operation_location = read_response.headers["Operation-Location"]
                operation_id = operation_location.split("/")[-1]

            # Wait for the OCR operation to complete
            while True:
                result = computervision_client.get_read_result(operation_id)
                if result.status not in ['notStarted', 'running']:
                    break
                time.sleep(1)

            extracted_text = ""
            if result.status == OperationStatusCodes.succeeded:
                for page in result.analyze_result.read_results:
                    for line in page.lines:
                        extracted_text += line.text + "\n"

            return render_template("index.html", text=extracted_text)

    return render_template("index.html", text="")

if __name__ == "__main__":
    app.run(debug=True)
