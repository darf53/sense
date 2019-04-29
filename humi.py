import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
pin = 17
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

def humidityIn():
    return(round(humidity,2))
    #return(humidity)

if __name__ == "__main__":
    print(humidityIn())
