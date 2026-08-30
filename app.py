from flask import Flask, render_template, request
import os

from utils.predictor import predict_pill
from utils.database import get_medicine_info
from utils.interaction_checker import check_interaction
from utils.ocr_reader import extract_text
from utils.medicine_detector import detect_medicines

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template(
        "index.html",
        prediction=None,
        medicine=None,
        image=None,
        ocr_text=None,
        medicines=[],
        interaction_result=None
    )


# ---------------- AI PILL RECOGNITION ----------------
@app.route("/upload", methods=["POST"])
def upload():

    prediction = None
    medicine = None
    image = None

    if "pill_image" in request.files:

        file = request.files["pill_image"]

        if file.filename != "":

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)

            image = file.filename

            prediction = predict_pill(filepath)

            medicine = get_medicine_info(prediction)

    return render_template(
        "index.html",
        prediction=prediction,
        medicine=medicine,
        image=image,
        ocr_text=None,
        medicines=[],
        interaction_result=None
    )



    # ---------------- OCR ----------------
@app.route("/ocr", methods=["POST"])
def ocr():

    text = None
    medicines = []
    image = None

    if "prescription" in request.files:

        file = request.files["prescription"]

        if file.filename != "":

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)

            image = file.filename

            text = extract_text(filepath)

            medicines = detect_medicines(text)

    return render_template(
        "index.html",
        prediction=None,
        medicine=None,
        image=image,
        ocr_text=text,
        medicines=medicines,
        interaction_result=None
    )
    
# ---------------- DRUG INTERACTION ----------------
@app.route("/interaction", methods=["POST"])
def interaction():

    med1 = request.form.get("medicine1", "").strip().lower()
    med2 = request.form.get("medicine2", "").strip().lower()

    result = check_interaction(med1, med2)

    return render_template(
        "index.html",
        prediction=None,
        medicine=None,
        image=None,
        ocr_text=None,
        medicines=[],
        interaction_result=result
    )


# ---------------- RUN APPLICATION ----------------
if __name__ == "__main__":
    app.run(debug=True)