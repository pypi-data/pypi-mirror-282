import os

from machine import Pin, SoftI2C
import machine
import time
from umqtt.simple import MQTTClient
import json
import gc

cycle_time = 5

# SHT31 default I2C address
SHT31_I2C_ADDRESS = 0x44

# MQTT configuration
mqtt_server = os.environ['MQTT_SERVER']
mqtt_port = 30083
mqtt_topic = "sensor/temperature_humidity"

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)  # ESP32


def initialize_sht31():
    try:
        # Send the command to initialize the sensor
        i2c.writeto(SHT31_I2C_ADDRESS, bytes([0x30, 0xA2]))

        # Wait for the sensor to initialize (datasheet says at least 10ms)
        time.sleep_ms(20)

        return True
    except Exception as e:
        print("Error initializing sensor:", e)
        return False


def read_sht31():
    try:
        i2c.writeto(SHT31_I2C_ADDRESS, bytes([0x2C, 0x06]))

        time.sleep_ms(20)

        # Read 6 bytes of data (2 bytes temperature, 2 bytes humidity, 2 bytes CRC)
        data = i2c.readfrom(SHT31_I2C_ADDRESS, 6)

        temperature_celsius = -45 + (175 * ((data[0] << 8) + data[1]) / 65535.0)
        temperature_fahrenheit = (temperature_celsius * 9 / 5) + 32

        humidity = 100 * ((data[3] << 8) + data[4]) / 65535.0

        return temperature_fahrenheit, humidity
    except Exception as e:
        print("Error reading sensor:", e)
        return None, None


def main():
    gc.enable()

    last_temperature = None
    last_humidity = None

    while True:
        # gc.collect()
        if initialize_sht31():
            # Maybe add try/except here?
            temperature, humidity = read_sht31()
            if temperature is not None and humidity is not None:
                if (last_temperature is None or abs(temperature - last_temperature) <= 3) and \
                   (last_humidity is None or abs(humidity - last_humidity) <= 3):
                    last_temperature = temperature
                    last_humidity = humidity
                    uptime_seconds = time.time()
                    allocated_mem = gc.mem_alloc()
                    payload = {
                        "temperature": temperature,
                        "humidity": humidity,
                        "seconds_up": uptime_seconds,
                        "allocated_mem": allocated_mem
                    }

                    try:
                        client = MQTTClient("hostname", mqtt_server, keepalive=60)
                        client.connect()
                        client.publish(mqtt_topic, json.dumps(payload))
                        client.disconnect()
                        del client
                        print("Published to MQTT: Temperature: {:.2f} F, Humidity: {:.2f} %".format(temperature, humidity))

                    except Exception as e:
                        print("Error sending MQTT message:", e)

                else:
                    print("Discarded data: Temperature or humidity differs by more than 3 from the most recent value.")
                    machine.reset()

            else:
                print(f'Failed to read sensor. Retrying in {cycle_time} seconds.')

            time.sleep(cycle_time)


if __name__ == "__main__":
    main()
