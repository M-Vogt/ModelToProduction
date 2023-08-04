import numpy as np


def generate_sensor_data():
    names = ['Temperature', 'Humidity', 'Sound Volume']
    min_vals = [20, 0, 80]
    max_vals = [120, 100, 130]

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
