from typing import Any, Dict
from flask import Flask, request
from common import load_model

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data:  Dict[str, Any] = request.get_json()
    model_filename = "trained_model.pkl"
    model = load_model(model_filename)
    names = ["Temperature", "Humidity", "Sound Volume"]
    features = [data[name]["value"] for name in names]
    predicted_label = model.predict([features])[0]
    return {'predicted_label': predicted_label}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)
