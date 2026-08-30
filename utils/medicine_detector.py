def detect_medicines(text):

    # List of medicines available in your project
    medicines = [
        "paracetamol",
        "aspirin",
        "ibuprofen",
        "cetirizine",
        "amoxicillin"
    ]

    detected = []

    # Convert OCR output to lowercase
    full_text = " ".join(text).lower()

    for medicine in medicines:
        if medicine in full_text:
            detected.append(medicine.capitalize())

    return detected