# AIoT Sensor Dashboard Demo 🌍

This repository houses a full-stack Python AIoT demonstration suite built for simulating, ingesting, and visualizing hardware sensor telemetry in real-time. 

## 🚀 Live Demo
You can view a live hosted version of this dashboard (configured with a static dataset snapshot) on Streamlit Community Cloud:

**[View Live App on Streamlit Cloud](https://share.streamlit.io/hsu24/hw1/main/dashboard.py)** *(Note: this URL will automatically redirect to your deployed app!)*

## 🛠️ System Architecture
The application is decoupled into three primary components:

- **Hardware Simulator (`esp32_sim.py`)**: A background mock script mimicking an ESP32 hardware device. It generates fake DHT11 Temperature, Humidity, and network RSSI metrics every 5 seconds and POSTs them to the backend API.
- **Backend API (`app.py`)**: A lightweight Flask server listening on port `5000`. It processes incoming JSON telemetry from the simulator and securely stores the metrics into a local SQLite database (`aiotdb.db`). It also exposes a `/health` endpoint for uptime verification.
- **Frontend Dashboard (`dashboard.py`)**: A modern, interactive Streamlit web application. It reads directly from the SQLite database to plot continuous sensor data onto UI line charts and metric cards.

## ⚙️ How to Run Locally

If you wish to spin up the entire active demo locally, follow these steps:

### 1. Environment Setup
```powershell
# Create and activate the virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install the required dependencies
pip install -r requirements.txt
```

### 2. Execution
You will need three separate terminal windows open in this directory to run the active demo concurrently:

```powershell
# Terminal 1: Start the backend Flask API
python app.py

# Terminal 2: Start the frontend dashboard UI
streamlit run dashboard.py

# Terminal 3: Start the hardware data simulator
python esp32_sim.py
```

Once the backend is listening and the simulator is transmitting, open your browser to `http://localhost:8501`. Toggle the **"Auto-refresh data (Live Mode)"** checkbox within the dashboard to watch the telemetry stream update dynamically!
