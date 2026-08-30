import easyocr

# Create OCR reader
reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image_path):
    """
    Extract text from a prescription image.
    """

    result = reader.readtext(image_path, detail=0)

    return result