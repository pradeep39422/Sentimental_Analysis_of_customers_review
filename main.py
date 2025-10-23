import streamlit as st
import requests
import json
import os

# Prediction endpoint: default to local Flask server for development.
# Can be overridden by setting the PREDICTION_ENDPOINT environment variable.
prediction_endpoint = os.environ.get("PREDICTION_ENDPOINT", "http://127.0.0.1:5000/predict")

st.title("Text Sentiment Predictor")

# Text input for sentiment prediction
user_input = st.text_input("Enter text and click on Predict", "")

# Prediction on single sentence
if st.button("Predict"):
    if user_input.strip():
        try:
            response = requests.post(
                prediction_endpoint, 
                headers={"Content-Type": "application/json"},
                data=json.dumps({"text": user_input})
            )
            response_data = response.json()
            st.write(f"Predicted sentiment: {response_data['prediction']}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some text to analyze.")
