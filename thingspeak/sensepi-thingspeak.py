#!/usr/bin/env python

import urllib2
import json
import time
import os
from sense_hat import SenseHat

sense = SenseHat()
baseURL='https://api.thingspeak.com/update?api_key=%s' % os.environ['MY_THINGSPEAK_WTOKEN']

def writeData(temp):
    ## Sending data to thingspeak
    conn = urllib2.urlopen(baseURL + '&field1=%s' % (temp))
    print(conn.read)
    conn.close()

while True:
    temp=round(sense.get_temperature(), 2)
    writeData(temp)
    sense.show_message(str(temp))
    time.sleep(60)

