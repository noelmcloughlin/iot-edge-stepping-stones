# Sample Use case: a redundant Weather Station solution using HTTP and MQTT.

Use MQTT to publish/subscribe to/from sensor data (humidity, temp, pressure) in a flexible manner.

.. image:: ./pics/mqtt-publish-subscribe.png
   :scale: 25 %
   :alt: high level architecture

Sample software &Hardware
===========================
* Raspberry Pi2B+ with Environmental Board (i.e. Sense HAT)
* Raspberry Pi3B+ with Environmental Board (i.e. BME680)
* Cloud MQTT Brokers
* TinyDB

Cloud MQTT broker
=================
Optionally select your cloud mqtt broker-

* mqtt://iot.eclipse.org:1883
* mqtt://broker.hivemq.com:1883
* mqtt://test.mosquitto.org:1883
* https://www.cloudmqtt.com/

Setup software
=================

* Clone this repo.

.. code-block:: bash

    git clone https://github.com/noelmcloughlin/iot-edge-stepping-stones.git
    cd iot-edge-stepping-stones

* Execute command to setup required software

.. code-block:: bash

        ./mqtt/mqtt.py -a install

Publish weather data
====================
The SenseHAT has temperature, pressure, and humidity sensors useful as Weather station. Lets starrt publishing data to a Cloud MQTT broker. The publisher defaults to 'sense_hat' board but 'bme680' is supported too.

* On hostA (default 'sense_hat' board), publish mqtt weather messages-

.. code-block:: bash

    sudo ./mqtt.py -a publish -u mqtt://iot.eclipse.org:1883/NOELWEATHER_A
    Connected to iot.eclipse.org:1883/NOELWEATHER_A Result: 0
    {'h': 49.61815643310547, 't': 29.33, 'p': 1043.434326171875}
    {'h': 49.139583587646484, 't': 29.33, 'p': 1043.46826171875}

* On hostB, subscribe to same mqtt weather messages-

.. code-block:: bash

    ./mqtt.py -a subscribe -u mqtt://iot.eclipse.org:1883/NOELWEATHER_A
    Connected to iot.eclipse.org:1883/NOELWEATHER_A Result: 0
    topic:NOELWEATHER_A/h, val:48.9634399414
    topic:NOELWEATHER_A/t, val:29.42
    topic:NOELWEATHER_A/p, val:1043.48852539

* On hostB, persist the same mqtt weather messages to TinyDB by setting flag-

.. code-block:: bash

    sudo ./mqtt.py -a subscribe -u mqtt://iot.eclipse.org:1883/NOELWEATHER_A --persist True
    Connected to iot.eclipse.org:1883/NOELWEATHER_A Result: 0
    Insert DB: NOELWEATHER_A/h, val:48.7972717285
    Insert DB: NOELWEATHER_A/t, val:29.31
    Insert DB: NOELWEATHER_A/p, val:1043.44677734

* Lets push the solution harder by using second ('bme680') board and MQTT broker...

* Open New Terminal on hostB and publish to/from different broker/board-

.. code-block:: bash

    ./mqtt.py -a publish -u mqtt://test.mosquitto.org:1883/NOELWEATHER_B --board bme680
    Connected to test.mosquitto.org:1883/NOELWEATHER_B Result: 0
    topic:NOELWEATHER_B/h, val:48.9634399414
    topic:NOELWEATHER_B/t, val:29.42
    topic:NOELWEATHER_B/p, val:1043.48852539

* Back on HostA, subscribe to the new channel and persist data too-

.. code-block:: bash


    sudo ./mqtt.py -a subscribe -u mqtt://test.mosquitto.org:1883/NOELWEATHER_B --persist True
    Connected to test.mosquitto.org:1883/NOELWEATHER_B Result: 0
    Insert DB: NOELWEATHER_B/h, val:48.7972717285
    Insert DB: NOELWEATHER_B/t, val:29.31
    Insert DB: NOELWEATHER_B/p, val:1043.44677734


* This illustrates a working MQTT publisher/subscriber redundant weather station solution.

Simple Analytics
================
Use TinyDB python api to extract simple statistics from the generated 'db.json' files-

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

