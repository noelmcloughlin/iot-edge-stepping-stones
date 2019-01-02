Use ThingSpeak to collect and write temperature data from your device.

Software, Hardware
===================
* Raspberry Pi2B/Pi3B
* SenseHAT
* Access tokens as OS environment variables

IoT Platform
============

https://thingspeak.com

OS setup
========

* Clone this repo.

.. code-block:: bash
    
    git clone https://github.com/noelmcloughlin/iot-edge-stepping-stones.git
    cd iot-edge-stepping-stones

* Execute command to setup required software

* Setup iot platform access tokens how you like. I use `~/.bash_profile` to manage as environment variables. Remember `sudo -E` for scripts needing elevated privledges.

.. code-block:: bash

    vi ~/.bash_profile
    ### My IoT Device Inventory
    export THINGSPEAK_RTOKEN_SENSEHAT="wwwwwwwwwwwwwww"
    export THINGSPEAK_WTOKEN_SENSEHAT="xxxxxxxxxxxxxxx"
    export THINGSPEAK_RTOKEN_RPI3BPLUS="yyyyyyyyyyyyyy"
    export THINGSPEAK_WTOKEN_RPI3BPLUS="zzzzzzzzzzzzzz"

    ### environment variables needed ##
    export MY_THINGSPEAK_RTOKEN="${THINGSPEAK_RTOKEN_SENSEHAT}"
    export MY_THINGSPEAK_WTOKEN="${THINGSPEAK_WTOKEN_SENSEHAT}"

Publish weather data
====================
The SenseHAT has temp, pressure, and humidity sensors useful for Weather station.

* Open Terminal #1 and run script to publish events to your Thingspeak channel-

.. code-block:: bash

    sudo -E ./thingspeak/configure_thingspeak.py -s temp

* Thingspeak consumes your Pi SenseHat temp/humidity/pressure data. 

.. image:: ./pics/thingspeak-dash.png
   :scale: 25 %
   :alt: ThingSpeak weather station dashboard

* Thingspeak has integrations with various third-party services too-

.. image:: ./pics/thingspeak-twitter.png
   :scale: 25 %
   :alt: ThingSpeak twitter integration

