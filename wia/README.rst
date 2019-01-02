Use WIA to collect and analyize data from your devices.

Software, Hardware
===================
* Raspberry Pi2B/Pi3B
* Pi SenseHAT
* Pi Camera is optional
* Access tokens as OS environment variables

IoT Platform
============

https://wia.io

OS setup
========

* Clone this repo.

.. code-block:: bash
    
    git clone https://github.com/noelmcloughlin/iot-edge-stepping-stones.git
    cd iot-edge-stepping-stones

* Setup iot platform access tokens how you like. I use `~/.bash_profile` to manage as environment variables. Remember `sudo -E` for scripts needing elevated privledges.

.. code-block:: bash

    vi ~/.bash_profile
    ### My IoT Device Inventory
    export WIA_TOKEN_SENSEHAT="d_sk_xxxxxxxxxxxxxxxxxxxxxxxpi"
    export WIA_TOKEN_RPI3BPLUS="d_sk_yyyyyyyyyyyyyyyyyyyyyyyy"
    export MY_WIA_TOKEN="${WIA_TOKEN_SENSEHAT}"

    ### environment variables needed ##
    export MY_WIA_TOKEN="${WIA_TOKEN_SENSEHAT}"

* Execute command to setup the software

.. code-block:: bash

        ./wia/configure_wia.py -a install

Publish weather data
====================
The SenseHAT has temperature, pressure, and humidity sensors useful as Weather station.

* Open Terminal #1 and run script to publish weather events to WIA-

.. code-block:: bash

    sudo -E ./configure_wia.py -s weather

* WIA consumes your Pi SenseHat temp/humidity/pressure data. 

.. image:: ./pics/wia-dash.png
   :scale: 25 %
   :alt: WIA weather station dashboard

Publish Photo data
==================
Use Wia events, commands. and flows to control SenseHat from facial expressions.

* In the WIA dashboard, add two commands named 'happy-face' and 'sad-face'.

* Publish photo events from your Raspiberry Pi Camera-

.. code-block:: bash

    python3 ./camera/local_snap.py

* Publish photo events from your laptop-

.. code-block:: bash

    python3 ./camera/remote_snap.py

* WIA consumes your RPi Camera data.

.. image:: ./pics/wia-photo-event.png
   :scale: 25 %
   :alt: WIA photo events

