#!/usr/bin/env python3

from influxdb import InfluxDBClient, SeriesHelper
from envirophat import light, weather, leds
import time

leds.off()

# InfluxDB connections settings
host = 'temporal.phontok.com'
port = 8086
user = 'tiwanon'
password = 'root'
dbname = 'tiwanon'
ssl = True

influx_client = InfluxDBClient(host, port, user, password, dbname, ssl)

class EnvironmentHelper(SeriesHelper):
  # Meta class stores time series helper configuration.
  class Meta:
    # The client should be an instance of InfluxDBClient.
    client = influx_client
    # The series name must be a string. Add dependent fields/tags in curly brackets.
    series_name = 'environment'
    # Defines all the fields in this time series.
    fields = ['temperature', 'light', 'pressure']
    # Defines all the tags for the series.
    tags = ['location', 'device']
    # Defines the number of data points to store prior to writing on the wire.
    bulk_size = 6
    # autocommit must be set to True when using bulk_size
    autocommit = True

try:
  while True:
    lux = light.light()
    temp = weather.temperature()
    press = weather.pressure()
    EnvironmentHelper(temperature=temp, light=lux, pressure=press, location='lounge', device='pi0')
    time.sleep(10)

finally:
  EnvironmentHelper.commit()

