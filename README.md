# iot-ble-gatt-server
Adding Bluetooth Low Energy LED Matrix Gatt Server service for IoT

Instructions
============

* Clone this repo

* Execute command to setup Bluetooth 5.50 prerequisites (system reboot)

.. code-block:: bash

        ./gatt-server/configure_ble_gatt_service.py

* Execute command to setup BLE GATT Service

.. code-block:: bash

        ./gatt-server/configure_ble_gatt_service.py

* Your PI is now BLE advertising and waiting for a device connections.

Testing
=======

Verified with LightBlue Explorer Android App on-
- Rasbian on RaspberryPi 2B+, USB BT (BLE advertising issues), SenseHat.
- Rasbian on RaspberryPi 3B+, UART BT.

For technical nuance reasons the SenseHat variant script is untested. Later.
