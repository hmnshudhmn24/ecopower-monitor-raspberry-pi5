import time
import random
import csv
from datetime import datetime

def read_sensor_data():
    # Simulated sensor value in watts
    return round(random.uniform(50, 300), 2)

def read_power_data():
    power = read_sensor_data()
    now = datetime.now().strftime("%H:%M:%S")
    with open("usage_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([now, power])

if __name__ == "__main__":
    with open("usage_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "Power(W)"])
    while True:
        read_power_data()
        time.sleep(5)