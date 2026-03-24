# AIoT Sensor Dashboard

This project is a local Python AIoT demonstration suite featuring an ESP32 simulator, a Flask backend with SQLite3 database, and a professional Streamlit dashboard.

## Live Demo
Watch the dashboard in action:

![Live Demo](demo.webp)

## Features
- **Real-time Simulator**: `esp32_sim.py` generates dummy DHT11 temperature and humidity data every 5 seconds.
- **Flask Backend & DB**: `app.py` exposes REST APIs (`/sensor`, `/health`) and stores data persistently in an SQLite database.
- **Streamlit Frontend**: `dashboard.py` visually renders the timeline data natively with KPIs and raw data expansion.

## How To Run Locally
1. Activate the Virtual Environment: `.\venv\Scripts\Activate.ps1`
2. Start the Backend: `python app.py`
3. Start the Simulator: `python esp32_sim.py`
4. Start the Dashboard: `streamlit run dashboard.py`
