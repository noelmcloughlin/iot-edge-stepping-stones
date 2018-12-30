# Use HTTP and MQTT to connect a device

Make RaspberryPi  sense and publish temp, pressure, and humidity data, to a MQTT broker. 

.. image:: ./pics/mqtt-publish-subscribe.png
   :scale: 25 %
   :alt: high level architecture

Software, Hardware
===================
* Raspberry Pi2B/Pi3B
* SenseHAT
* Cloud MQTT Broker
* TinyDB

Cloud MQTT broker
=================
Optionally select your cloud mqtt broker-

mqtt://iot.eclipse.org:1883
mqtt://broker.hivemq.com:1883
mqtt://test.mosquitto.org:1883
https://www.cloudmqtt.com/

Setup software
=================

* Execute command to setup the software

.. code-block:: bash

        ./mqtt/configure_mqtt.py

Publish weather data
====================
The SenseHAT has temperature, pressure, and humidity sensors useful as Weather station.

* Open Terminal #1 and run mqtt broker publisher script-

.. code-block:: bash

    ./mqtt/client_pub_multi.py mqtt://iot.eclipse.org:1883/WEATHER/home

* Your RPi publishes temp/humidity/pressure timestamped messages to your cloud MQTT broker.

.. code-block:: bash

    mqtt://iot.eclipse.org:1883/WEATHER/home
    Message ID: 1
    Connection Result: 0     #see https://pypi.org/project/paho-mqtt/#callbacks
    Message ID: 2

subscribe to weather data
=========================
* Open Terminal #2 on (local or remote) host, and run mqtt broker subscriber script-

.. code-block:: bash

    ./mqtt/client_sub.py mqtt://iot.eclipse.org:1883/WEATHER/home

* Your Pi is now subscribed to temp, humid, and pressure topics from the cloud MQTT broker.

.. code-block:: bash

    Connection Result: 0
    Subscribed,  QOS granted: (0,)
    Topic:WEATHER/home/t,Payload:{"timestamp": 1545615738.727764, "t": 30.23}
    Topic:WEATHER/home/h,Payload:{"timestamp": 1545615738.728046, "h": 46.563934326171875}
    Topic:WEATHER/home/p,Payload:{"p": 1024.540771484375, "timestamp": 1545615738.728198}
    Topic:WEATHER/home/t,Payload:{"timestamp": 1545615753.758816, "t": 30.27}
    Topic:WEATHER/home/h,Payload:{"timestamp": 1545615753.759097, "h": 46.33129119873047}
    Topic:WEATHER/home/p,Payload:{"p": 1024.53515625, "timestamp": 1545615753.759253}

* This illustrates a working MQTT publisher/subscriber weather station solution.

Persist weather data
====================
* Stop the subscriber by entering ctrl+c on your Terminal #2..

* In same terminal run mqtt broker subscriber and persist script-

.. code-block:: bash

        ./mqtt/persist_sub.py mqtt://iot.eclipse.org:1883/WEATHER/home

* Your Pi is now persisting temp, humid, and pressure data from the cloud MQTT broker.

.. code-block:: bash

        Connection Result: 0
        Subscribed,  QOS granted: (0,)
        Subscribed,  QOS granted: (0,)
        Subscribed,  QOS granted: (0,)
        Insering into DB: {"timestamp": 1545617005.797151, "t": 30.28}
        Insering into DB: {"h": 46.22826385498047, "timestamp": 1545617005.797439}
        Insering into DB: {"p": 1024.527587890625, "timestamp": 1545617005.797592}

Simple Analytics
================
You can use TinyDB python api to extract simple statistics-

.. code-block:: bash

        python
        >>> from tinydb import TinyDB, Query
        >>> db = TinyDB('db.json')
        >>> for item in db:
        >>>    print(item)
        {u'timestamp': 1541453440.878712, u'temperature': 34.67}
        {u'timestamp': 1541453455.783444, u'temperature': 34.5}
        {u'timestamp': 1541453470.80211, u'temperature': 34.54}
        >>> q = Query()
        >>> db.search(q.temperature < 33.95)
        [{u'temperature': 33.93},]
        >>> exit()

Weather Station Web API
=======================
* Start a web service on port 500 as follows-

.. code-block:: bash

        FLASK_APP=hello.py
        python temp_api.py

* Get various temperature statistics

.. code-block:: bash

       curl http://127.0.0.1:5000/sensehat/temp
       curl http://127.0.0.1:5000/sensehat/temp/min
       curl http://127.0.0.1:5000/sensehat/temp/mean
       curl http://127.0.0.1:5000/sensehat/temp/max

* Control the LED array (light) on the SenseHat-

.. code-block:: bash

       curl -X POST http://127.0.0.1:5000/sensehat/light?state=on
       curl -X POST http://127.0.0.1:5000/sensehat/light?state=off


Testing
=======
Verified on-
- Rasbian on RaspberryPi 2B+, and SenseHat.

