# OCR VisiText AI

A **Flask-based** web application that allows users to upload images and extract structured text using **Azure Cognitive Services**. This project serves as an end-to-end demo of OCR capabilities, integrating with Azure Blob Storage, SQL Database, Document Intelligence, and more.

---

## 🚀 Features

- Upload PNG/JPG/TIFF images via a web interface.
- Extract text using Azure’s **Computer Vision Read API (OCR v3.2+)**.
- Store images in **Azure Blob Storage**.
- Save extracted data in **Azure SQL Database**.
- Use **Azure Document Intelligence** for parsing structured documents.
- Modular code supports future extensions (e.g., CSV export, multi-language OCR).

---


---

## 🔧 Setup & Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Raviteja-Beri/OCR_VisiText_AI.git
    cd OCR_VisiText_AI
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Assign your `KEYS` in the project code:
    ```ini
    AZURE_SUBSCRIPTION_KEY=your-azure-subscription-key
    AZURE_ENDPOINT=https://<your-region>.api.cognitive.microsoft.com/
    ```

4. Run the Flask app:
    ```bash
    flask run
    ```
    Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🧠 Usage & Extensions

- Upload a valid image via the web form.
- The app will:
  1. Save the file (locally + Blob Storage).
  2. Run OCR with Azure Computer Vision.
  3. Parse structured data using Document Intelligence (for advanced layouts/forms).
  4. Store extracted text and metadata in Azure SQL.

- Easily extendable to:
  - Bulk image upload processing
  - Exporting results to CSV or PDF
  - Multilingual OCR support
  - NLP post-processing (e.g., entity recognition, classification)

---

## 📈 Tech Stack

| Layer                   | Technology                        |
|-------------------------|-----------------------------------|
| Web Backend             | Python + Flask                    |
| OCR / AI Integration    | Azure Computer Vision Read API    |
| Document Parsing        | Azure Document Intelligence       |
| File Storage            | Azure Blob Storage                |
| Data Storage            | Azure SQL Database                |
| Local Testing           | `uploads/` folder                 |

---

## 📚 Learnings & Insights

1. During this project, I gained experience in:

2. Building end-to-end AI workflows on Azure

3. Secure secrets management

4. Integrating multiple Azure services cohesively

5. Building a user-friendly front end with Flask

6. Preparing pipelines for document automation and OCR accuracy

---

## Thank You🙏



