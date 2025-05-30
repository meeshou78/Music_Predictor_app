# File: app.py
from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")  # Load the same scaler used in training

FEATURES = [
    "danceability", "energy", "valence", 
    "speechiness", "acousticness", "tempo", "duration"
]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    if request.method == "POST":
        try:
            inputs = [float(request.form[f]) for f in FEATURES]
            scaled = scaler.transform([inputs])
            proba = model.predict_proba(scaled)[0]
            result = np.argmax(proba)
            prediction = "Popular" if result == 1 else "Not Popular"
            confidence = round(100 * proba[result], 2)
        except Exception as e:
            prediction = f"Error: {str(e)}"
            confidence = "N/A"
    return render_template("index.html", prediction=prediction, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)

