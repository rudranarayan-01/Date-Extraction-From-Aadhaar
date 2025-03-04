# Aadhaar OCR - Extract Dates from Aadhaar Card using OpenCV & Django

## Overview
This project extracts dates (such as Date of Birth) from an Aadhaar card using Optical Character Recognition (OCR) with OpenCV and Django.

## Features
- Upload Aadhaar card images via a web interface
- Preprocess images using OpenCV for better OCR accuracy
- Extract text from images using Tesseract OCR
- Identify dates in formats like `DD/MM/YYYY` or `YYYY`

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- OpenCV (`opencv-python`)
- Tesseract OCR ([Install Here](https://github.com/UB-Mannheim/tesseract/wiki))

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/rudranarayan-01/Date-Extraction-From-Aadhaar
cd Date-Extraction-From-Aadhaar
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Tesseract OCR Path (Windows Users)
Edit `utils.py` and update the Tesseract path:
```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
```

**or**
simply add the tesseract folder path in environment variable where **tesseract.exe** exists


## Usage

### 1. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Start the Django Development Server
```bash
python manage.py runserver
```

### 3. Upload Aadhaar Image
- Open `http://127.0.0.1:8000/ocr/upload/` in your browser
- Upload an Aadhaar card image
- The extracted dates will be displayed as JSON response

## Project Structure
```
├── aadhar_ocr
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── ...
│
├── ocr_app
│   ├── models.py       # Database Model
│   ├── views.py        # OCR Processing Logic
│   ├── utils.py        # Image Preprocessing & Text Extraction
│   ├── forms.py        # Upload Form
│   ├── templates/
│   │   ├── upload.html # Upload Page
│   ├── urls.py         # App URL Configurations
│
├── media/aadhaar_images/ # Uploaded Images
├── manage.py
└── README.md
```

## OCR Process
1. **Preprocess Image**: Convert to grayscale & apply thresholding.
2. **Extract Text**: Use Tesseract OCR to read text.
3. **Extract Dates**: Use regex to identify date patterns (`DD/MM/YYYY` or `YYYY`).

## Future Enhancements
- Improve OCR accuracy with custom training.
- Add support for multiple languages (Hindi, English, etc.).
- Store extracted details in a database.

## License
This project is licensed under the MIT License.

## Contact
For queries, contact [Rudranarayan Sahu](mailto:rudranarayansahu.tech@gmail.com) or visit my [GitHub](https://github.com/rudranarayan-01).


**Website** - https://akash0101.pythonanywhere.com



