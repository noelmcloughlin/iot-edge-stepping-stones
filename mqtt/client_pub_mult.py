#!/usr/bin/env python

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import urlparse
import sys
import time
import json

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# parse mqtt url for connection details
url_str = sys.argv[1]
print(url_str)
url = urlparse.urlparse(url_str)
base_topic = url.path[1:]
auth=None
# Connect
if (url.username):
    auth = {'username':url.username, 'password':url.password}

# Publish a message
while True:
    temperature=round(sense.get_temperature(),2)
    humidity=sense.get_humidity()
    pressure=sense.get_pressure()

    #Create JSON strings
    temp_sensor=json.dumps({"t":temperature, "timestamp":time.time()}) 
    humidity_sensor=json.dumps({"h":humidity, "timestamp":time.time()}) 
    pressure_sensor=json.dumps({"p":pressure, "timestamp":time.time()}) 

    #Create array of MQTT messages
    temp_msg={'topic': base_topic +"/t", 'payload':temp_sensor}
    hum_msg={'topic':base_topic +"/h", 'payload':humidity_sensor}
    pres_msg={'topic':base_topic +"/p", 'payload':pressure_sensor}
    msgs=[temp_msg,hum_msg,pres_msg]

    #Publish array of messages
    publish.multiple(msgs, hostname=url.hostname, port=url.port, auth=auth)
    print("published")
    time.sleep(15)
