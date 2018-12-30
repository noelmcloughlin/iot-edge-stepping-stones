#####################################
# Basic MQTT Subscriber class
#####################################

import paho.mqtt.client as mqtt_c
from tinydb import TinyDB, Query
import time, datetime
import json

sys.path.append('../lib')
import osutils as utils

class MySubscriber():
    """ MQTT Subscriber class with event callbacks """

    def __init__(self, controller, url, topics=[], dbengine=None):
        self.client = mqtt_c.Client()
        self.type = 'subscriber'
        self.base_topic = url.path[1:]
        self.topics = topics
        try:
            self.auth = controller.connect(self, url)
        except:
            print("\nCannot connect to %s" % url)
            exit(1)
        self.url = url
        if dbengine:
            if dbengine == 'tinydb':
                self.db = TinyDB('db.json')
            else:
                print("\nUnsupported dbengine")
                exit(1)
        self.dbengine = dbengine
        
        # Assign event callbacks
        self.client.on_message = on_message
        self.client.on_connect = on_connect
        self.client.on_subscribe = on_subscribe

    def subscribe(topics=None):
        #Subscribe, with QoS level 0
        if topics:
            for topic in topics:
                self.subscribe(self.base_topic+"/%s" % topic, 0)
                self.topics.append(topic)

    def on_connect(role, userdata, flags, rc):
        print("Connection Result: " + str(rc))

    def on_message(client, obj, msg):
        """ Display or Persist received message """
        if not self.dbengine:
            print("Topic:"+msg.topic + ",Payload:" + str(msg.payload))
        else:
            print("Insering into DB: "+msg.payload)
            msg_json=json.loads(msg.payload)
            print(msg_json)
            self.db.insert(msg_json)

    def on_subscribe(role, obj, mid, granted_qos):
        print("Subscribed,  QOS granted: "+ str(granted_qos))

    def get_records_by_key(item_key='t'):
        """ Get DB records (only supports TinyDB) """
        records=""
        if self.dbengine:
            for rec in self.db:
                if str(item_key) in record:
                    records+= str(float(rec[str(item_key)]))
        return records

    def get_min(key='t'):
        """ Get minimum value by key """
        if self.dbengine:
            records = self.get_records_by_key(key)
            return min(records)
        return None

    def get_max(key='t'):
        """ Get maximum value by key """
        if self.dbengine:
            records = self.get_records_by_key(key)
            return max(records)
        return None

    def get_mean(key='t'):
        """ Get mean value by key """
        if self.dbengine:
            records = self.get_records_by_key(key)
            return sum(records)/len(records)
        return None

    def records(start, end):
        """ Get records by start/end (TinyDB only) """
        if self.dbengine:
            records = Query()
            return db.search((records.timestamp >= start) & (records.timestamp <= end))
        return None
