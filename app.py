import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_NAME = 'aiotdb.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sensors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            temp REAL,
            hum REAL,
            device_id TEXT,
            ip TEXT,
            rssi INTEGER
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/sensor', methods=['POST'])
def sensor_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('''
            INSERT INTO sensors (temp, hum, device_id, ip, rssi)
            VALUES (?, ?, ?, ?, ?)
        ''', (data.get('temp'), data.get('hum'), data.get('device_id'), data.get('ip'), data.get('rssi')))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
