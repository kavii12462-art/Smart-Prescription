import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load trained model
model = tf.keras.models.load_model("model/pill_model.h5")

# Class names (must match your folder names)
class_names = [
    "amoxicillin",
    "aspirin",
    "cetirizine",
    "ibuprofen",
    "paracetamol"
]

def predict_pill(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)
    index = np.argmax(prediction)

    return class_names[index]