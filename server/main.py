from typing import Dict
from server.test.application_test import load_model
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello", methods=["POST"])
def hello():
    print(request.json)
    return f"Hello {request.json['name']}!"


@app.route("/predict", methods=["POST"])
def predict(data: any):
    model_filename = "trained_model.pkl"
    model = load_model(model_filename)

    names = ['Temperature', 'Humidity', 'Sound Volume']

    features = [data[name]['value'] for name in names]
    predicted_label = model.predict([features])[0]
    return predicted_label

if __name__ == '__main__':
    app.run(debug=True)
