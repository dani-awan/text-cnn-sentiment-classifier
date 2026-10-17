# Text CNN Sentiment Classifier

A Streamlit application that classifies review text as positive or negative
using a trained TensorFlow/Keras model.

## Run
Install dependencies:
    pip install -r requirements.txt

Start the app from this project folder:
    streamlit run text_app.py

## Files
- text_app.py: review input and prediction interface.
- text_cnn_model.keras: trained sentiment model.
- requirements.txt: application dependencies.

## Limitations
Training code and the dataset are not included in this upload.
The model returns a binary sentiment prediction.
Displayed confidence is a model score, not a calibrated probability.
Performance on new reviews has not been verified in this upload.
