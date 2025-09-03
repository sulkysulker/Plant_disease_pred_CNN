import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import os, json
import gdown

working_dir = os.path.dirname(os.path.abspath(__file__))
file_id="1j_Bb0mLI-IIwy_6flTscx6yvyYvKA_fe"
url = f"https://drive.google.com/uc?id={file_id}"
output = f"{working_dir}/trained_model/plant_disease_prediction_model.h5"

if not  os.path.exists(output):
    gdown.download(url, output, quiet=False)

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(output)

model = load_model()
class_indices = json.load(open(f"{working_dir}/class_indices.json"))

def load_and_preprocess_image(image_path, target_size=(224, 224)):
    # Load the image
    img = Image.open(image_path)
    # Resize the image
    img = img.resize(target_size)
    # Convert the image to a numpy array
    img_array = np.array(img)
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    # Scale the image values to [0, 1]
    img_array = img_array.astype('float32') / 255.
    return img_array


# Function to Predict the Class of an Image
def predict_image_class(model, image_path, class_indices):
    preprocessed_img = load_and_preprocess_image(image_path)
    predictions = model.predict(preprocessed_img)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)]
    return predicted_class_name



st.title("🍃 Plant Disease Predictor")
st.sidebar.title("Hey there!!")
st.sidebar.write("This app uses a CNN model to identify plant diseases from leaf images.")

st.write("Upload an image of a plant leaf to find if the plant is healthy or has disease.")
uploaded_image = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", width=255)


    if st.button("Predict Disease"):
        st.write("Analyzing image...")
        prediction=predict_image_class(model,uploaded_image,class_indices)

        st.success(f"Analysis complete! This appears to be a {prediction}.")
