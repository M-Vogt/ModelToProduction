import json
import numpy as np
import pickle
import time
import sys

def load_model(model_filename):
    with open(model_filename, 'rb') as f:
        model = pickle.load(f)
    return model

def generate_data(names, min_vals, max_vals):
    data = {}

    # Generate Values while very high and very low values are unlikely
    mu = np.mean([min_val + max_val for min_val, max_val in zip(min_vals, max_vals)]) / 2
    sigma = np.std([min_val + max_val for min_val, max_val in zip(min_vals, max_vals)]) / 6
    values = np.random.normal(mu, sigma, size=len(names))
    values = np.clip(values, min_vals, max_vals)
    values = np.round(values, decimals=2)

    # Calculate anomaly probability based on the sum of values
    anomaly_probability = np.sum(values) / (np.sum(max_vals) * len(names))
    anomaly_probability = min(anomaly_probability, 0.1)  # Limit the anomaly probability
    label = np.random.choice(['normal', 'anomaly'], p=[1 - anomaly_probability, anomaly_probability])

    for name, value in zip(names, values):
        data[name] = {'value': value}

    return data, label


if __name__ == '__main__':
    # Load the trained model
    model_filename = "trained_model.pkl"
    model = load_model(model_filename)

    names = ['Temperature', 'Humidity', 'Sound Volume']
    min_vals = [20, 0, 80]
    max_vals = [120, 100, 130]

    iteration = 0
    correct_predictions = 0

    while True:
        data, label = generate_data(names, min_vals, max_vals)


        # Flush the output to display it immediately
        sys.stdout.flush()

        # Perform prediction
        features = [data[name]['value'] for name in names]
        predicted_label = model.predict([features])[0]

        # Check if label and predicted label are the same
        if label == predicted_label:
            correct_predictions += 1

        iteration += 1

        # Perform accuracy analysis every 10 iterations
        if iteration % 1000 == 0:
            accuracy = correct_predictions / iteration
            print("Accuracy Analysis - Iteration:", iteration)
            print("Correct Predictions:", correct_predictions)
            print("Total Iterations:", iteration)
            print("Accuracy:", accuracy)
            print()

