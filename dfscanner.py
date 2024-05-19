import numpy as np
import cv2
from tensorflow.keras.models import load_model
import os

# Path to your trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model01.h5')

# Load the trained model
def load_trained_model():
    return load_model(MODEL_PATH)

# Function to preprocess input image
def preprocess_input_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (64, 64))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Function to predict deepfake
def predict_deepfake(model, image_path):
    input_image = preprocess_input_image(image_path)
    prediction = model.predict(input_image)
    if prediction[0][0] > 0.6:
        return "Real"
    else:
        return "Fake"
