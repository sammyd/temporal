# Temporal

System to store data from our IoT devices.

Personal project—it's not meant to be useful.


# InfluxDB

To generate the SSL cert:

```sh
$ sudo openssl req -x509 -nodes -newkey rsa:2048 -keyout etc/ssl/influxdb/influxdb.key -out etc/ssl/influxdb/influxdb.crt -days <NUMBER_OF_DAYS>
```