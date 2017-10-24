# Bluetooth API

This is the bluetooth api that will host all hardware bluetooth interactions.

### Routes

**Scan Deviecs**

```sh
/bluetooth_scan/on
```
Turns on bluetooth and starts scanning for any bluetooth devices.
If the function finds a new device that is not in the database it will add it
```sh
/bluetooth_scan/off
```
Stops searching for bluetooth devices
  
  
  
  **Connect Devices**
  ```sh
/bluetooth/connect/<device_id>
```
Connects to a specific device
  
  
  **Disconnect devices**
  ```sh
/bluetooth/disconnect/<device_id>
```
Disconnects device
  
**Make discoverable / start server**

```sh
/bluetooth/server/up
```
Starts bluetooth server so devices can find and be able to connect to software
  
