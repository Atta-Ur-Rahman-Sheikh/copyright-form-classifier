## Copyright Form Classifier

This Python script uses **Tesseract OCR** and **OpenCV** to automatically classify images as either **copyright-related forms** or **other documents**. It processes images using grayscale, blurring, and thresholding before applying OCR to extract text and match against key copyright-related terms.

## ✨ Features

- OCR text extraction using Tesseract
- Image preprocessing with OpenCV (grayscale, blur, thresholding)
- Keyword-based classification
- Automatically sorts images into:
  - `copyright_forms/`
  - `random_images/`

## 🔧 Requirements

- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (must be installed)
- Python packages:
  - `pytesseract`
  - `opencv-python`
  - `Pillow`
  - `numpy`

Install dependencies with:

```bash
pip install pytesseract opencv-python pillow numpy
````

## ⚙️ Setup

1. Install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
2. Update the script with the correct path to `tesseract.exe`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

3. Modify the folder paths at the bottom of the script:

```python
input_folder = r"path\to\your\input_images"
form_folder = r"path\to\copyright_forms"
other_folder = r"path\to\random_images"
```

## 🚀 Usage

Run the script:

```bash
python classifier.py
```

It will:

* Preprocess all images in the input folder
* Use OCR to extract and check text
* Move files to the appropriate output folder based on matched keywords

## 📁 Folder Structure Example

```
project/
│
├── classifier.py
├── README.md
├── .gitignore
├── input_images/
├── copyright_forms/
└── random_images/
```

## 📌 Notes

* The script checks for at least **3 keyword matches** to classify an image as a copyright form.
* You can adjust the list of keywords or threshold for stricter/looser classification.

---

