# Local Python AIoT Demo 🌍

Welcome to the AIoT Sensor Dashboard demonstration project! 

### 🟢 Live Demo
You can view a working static snapshot of the UI deployed on Streamlit Community Cloud here:  
👉 **[Live Streamlit Dashboard](https://l7fhemzvwjudcbosk5xndt.streamlit.app/)**

---

## Project Overview

This project simulates an end-to-end AIoT (Artificial Intelligence of Things) system utilizing a local Python stack. It features an ESP32 simulator sending mock hardware telemetry to a Flask backend, which processes and stores the information in a database to be visualized by a modern Streamlit frontend.

### Architecture
- **Simulator (`esp32_sim.py`)**: A Python script simulating an ESP32 microcontroller. It generates dummy DHT11 temperature and humidity sensor data alongside Wi-Fi metadata (IP address, RSSI) and pushes it over HTTP POST every 5 seconds.
- **Backend API (`app.py`)**: A lightweight Flask server handling data ingestion at the `/sensor` endpoint and routing it directly to structured storage. It also exposes a `/health` endpoint for uptime monitoring.
- **Database (`aiotdb.db`)**: A local SQLite3 database persisting all timestamped metrics in a `sensors` table.
- **Frontend Dashboard (`dashboard.py`)**: A professional web application built in Streamlit. It fetches the latest 60 readings from the database and renders dynamic KPI metric cards alongside clean, full-width `st.line_chart` visualizations for both temperature and humidity trends.

## How to Run Locally

If you clone this repository and want to run the full simulation stack on your local machine:

1. **Set up the environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. **Start the Backend API**:
   ```bash
   python app.py
   ```
   *(Runs on http://localhost:5000)*

3. **Start the ESP32 Simulator** (in a new terminal):
   ```bash
   python esp32_sim.py
   ```

4. **Start the Dashboard** (in a new terminal):
   ```bash
   streamlit run dashboard.py
   ```
   *(Runs on http://localhost:8501)*
