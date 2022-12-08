# ECE 422 Term Project
Memebers : Sean Flebbe, Sarah Arajuo, Oluwaseun Abiona, Stuart Ward
## Summary
The purpose of this project is to create a GUI based Bluetooth Utility to show nearby Bluetooth devices. We will also show their Connections, Central/Peripheral types, mac address, etc...

Bluetooth API -> Scan Nearby Devices -> Save to local/temp json file -> Display Repository of Saved Scans

[https://www.ampedrftech.com/datasheets/cod_definition.pdf]

## Setup

First step is clone the repository,

    git clone https://github.com/Sycther/bluetooth-util
    cd bluetooth-util

Setup a virtual Python enviornment

*Optional but highly recommended*

    python -m virtualenv venv

    (windows) 
    venv/Scripts/activate

    (linux)
    source /venv/bin/activate

install all the dependencies

    python -m pip install -r requirements.txt

## Run

    python ble_gui

## Requirements
- Python >= 3.9

### Libraries Used
- PySide6
- Bleak
- Qasync

## Bugs
Your IDE might give an error while importing the some libraries, otherwise the library works.... somehow...
  
### Deliverables
- [x] Asyncronous Bluetooth Scanner
  - [x] Save devices to list
  - [x] Json Save Files
  - [x] Interpret & Display Device Class
    - [x] CIC (Company ID)
    - [ ] COD (Class Of Device)
  - [ ] Detect Connected Devices
- [x] GUI
  - [x] Design Layout
  - [x] Bluetooth scanning parralell to gui