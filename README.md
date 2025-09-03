# Plant Disease Prediction App

This project is a web application built with **Streamlit** and a trained **CNN model** that can predict plant diseases from leaf images.

---

# Features
- Upload a plant leaf image (JPG/PNG)
- The model predicts if the plant is healthy or diseased
- Simple and interactive UI built with Streamlit
- Dockerized for easy deployment

---

##  Project Structure
plant_pred_app/
│-- app.py # Main Streamlit app
│-- requirements.txt # Python dependencies
│-- Dockerfile # Docker  file
│-- .gitignore # Ignore unnecessary files for git
│-- class_indices.json #  model classes used for prediction
│-- trained_model/ # model is downloaded here at runtime

---

## Docker tips
- create an image with the command 'docker build -t plant_pred_app .'
- make a container instance using 'docker run -p 8501:8501 plant_pred_app'
  where 8501 is the port number streamlit will run on.
