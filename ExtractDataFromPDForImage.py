import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import cv2
from PyPDF2 import PdfFileReader, PdfFileWriter
import re


tempImageFile = r"D:\Aadesh\Extra\tesseractOCR/tempImg.jpg"
tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
poppler_path = r"D:\Aadesh\Extra\tesseractOCR\poppler-0.67.0\bin"


def forPdf(filepath, pagelimit=5):
    pdf = PdfFileReader(filepath,strict=False)
    pdfWriter = PdfFileWriter()
    if pagelimit > pdf.numPages:
        limit = pdf.numPages
    else:
        limit = pagelimit
    for i in range(limit):
        pdfWriter.addPage(pdf.getPage(i))
    with open('temp.pdf', 'wb') as f:
        pdfWriter.write(f)
        f.close()
    pages = convert_from_path('temp.pdf', 500, poppler_path=poppler_path)
    data = ""
    for i in range(limit):
        page = pages[i]
        page.save(tempImageFile,"JPEG")
        try:
            osd = pytesseract.image_to_osd(tempImageFile)
            angle = re.search('(?<=Rotate: )\d+',osd).group(0)
        except:
            angle = "0"
        if angle != "0":
            im = Image.open(tempImageFile)
            out = im.rotate(int(angle),expand=True)
            out.save(tempImageFile)
        text = str(pytesseract.image_to_string(Image.open(tempImageFile)))
        text = text.replace('\n'," ")
        data = data+" "+text
    return data


def forImage(filepath):
    image = cv2.imread(filepath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    thresh = cv2.GaussianBlur(thresh,(3,3),0)
    data = pytesseract.image_to_string(thresh)
    return data


def ExtractData(filepath,filetype):
    pytesseract.pytesseract.tesseract_cmd = tesseract
    if filetype == "pdf":
        data = forPdf(filepath)
        return data
    elif filetype == "image":
        data = forImage(filepath)
        return data
    else:
        return None


def inferType(filepath):
    filename,fileExtension = os.path.splitext(filepath)
    if fileExtension == ".pdf" or fileExtension == ".PDF":
        return "pdf"
    elif fileExtension == ".jpeg" or ".bmp" or ".tiff" or ".png":
        return "image"
    else:
        return None


def main(filepath):
    filetype = inferType(filepath)
    data = ExtractData(filepath,filetype)
    print(data)


if __name__ == "__main__":
    main(r"D:\Aadesh\Aadesh_Dalvi_Resume.pdf")
