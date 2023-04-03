import numpy as np
import pytesseract
from pdf2image import convert_from_path


def pdf_ocr(fname, **kwargs):
    images = convert_from_path(fname, **kwargs)
    text = ''
    for img in images:
        img = np.array(img)
        text += pytesseract.image_to_string(img)

    return text


fname = 'png2pdf.pdf'
# text = pdf_ocr(fname, first_page=7, last_page=8)
text = pdf_ocr(fname)
print(text)

# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:C:\Program Files\Tesseract-OCR
# echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:C:\Program Files\Tesseract-OCR' >> ~/.bashrc
# ***failed
