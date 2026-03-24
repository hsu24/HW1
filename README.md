# Local Python AIoT Workspace 🌍

Welcome to the fully functional AIoT Sensor demonstration project. This repository contains both a software-only simulation environment and the code required to run the stack on real physical ESP32 hardware!

### 🟢 Live Demo Snapshot
You can view a working static snapshot of the UI deployed on Streamlit Community Cloud here:  
👉 **[Live Streamlit Dashboard](https://l7fhemzvwjudcbosk5xndt.streamlit.app/)**
<img width="1872" height="1060" alt="螢幕擷取畫面 2026-03-25 015710" src="https://github.com/user-attachments/assets/536a8837-15da-4df1-a261-cac2cdcfb618" />

---

## Architecture Overview

This project demonstrates an end-to-end AIoT system with the following framework:
- **Backend API (`app.py`)**: A lightweight Flask server handling data ingestion at the `/sensor` endpoint. It parses incoming HTTP POST JSON data.
- **Database (`aiotdb.db`)**: A local SQLite database storing all timestamped metrics in a `sensors` table.
- **Frontend Dashboard (`dashboard.py`)**: A professionally styled Streamlit application that fetches the latest 60 readings from the database, displaying dynamic KPI metric cards, raw data tables, and `st.line_chart` visualizations for temperature and humidity.

---

## Deployment Modes

The beauty of this architecture is that the **same Backend API and Dashboard frontend work seamlessly for both the simulation AND the real hardware!** You do not need to rewrite the server architecture to switch between modes.

### Mode 1: Simulation Version
*Ideal for testing the UI, API, and database without spinning up physical hardware.*

- **Hardware Requirement**: None.
- **Data Source**: `esp32_sim.py`
  - A Python script generating randomized dummy DHT11 temperature/humidity data. It runs locally and automatically pushes this generated data to the Flask API every 5 seconds.

### Mode 2: Real Hardware Version
*Ideal for real-world live IoT deployment.*

- **Hardware Requirement**: ESP32 Microcontroller + DHT11 Sensor.
- **Data Source**: `esp32_real.cpp`
  - A C++ script utilizing `WiFi.h`, `HTTPClient.h`, and the `SimpleDHT11` library to capture real-world environmental data and POST it directly over Wi-Fi to your Flask backend.
  - Accompanied by `platformio.ini` which handles the ESP32 framework dependencies natively.

---

## How to Run Locally

If you cloned this repository and want to run it on your local network:

1. **Set up the Python Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. **Start the Central Backend API** (Keep this running):
   ```bash
   python app.py
   ```

3. **Start the Streamlit Dashboard** (Keep this running in a second terminal):
   ```bash
   streamlit run dashboard.py
   ```

4. **Choose your Data Source**:
   - **For Simulation**: Open a third terminal window and run `python esp32_sim.py`.
   - **For Real Hardware**: Update `esp32_real.cpp` with your Wi-Fi credentials and your computer's local IP address, flash the code to your ESP32 board via PlatformIO or the Arduino IDE, and watch the physical device begin logging data live to your Streamlit dashboard!
