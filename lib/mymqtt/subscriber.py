#####################################
# Basic MQTT Subscriber utilty class
#####################################

import paho.mqtt.client as mqtt_c
import json
from tinydb import TinyDB, Query

class MySubscriber():
    """ MQTT Subscriber class with event callbacks """

    def __init__(self, controller, url, qos=0, mydb=False, dbengine='tinydb'):
        """ Initialize the mqtt subscriber.
            Setup the mqtt client, event callbacks.
            Then establish the connection.
        """

        self.base_topic = url.path[1:]
        self.url = url
        self.qos = qos
        self.persist = False
        if mydb and dbengine == 'tinydb':
            self.db = TinyDB('db.json')
            self.persist = True
        self.topics = []
        self.mqttc = mqtt_c.Client()
        self.mqttc.on_message = self.on_message
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_subscribe = self.on_subscribe
        controller.connect(self.mqttc, url)

    def subscribe(self, topics=None):
        """ Subscribe, with QoS level 0 """
        for topic in topics:
            self.mqttc.subscribe(self.base_topic+"/%s" % topic, self.qos)
            self.topics.append(topic)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to %s%s Result: %s" % (self.url.netloc, self.url.path, str(rc)))

    def on_message(self, client, obj, msg):
        """ Display or Persist received message """

        if self.persist:
            print("Insert DB: " + msg.topic + ", val:" + str(msg.payload))
            t = ["topic", "val"]
            v = [msg.topic, str(msg.payload)]
            self.db.insert(dict(zip(t, v)))
        else:
            print("topic:" + msg.topic + ", val:" + str(msg.payload))


    def on_subscribe(self, client, obj, mid):
        print(mid)
        print("Subscribed to %s%s  QOS: %s" % (self.url.netloc, self.url.path, str(self.qos)))

    def get_records_by_key(self, item_key='t'):
        """ Get DB records (only supports TinyDB) """
        records=""
        if self.persist:
            for rec in self.db:
                if str(item_key) in record:
                    records+= str(float(rec[str(item_key)]))
        return records

    def get_min(self, key='t'):
        """ Get minimum value by key """
        if self.mydb:
            records = self.get_records_by_key(key)
            return min(records)
        return None

    def get_max(self, key='t'):
        """ Get maximum value by key """
        if self.persist:
            records = self.get_records_by_key(key)
            return max(records)
        return None

    def get_mean(self, key='t'):
        """ Get mean value by key """
        if self.persist:
            records = self.get_records_by_key(key)
            return sum(records)/len(records)
        return None

    def records(self, start, end):
        """ Get records by start/end (TinyDB only) """
        if self.persist:
            records = Query()
            return db.search((records.timestamp >= start) & (records.timestamp <= end))
        return None
