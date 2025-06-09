# Copyright Form Classifier

A Python script that uses OCR (Tesseract) and OpenCV to classify scanned images as either copyright-related forms or general documents.

## Features
- Image preprocessing with OpenCV
- OCR using Tesseract
- Keyword-based classification
- Sorts images into two folders: `copyright_forms` and `random_images`

## Requirements

- Python 3
- Tesseract OCR (must be installed and path set)
- Required libraries: `pytesseract`, `opencv-python`, `Pillow`, `numpy`

## Installation

```bash
pip install pytesseract opencv-python pillow numpy
