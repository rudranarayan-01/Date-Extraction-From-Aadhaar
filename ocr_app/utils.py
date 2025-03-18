import cv2
import pytesseract
import re

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding for better text detection
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresh

def extract_text(image):
    return pytesseract.image_to_string(image, lang="eng")

def extract_dates(text):
    date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'  # Format DD/MM/YYYY
    year_pattern = r'\b\d{4}\b'  # Match only year

    dates = re.findall(date_pattern, text)
    years = re.findall(year_pattern, text)

    return dates if dates else years  # Return years if no full dates found
 
