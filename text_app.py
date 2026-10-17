import streamlit as st
import tensorflow as tf

model = tf.keras.models.load_model("text_cnn_model.keras")

st.title("Review Sentiment Classifier")

review = st.text_area(
    "Enter your review:",
    placeholder="Type a review here..."
)

if st.button("Predict"):

    if review.strip() == "":
        st.warning("Please enter a review.")

    else:
        input_text = tf.constant([review])

        prediction = model.predict(input_text, verbose=0)

        score = float(prediction[0][0])

        if score >= 0.5:
            st.success("Prediction: Positive")
            st.write(f"Confidence: {score * 100:.2f}%")
        else:
            st.error("Prediction: Negative")
            st.write(f"Confidence: {(1-score) * 100:.2f}%")
