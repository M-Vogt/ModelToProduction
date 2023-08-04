import sys
import time

from common.generate_sensor_data import generate_sensor_data


if __name__ == '__main__':
    while True:
        data, label = generate_sensor_data()

        for name, value_data in data.items():
            print(name + ": ", value_data)
        
        print(f"Label: {label}\n")

        # Flush the output to display it immediately
        sys.stdout.flush()

        # Optional: Pause for a certain time interval between data points
        time.sleep(1)
