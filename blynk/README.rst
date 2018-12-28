Use Blynk Mobile App to control, collect, and analyize your devices.

Software, Hardware
===================
* Blynk app on Android or IoS
* Raspberry Pi2B/Pi3B
* Access tokens as OS environment variables

IoT Platform
============

https://www.blynk.cc/

OS setup
========

* Setup your iot platform access tokens how you like. This example uses `~/.bash_profile` to manage as environment variables. Remember to use `sudo -E` for scripts needing elevated privledges.

.. code-block:: bash

    vi ~/.bash_profile
    ### My IoT Device Inventory
    export BLYNK_TOKEN_SENSEHAT="9a1603382ab7432ea3b3b23980442f5b"
    export BLYNK_TOKEN_RPI3BPLUS=""
    export MY_BLYNK_TOKEN="${BLYNK_TOKEN_SENSEHAT}"

    ### environment variables needed by iot-pi-stepping-stones ###
    export MY_BLYNK_TOKEN="${BLYNK_TOKEN_SENSEHAT}"

* Execute command to setup the software

.. code-block:: bash

        ./wia/configure_blynk.py

Publish weather data
====================
The SenseHAT has temperature, pressure, and humidity sensors suitable for a Weather station.

* Open Terminal #1 and run script to publish events to your Blynk channel-

.. code-block:: bash

    sudo -E ./blynk/sensehat.py

* Blynk consumes your Pi SenseHat temp/humidity/pressure data. 

.. image:: ./pics/blynk-dash.png
   :scale: 25 %
   :alt: Blynk weather station dashboard

* Blynk has integrations with various third-party services too-

.. image:: ./pics/blynk-twitter.png
   :scale: 25 %
   :alt: Blynk twitter integration

