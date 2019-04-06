import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
pin = 17
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
print humidity
