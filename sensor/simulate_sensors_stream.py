import sys
import time

from pprint import pprint
from common.generate_sensor_data import generate_sensor_data


if __name__ == "__main__":
    while True:
        data, label = generate_sensor_data()

        # send the generated sensor data to the server
        import requests
        ret = requests.post('http://127.0.0.1:8080/predict', json=data)
        pprint(f'Sensor data:\n{data}')
        print(f'Result was: {ret.json()["predicted_label"]} / True label is: {label}')

        # for name, value_data in data.items():
        #     print(name + ": ", value_data)
        # print(f"Label: {label}\n")

        # Flush the output to display it immediately
        sys.stdout.flush()

        # Optional: Pause for a certain time interval between data points
        time.sleep(1)
