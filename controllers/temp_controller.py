import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

def get_temp():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

    # humidity = round(humidity, 2)
    temperature = round(temperature, 2)
    return '{0:0.1f}*C'.format(temperature)