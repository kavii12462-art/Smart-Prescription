from utils.ocr_reader import extract_text

image_path = "static/uploads/test.jpg"

text = extract_text(image_path)

print("Detected Text:")

for line in text:
    print(line)