#####################################
# Basic MQTT Subscriber utilty class
#####################################

import paho.mqtt.client as mqtt_c
import json
from tinydb import TinyDB, Query

class MySubscriber():
    """ MQTT Subscriber class with event callbacks """

    def __init__(self, controller, url, dbengine=None):
        """ Initialize the mqtt subscriber.
            Setup the mqtt client, event callbacks.
            Then establish the connection.
        """

        self.base_topic = url.path[1:]
        self.url = url
        if dbengine and dbengine == 'tinydb':
            self.db = TinyDB('db.json')
        self.dbengine = dbengine
        self.topics = []
        self.mqttc = mqtt_c.Client()
        self.mqttc.on_message = self.on_message
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_subscribe = self.on_subscribe
        controller.connect(self.mqttc, url)

    def subscribe(self, topics=None):
        """ Subscribe, with QoS level 0 """
        for topic in topics:
            self.mqttc.subscribe(self.base_topic+"/%s" % topic, 0)
            self.topics.append(topic)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to %s%s Result: %s" % (self.url.netloc, self.url.path, str(rc)))

    def on_message(self, client, obj, msg):
        """ Display or Persist received message """
        if not self.dbengine:
            print("Topic:"+msg.topic + ",Payload:" + str(msg.payload))
        else:
            print("Insering into DB: "+msg.payload)
            msg_json=json.loads(msg.payload)
            print(msg_json)
            self.db.insert(msg_json)

    def on_subscribe(self, client, obj, mid, qos):
        print("Subscribed to %s%s  QOS: %s" % (self.url.netloc, self.url.path, str(qos)))

    def get_records_by_key(self, item_key='t'):
        """ Get DB records (only supports TinyDB) """
        records=""
        if self.dbengine:
            for rec in self.db:
                if str(item_key) in record:
                    records+= str(float(rec[str(item_key)]))
        return records

    def get_min(self, key='t'):
        """ Get minimum value by key """
        if self.dbengine:
            records = self.get_records_by_key(key)
            return min(records)
        return None

    def get_max(self, key='t'):
        """ Get maximum value by key """
        if self.dbengine:
            records = self.get_records_by_key(key)
            return max(records)
        return None

    def get_mean(self, key='t'):
        """ Get mean value by key """
        if self.dbengine:
            records = self.get_records_by_key(key)
            return sum(records)/len(records)
        return None

    def records(self, start, end):
        """ Get records by start/end (TinyDB only) """
        if self.dbengine:
            records = Query()
            return db.search((records.timestamp >= start) & (records.timestamp <= end))
        return None
