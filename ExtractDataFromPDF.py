import pytesseract
from pdf2image import convert_from_path


poppler_path = r"D:\Aadesh\Extra\tesseractOCR\poppler-0.67.0\bin"


def ExtractData(filepath, pagelimit=2):
    data = ""
    try:
        doc = convert_from_path(filepath,poppler_path=poppler_path)
        for page_number, page_data in enumerate(doc):
            txt = pytesseract.image_to_string(page_data).encode("utf-8")
            data = data + " " + txt.decode("utf-8")
            if page_number > pagelimit-1:
                break
    except:
        print("Error while extracting data")
    return data


def main(filepath):
    data = ExtractData(filepath)
    print(data)


if __name__ == "__main__":
    main(r"D:\Aadesh\Extra\LifeIns\Medical Report.pdf")
