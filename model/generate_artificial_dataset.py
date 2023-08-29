import json

from common.generate_sensor_data import generate_sensor_data


"""This file generates a JSON file that contains artificial data for training and testing the model.
"""


if __name__ == "__main__":
    # Generate data
    data = [generate_sensor_data() for _ in range(10000)]

    # Save the data to a JSON file
    with open("dataset.json", "w") as file:
        json.dump(data, file)
