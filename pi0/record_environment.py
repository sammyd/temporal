from influxdb import InfluxDBClient
from envirophat import light, weather, leds
import datetime


leds.off()
lux = light.light()
temp = weather.temperature()
press = weather.pressure()
timestamp = datetime.datetime.now().isoformat()

host = 'temporal.phontok.com'
post = 8086
user = 'tiwanon'
password = 'root'
dbname = 'tiwanon'
json_body = [
  {
    "measurement": "environment",
    "tags": {
      "location": "lounge",
      "device": "pi0"
    },
    "time": timestamp,
    "fields": {
      "temperature": temp,
      "light": lux,
      "pressure": press
    }
  }
]

client = InfluxDBClient(host, port, user, password, dbname)

print("Write points: {0}".format(json_body))
client.write_points(json_body)

