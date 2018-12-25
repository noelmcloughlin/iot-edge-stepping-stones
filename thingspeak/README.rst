Use ThingSpeak to collect and analyize data from your devices.

Software, Hardware
===================
* Raspberry Pi2B/Pi3B
* SenseHAT
* Access Token as environment variables

IoT Platform
============

https://thingspeak.com

Setup software
=================

* Setup your IoT platform Access Tokens environment how you like. This example uses `~/.bash_profile` to manage the variables. As aside, use `sudo -E` when a script need elevated privledges.

.. code-block:: bash

    vi ~/.bash_profile
    ### My IoT Device Inventory
    export WIA_TOKEN_SENSEHAT="d_sk_xxxxxxxxxxxxxxxxxxxxxxxpi"
    export WIA_TOKEN_RPI3BPLUS="d_sk_yyyyyyyyyyyyyyyyyyyyyyyy"
    export MY_WIA_TOKEN="${WIA_TOKEN_SENSEHAT}"
    export THINGSPEAK_RTOKEN_SENSEHAT="wwwwwwwwwwwwwww"
    export THINGSPEAK_WTOKEN_SENSEHAT="xxxxxxxxxxxxxxx"
    export THINGSPEAK_RTOKEN_RPI3BPLUS="yyyyyyyyyyyyyy"
    export THINGSPEAK_WTOKEN_RPI3BPLUS="zzzzzzzzzzzzzz"

    ### environment variables needed by iot-pi-stepping-stones ###
    export MY_WIA_TOKEN="${WIA_TOKEN_SENSEHAT}"
    export MY_THINGSPEAK_RTOKEN="${THINGSPEAK_RTOKEN_SENSEHAT}"
    export MY_THINGSPEAK_WTOKEN="${THINGSPEAK_WTOKEN_SENSEHAT}"

* Execute command to setup the software

.. code-block:: bash

        ./wia/configure_thingspeak.py

Publish weather data
====================
The SenseHAT has temperature, pressure, and humidity sensors suitable for a Weather station.

* Open Terminal #1 and run script to publish events to your Thingspeak channel-

.. code-block:: bash

    sudo -E ./thingspeak/sensehat.py

* Thingspeak consumes your Pi SenseHat temp/humidity/pressure data. 

.. image:: ./pics/thingspeak-dash.png
   :scale: 25 %
   :alt: ThingSpeak weather station dashboard

* Thingspeak has integrations with various third-party services too-

.. image:: ./pics/thingspeak-twitter.png
   :scale: 25 %
   :alt: ThingSpeak twitter integration

