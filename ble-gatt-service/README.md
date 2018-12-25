Adding Bluetooth Low Energy LED Matrix Gatt Server service for IoT

Software, Hardware
===================
* Raspberry Pi2B/Pi3B
* LightBlue Explorer Android App

OS setup
========

* Setup Bluetooth 5.50 prerequisites (system will reboot)

.. code-block:: bash

        ./configure_ble.py

Gatt Service
============
* Execute command to setup BLE GATT Service

.. code-block:: bash

        ./start_gatt.py

* Your PI is now BLE advertising and waiting for a device connections.

* Try restart BLE if you have issues.

.. code-block:: bash

        ./restart_ble.py


Testing
=======
Verified on-
- Rasbian/RaspberryPi 3B+, UART BT.
Issues on-
- Rasbian/RaspberryPi 2B+, USB BT (BLE advertising issues), SenseHat.
