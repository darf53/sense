Crontab update:
*/5 * * * * root /home/pi/sense/temp.sh
*/5 * * * * root /home/pi/sense/humi.sh


Crontab for user:
*/5 * * * * python3 /home/pi/sense/upload.py


Attaching dust sensor SDS11
used this page: https://hackernoon.com/how-to-measure-particulate-matter-with-a-raspberry-pi-75faa470ec35
GIT: https://github.com/zefanja/aqi
