#!/bin/bash

# script for reading a humidity sensor on the RaspberryPI
# connect a sensor type DTH22

humi=`python /home/pi/sense/humi.py`

curl -i "https://influx.effwd.be/write?db=bommel" --data-binary "humidity,location=living value=$humi"
# echo "uploading temp data to influxdb - exit code:" $?
