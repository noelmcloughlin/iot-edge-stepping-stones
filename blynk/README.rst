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

* Setup your iot platform access tokens how you like. This example uses `~/.bash_profile` to manage as environment variables. Remember to use `sudo -E` for scripts needing elevated privledges.

.. code-block:: bash

    vi ~/.bash_profile
    ### My IoT Device Inventory
    export BLYNK_TOKEN_SENSEHAT="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    export BLYNK_TOKEN_RPI3BPLUS=""

    ### environment variables needed by iot-pi-stepping-stones ###
    export MY_BLYNK_TOKEN="${BLYNK_TOKEN_SENSEHAT}"

* Execute command to setup the software

.. code-block:: bash

    ./configure_blynk.py

Create a Blynk App
==================
You can use Blynk to control your device using a Virtual Pin.

* Execute command to start your on-device Blynk NodeJs service.

.. code-block:: bash

    node ./rpi2b/index.js

* The Blynk App can now control your device using this Virtual Pin.
