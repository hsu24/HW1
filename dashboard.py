import os
import pandas as pd
import streamlit as st
import time
from sqlalchemy import create_engine

DB_URL = os.environ.get("DATABASE_URL", "sqlite:///aiotdb.db")
if DB_URL.startswith("postgres://"):
    DB_URL = DB_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DB_URL)

def load_data():
    try:
        # Limit to the most recent 60 readings
        df = pd.read_sql_query("SELECT * FROM sensors ORDER BY timestamp DESC LIMIT 60", engine)
        return df
    except Exception:
        return pd.DataFrame()

st.set_page_config(page_title="AIoT Dashboard", page_icon="🌍", layout="wide")

# Inject Custom CSS
st.markdown("""
<style>
    /* Hide Streamlit default UI components */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Style the main container padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Style the metrics cards */
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border: 1px solid #e9ecef;
        padding: 5% 5% 5% 10%;
        border-radius: 12px;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.04);
        color: #1E3A8A;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-4px);
        box-shadow: 2px 8px 15px rgba(0,0,0,0.1);
    }
    
    /* Font styling */
    h1, h2, h3 {
        color: #1a202c;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; margin-bottom: 30px;'>🌍 AIoT Sensor Dashboard</h1>", unsafe_allow_html=True)

df = load_data()

if df.empty:
    st.info("📡 Scanning for sensor data... Waiting for esp32_sim to ingest data.")
    time.sleep(2)
    st.rerun()
else:
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # KPIs
    st.markdown("### Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    avg_temp = df['temp'].mean()
    avg_hum = df['hum'].mean()
    latest_temp = df.iloc[0]['temp']
    latest_hum = df.iloc[0]['hum']
    
    col1.metric("🌡️ Latest Temp", f"{latest_temp:.1f} °C")
    col2.metric("💧 Latest Humidity", f"{latest_hum:.1f} %")
    col3.metric("📈 Avg. Temp", f"{avg_temp:.1f} °C")
    col4.metric("📊 Avg. Humidity", f"{avg_hum:.1f} %")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Chronological sort for plotting left-to-right
    plot_df = df.sort_values('timestamp')

    # Charts: Temperature above, Humidity below
    st.markdown("### 🌡️ Temperature Overview")
    st.line_chart(plot_df.set_index('timestamp')['temp'], color="#FF4B4B")
    
    st.markdown("### 💧 Humidity Overview")
    st.line_chart(plot_df.set_index('timestamp')['hum'], color="#1E88E5")
        
    # Data Table
    with st.expander("📄 View Raw Sensor Data"):
        st.dataframe(df, use_container_width=True)

    time.sleep(2)
    st.rerun()
