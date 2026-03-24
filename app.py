import os
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)

# Render uses Postgres, local uses SQLite
DB_URL = os.environ.get("DATABASE_URL", "sqlite:///aiotdb.db")
if DB_URL.startswith("postgres://"):
    DB_URL = DB_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DB_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class SensorData(Base):
    __tablename__ = 'sensors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=func.now())
    temp = Column(Float)
    hum = Column(Float)
    device_id = Column(String)
    ip = Column(String)
    rssi = Column(Integer)

def init_db():
    Base.metadata.create_all(engine)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/sensor', methods=['POST'])
def sensor_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    try:
        session = Session()
        new_entry = SensorData(
            temp=data.get('temp'),
            hum=data.get('hum'),
            device_id=data.get('device_id'),
            ip=data.get('ip'),
            rssi=data.get('rssi')
        )
        session.add(new_entry)
        session.commit()
        session.close()
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
else:
    # Gunicorn calls this when importing the app
    init_db()
