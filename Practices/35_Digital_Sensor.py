import random
import threading
import time

import timer
from lxml.html.builder import INPUT


class DataProvider:
    def __init__(self):
        self.temp_sensor = Sensor()
        self.humidity_sensor = Sensor()
        self.flow_sensor = Sensor()

        self.temp_value = 0
        self.humidity_value = 0
        self.flow_value = 0

        th = threading.Thread(target = self.read_senors, daemon=True)
        th.start()

    def read_senors(self):
        print("Starting read sensor value with 1 second interval..")
        while True:
            tick_start = time.monotonic()

            self.get_temp_value()
            self.get_humidity_value()
            self.get_flow_value()

            elapsed = time.monotonic() - tick_start
            if elapsed > 1 : print(f"Exceeded the maximum read time! {elapsed}")
            else:
                print(f"Reading finished within {elapsed} s")
                time.sleep(1 - elapsed)

    def get_temp_value(self):
        if (self.temp_sensor is not None):
            self.temp_value = self.temp_sensor.get_value()

    def get_humidity_value(self):
        if (self.humidity_sensor is not None):
            self.humidity_value = self.humidity_sensor.get_value()

    def get_flow_value(self):
        if (self.flow_sensor is not None):
            self.flow_value = self.flow_sensor.get_value()

class Sensor:
    def get_value(self):
        value = random.randint(1, 100)
        time.sleep(random.randint(1, 30)/100) # random delay 0.1s ~ 1s
        print("Getting random sensor value {}..".format(value))
        return value

if __name__ == "__main__":
    data_provider = DataProvider()
    print("waiting for some command..")
    input()