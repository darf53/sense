#!/bin/bash

temp=`python /home/pi/sense/temp.py`

curl -i "https://influx.effwd.be/write?db=bommel" --data-binary "temp,location=living value=$temp"
# echo "uploading temp data to influxdb - exit code:" $?
