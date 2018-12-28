Use Wia.io to collect and display data from the RPi

Software, Hardware
===================
* Raspberry Pi2B/Pi3B
* SenseHAT
* Optionally a Pi Camera
* Access Token as environment variables

IoT Platform
============

https://wia.io

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

        ./wia/configure_wia.py

Publish weather data
====================
The SenseHAT has temperature, pressure, and humidity sensors useful as Weather station.

* Open Terminal #1 and run script to publish events to WIA-

.. code-block:: bash

    sudo -E ./wia/sensehat.py

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

    curl -Ls -O https://raw.githubusercontent.com/noelmcloughlin/iot-pi-stepping-stones/master/wia/camera/local_snap.py
    python3 ./local_snap.py

* Publish photo events from your laptop-

.. code-block:: bash

    curl -Ls -O https://raw.githubusercontent.com/noelmcloughlin/iot-pi-stepping-stones/master/wia/camera/remote_snap.py
    python3 ./remote_snap.py

* WIA consumes your RPi Camera data.

.. image:: ./pics/wia-photo-event.png
   :scale: 25 %
   :alt: WIA photo events

