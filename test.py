# http://127.0.0.1:8000/api/sensor/?value=45

import time
import random
import requests

API_URL_ANALOG = "http://127.0.0.1:8000/api/sensor/"
API_URL_DIGITAL = "http://127.0.0.1:8000/api/digital/"

def send_fake_sensor_data():
    while True:
        value = random.uniform(0, 1)
        value2 = random.randint(0, 1)
        try:
            response = requests.get(API_URL_ANALOG, params={'value': value})
            print(f"Sent value: {value} | Status: {response.status_code}")

            response = requests.get(API_URL_DIGITAL, params={'value': value2})
            print(f"Sent value2: {value2} | Status2: {response.status_code}")

        except Exception as e:
            print(f"Error sending data: {e}")
        time.sleep(0.5)

if __name__ == "__main__":
    send_fake_sensor_data()






