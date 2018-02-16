# Script for sending RPi SenseHat sensor data to MQTT-server

## Configuring

Set values to ```mini-iot-sender-config.ini``` and copy file next to python-script.

## To run on boot

Copy ```mini-iot-sender.service``` to ```/lib/systemd/system/mini-iot-sender.service```

Start service with

    sudo systemctl start mini-iot-sender.service

Set to start on boot

    sudo systemctl enable mini-iot-sender.service