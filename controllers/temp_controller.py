import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

def get_temp_string():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)

    # humidity = round(humidity, 2)
    temperature = round(temperature, 2)
    return "{:.2f}".format(temperature)

def get_temp_float():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
    return temperature
