#!/usr/bin/env python
### run as 'sudo -E ./sensehat_wia.py

import os
from time import sleep
from wia import Wia
from sense_hat import SenseHat
sense = SenseHat()

wia = Wia()
wia.access_token = os.environ['MY_WIA_TOKEN']

while True:
    temperature=round(sense.get_temperature(),2)
    humidity=round(sense.get_humidity(), 2)
    pressure=round(sense.get_pressure(), 2)
    wia.Event.publish(name="temperature", data=temperature)
    wia.Event.publish(name="humidity", data=humidity)
    wia.Event.publish(name="pressure", data=pressure)
    sleep(30)
