#include <DHT.h>
#include <WiFi.h>
#include <WebServer.h>
#include <WiFiClient.h>
#include <uri/UriBraces.h>
#include <WiFiClientSecure.h>

#define DHT_SENSOR_PIN  2
#define DHT_SENSOR_TYPE DHT11
#define WIFI_SSID ""
#define WIFI_PASSWORD ""

DHT dht_sensor(DHT_SENSOR_PIN, DHT_SENSOR_TYPE);
WebServer server(80);

void setup() {
  Serial.begin(9600);
  dht_sensor.begin(); 
}

void loop() {
  float humi  = dht_sensor.readHumidity();
  float temp = dht_sensor.readTemperature();

  if ( isnan(temp) || isnan(humi)) {
    Serial.println("Failed to read from sensor!");
  } else {
    Serial.print("Humidity: ");
    Serial.print(humi);
    Serial.print("%");

    Serial.print("  |  ");

    Serial.print("Temperature: ");
    Serial.print(temp);
    Serial.print("°C\n");
  }
  delay(1000);
}
