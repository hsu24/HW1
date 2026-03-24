#include <HTTPClient.h>
#include <SimpleDHT.h>
#include <WiFi.h>


// ===== WiFi 設定 =====
const char *ssid = "你的WiFi名稱";
const char *password = "你的WiFi密碼";

// ===== Flask API =====
const char *serverUrl = "http://你的IP:5000/sensor";
// ⚠️ 本機測試用 192.168.x.x
// ⚠️ Render 用 https://xxx.onrender.com/sensor

// ===== DHT11 =====
int pinDHT11 = 15;
SimpleDHT11 dht11;

void setup() {
  Serial.begin(115200);

  // 連 WiFi
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi...");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected!");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // ===== 讀取 DHT11 =====
  byte temperature = 0;
  byte humidity = 0;
  int err = SimpleDHTErrSuccess;

  if ((err = dht11.read(pinDHT11, &temperature, &humidity, NULL)) !=
      SimpleDHTErrSuccess) {
    Serial.print("DHT11 Error: ");
    Serial.println(err);
    delay(2000);
    return;
  }

  Serial.print("Temp: ");
  Serial.print((int)temperature);
  Serial.print("C  Humidity: ");
  Serial.print((int)humidity);
  Serial.println("%");

  // ===== 傳送 HTTP POST =====
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    // JSON 資料 (Updated to match app.py expected keys)
    String ipStr = WiFi.localIP().toString();
    int rssi = WiFi.RSSI();
    
    String jsonData = "{";
    jsonData += "\"device_id\":\"esp32_real_001\",";
    jsonData += "\"temp\":" + String((int)temperature) + ",";
    jsonData += "\"hum\":" + String((int)humidity) + ",";
    jsonData += "\"ip\":\"" + ipStr + "\",";
    jsonData += "\"rssi\":" + String(rssi);
    jsonData += "}";

    int httpResponseCode = http.POST(jsonData);

    if (httpResponseCode > 0) {
      Serial.print("POST OK, code: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("POST failed: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  } else {
    Serial.println("WiFi disconnected");
  }

  delay(5000); // 每 5 秒送一次
}