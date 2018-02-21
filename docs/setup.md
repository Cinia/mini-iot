# Mini-IoT setup guide

## Start MQTT

`triton-docker run -d -p 1883 -p 9001 --name iot-mqtt eclipse-mosquitto`

## Start InfluxDB

`triton-docker run -d -p 8086 --name iot-influxdb influxdb`

## Start MQTT -> Influx router

`triton-docker run -d --name=mqtt-influxdb-bridge -e BROKER=tcp://BROKER_IP:1883 -e DB=http://INFLUX_IP:8086 reap/mqtt-influxdb-bridge`

## Start Grafana

`triton-docker run -d --name=grafana -p 3000:3000 grafana/grafana`
