from bleak import BleakScanner, BLEDevice
import pickle
from datetime import datetime
import os

async def scan_now() -> BLEDevice:
    dt = datetime.now().strftime("%m-%d-%y - %H:%M:%S")
    devices = await BleakScanner.discover()
    
    with open('saves/{}.pkl'.format(dt), 'wb') as f:
        pickle.dump(devices, f, -1)
    return devices


def get_previous_scans() -> list:
    dt: list = []
    for obj in os.scandir('saves'):
        dt.append(obj)
    return dt