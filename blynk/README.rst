Use Blynk Mobile App to control, collect, and analyize your devices.

Software, Hardware
===================
* Blynk app on Android or IoS
* Raspberry Pi2B/Pi3B / Node Blynk library
* Access tokens as OS environment variables

IoT Platform
============

https://www.blynk.cc/

OS setup
========

* Setup iot platform access tokens how you like. I use `~/.bash_profile` to manage as environment variables. Remember `sudo -E` for scripts needing elevated privledges.

.. code-block:: bash

    vi ~/.bash_profile
    ### My IoT Device Inventory
    export BLYNK_TOKEN_SENSEHAT="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    export BLYNK_TOKEN_RPI3BPLUS=""

    ### environment variables needed by iot-pi-stepping-stones ###
    export MY_BLYNK_TOKEN="${BLYNK_TOKEN_SENSEHAT}"

* Run script to setup each device (represented by subdir containing code)

.. code-block:: bash

    ./configure_blynk.py -d rpi2b
    ./configure_blynk.py -d sensehat/2vpin
    ./configure_blynk.py -d sensehat/3vpin
    ./configure_blynk.py -d sensehat/4vpin

.. image:: ./pics/npm-installed.png
   :scale: 10 %
   :alt: npm package installed

Simple Blynk App
=================
Use Blynk to control your device using a Virtual Pin.

* Start your on-device Blynk NodeJs service-

.. code-block:: bash

    sudo -E node ./rpi2b/index.js

* You should see output like the following-

.. image:: ./pics/blynk-ready.png
   :scale: 10 %
   :alt: BlynkApp output

* Interact with the device from your Blynk app (Android/iOS).

SenseHat Blynk App
==================

* Kill the previous NodeJs service.

.. code-block:: bash

    Ctrl+C

* Start your on-device Blynk NodeJs service for SenseHat-

.. code-block:: bash

    sudo -E node ./sensehat/2vpin/index.js

* The service "listens" for reads events on V1, and "sends"temperature to virtual pin V2.

* On BlynkApp, interact with the device.

Phone Sensors Blynk App
=======================
Blynk app can access phones sensors such as light, and accelerometer.

* In BlynkApp add a "Light Sensor" widget, output to V3, to measure light intensity (lux).

* kill the running node app.

.. code-block:: bash

    Ctrl+C

* Run the node app again.

.. code-block:: bash

    sudo -E node ./sensehat/2vpin/index.js

* Your RPi could perhaps display "too bright/dark" messages on the console depending on what threshold lux value triggers on/off behaviour.


Send temperature data to Thingspeak
====================================
BlynkApp Webhook widget can communicate with 3rd party services like ThingSpeak.

* Go to ThingSpeak.com and create new temperature channel.

* Go to BlynkApp and add "Webhook" from the widget box.

* Monitor V2 and send data to Thingspeak (see: https://docs.blynk.cc/#widgets-other-webhook)

.. image:: ./pics/blynk-webhooks.png
   :scale: 10 %
   :alt: npm package installed

* On your device kill the running NodeJs service.

.. code-block:: bash

    Ctrl+C

* Run node app again.

.. code-block:: bash

    sudo -E node ./sensehat/3vpin/index.js


Send GPS data to WiA
=====================
BlynkApp Webhook widget can communicate with 3rd party services like WIA.

* Go to BlynkApp and add "GPS Webhook" from widget box.

* Monitor V4 as illustrated.

.. image:: ./pics/blynk-gps-webhook.png
   :scale: 10 %
   :alt: GPS Streaming Webhook in Wia

* Ensure your WiA tokens are OS environ variables.

.. code-block:: bash

    vi ~/.bash_profile
    ### My IoT Device Inventory
    export WIA_TOKEN_SENSEHAT="d_sk_xxxxxxxxxxxxxxxxxxxxxxxpi"
    export WIA_TOKEN_RPI3BPLUS="d_sk_yyyyyyyyyyyyyyyyyyyyyyyy"
    export MY_WIA_TOKEN="${WIA_TOKEN_SENSEHAT}"

    ### environment variables needed by iot-pi-stepping-stones ###
    export MY_WIA_TOKEN="${WIA_TOKEN_SENSEHAT}"

* On your device kill the running NodeJs service.

.. code-block:: bash

    Ctrl+C

* Run node app again.

.. code-block:: bash

    sudo -E node ./sensehat/4vpin/index.js

* Go to wia.io and interact with the service.
