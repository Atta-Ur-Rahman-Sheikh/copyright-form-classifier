import os
import pytesseract
from PIL import Image
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Keywords for detection
KEYWORDS = [
    "certificate of registration", "title", "completion", "publication",
    "author", "copyright claimant", "rights and permissions", "certification"
]

# Preprocessing
def preprocess_image(image_path):
    try:
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return thresh
    except Exception as e:
        print(f"[ERROR] Could not preprocess {image_path}: {e}")
        return None

def is_copyright_form(image_path):
    processed = preprocess_image(image_path)
    if processed is None:
        return False

    try:
        text = pytesseract.image_to_string(processed).lower()
        print(f"\n[DEBUG] Text from {os.path.basename(image_path)}:\n{text}\n")
        match_count = sum(1 for keyword in KEYWORDS if keyword in text)
        return match_count >= 3  # 3–5 for stricter match
    except Exception as e:
        print(f"[ERROR] OCR failed on {image_path}: {e}")
        return False

def classify_images(input_folder, output_folder_form, output_folder_other):
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder_form, exist_ok=True)
    os.makedirs(output_folder_other, exist_ok=True)

    images = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]

    if not images:
        print(f"[INFO] No images found in '{input_folder}'. Please add your images there.")
        return

    for filename in images:
        full_path = os.path.join(input_folder, filename)
        try:
            if is_copyright_form(full_path):
                os.rename(full_path, os.path.join(output_folder_form, filename))
                print(f"[✓] {filename} → copyright_forms")
            else:
                os.rename(full_path, os.path.join(output_folder_other, filename))
                print(f"[✗] {filename} → random_images")
        except Exception as e:
            print(f"[ERROR] Failed to classify {filename}: {e}")

# === Main ===
input_folder = r"C:\Users\Atta-Laptop\Desktop\sample copyright\sample copyright\TASK\all_images"
form_folder = r"C:\Users\Atta-Laptop\Desktop\sample copyright\sample copyright\TASK\copyright_forms"
other_folder = r"C:\Users\Atta-Laptop\Desktop\sample copyright\sample copyright\TASK\random_images"

classify_images(input_folder, form_folder, other_folder)
