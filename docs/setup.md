# Mini-IoT setup guide

## Start MQTT

triton-docker run -d -p 1883 -p 9001 --name iot-mqtt eclipse-mosquitto

## Get public IP

triton instance get -j iot-mqtt | json ips[1]

## Start InfluxDB

triton-docker run -d -p 8086 --name iot-influxdb influxdb

## Get public IP

triton instance get -j iot-influxdb | json ips[1]
