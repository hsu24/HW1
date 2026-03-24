import time
import random
import requests
import datetime

URL = "http://localhost:5000/sensor"
DEVICE_ID = "ESP32_AIoT_Demo"
IP_ADDR = "192.168.x.x"
RSSI = -50

def generate_data():
    temp = round(random.uniform(22.0, 26.0), 1)
    hum = round(random.uniform(40.0, 60.0), 1)
    rssi = random.randint(-80, -40)
    
    return {
        "temp": temp,
        "hum": hum,
        "device_id": DEVICE_ID,
        "ip": IP_ADDR,
        "rssi": rssi
    }

def run_simulation():
    print(f"Starting ESP32 Simulator... Target: {URL}")
    while True:
        payload = generate_data()
        try:
            response = requests.post(URL, json=payload, timeout=5)
            print(f"[{datetime.datetime.now()}] Sent {payload} => {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[{datetime.datetime.now()}] Error connecting to server: {e}")
        time.sleep(5)

if __name__ == "__main__":
    run_simulation()
