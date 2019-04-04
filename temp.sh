#!/bin/bash

# script for reading a temp sensor on the RaspberryPI
# connect a sensor type DS18b20 

temp=`python /home/pi/sense/temp.py`

curl -i "https://influx.effwd.be/write?db=bommel" --data-binary "temp,location=living value=$temp"
# echo "uploading temp data to influxdb - exit code:" $?
