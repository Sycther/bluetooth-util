import asyncio
import BLEUtil as BLEUtil
import ble_dict as ble_dict
import datetime
import json
from bleak import BLEDevice
from typing import Dict

from GUI import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow, QListWidgetItem

import functools, sys
import qasync
from qasync import asyncSlot, QApplication

### Constants
WIN_WIDTH = 950
WIN_HEIGHT = 600


class BLElistItem(QListWidgetItem):

    def __init__(self, device = None, adv=None):
        super().__init__()
        self.address = device.address
        self.name = device.name
        #self.details:str = device.details
        self.rssi = device.rssi
        self.update_adv(adv)

        self.setSelfText()
    
    def update_adv(self, adv):

        if(adv.service_uuids):
            uuids = adv.service_uuids
        else:
            uuids = []
        
        if(adv.manufacturer_data):
            data = adv.manufacturer_data.popitem()
            cic = data[0]
            data = data[1]
        else:
            cic = None
            data = None

        self.metadata = {
            "uuids":uuids,
            "manufacturer_data": {
                "cic": cic,
                "data": str(data)
            }
        }

    def parse_cic(self):
        if(self.metadata["manufacturer_data"]["cic"]):
            try:
                out = ble_dict.SIG_MAP[self.metadata["manufacturer_data"]["cic"]]
            except KeyError:
                return "Unrecognized SIG - {}".format(self.metadata["manufacturer_data"]["cic"])
        else:
            return "No SIG Given"
        return out

    def parse_rssi(self):
        if self.rssi >-30:
            return "Very Good Signal Strength"
        elif self.rssi > -50:
            return "Decent Signal Strength"
        elif self.rssi > -70:
            return "Fair Signal Strength"
        elif self.rssi > -100:
            return "Poor Signal Strength"
        elif self.rssi <= -100:
            return "No signal"

    def setSelfText(self):
        self.setText(self.__str__())

    def __eq__(self, other) -> bool:
        return self.address == other.address

    def __str__(self) -> str:
        return "{}\n     - {}\n     - {}\n     - {}".format(self.name, self.address,self.parse_cic(), self.parse_rssi())

class TestWindow(QMainWindow, Ui_MainWindow):

    deviceList: Dict[str, BLElistItem] 
    """
    List of Seen Devices in BLE List Item
    """


    def __init__(self):
        super(TestWindow, self).__init__()
        self.setupUi(self)
        self.scanner = BLEUtil.Scanner(self.callback)
        self.deviceList = {}

    def callback(self, device, advertisment_data):
        if not device.address in self.deviceList:
            # Create
            dev = BLElistItem(device, advertisment_data)
            self.list.addItem(dev)
            self.deviceList[dev.address] = dev
        else :
            #print("Updating - {}\n     - {}".format(device, advertisment_data))
            self.deviceList[device.address].update_adv(advertisment_data)
            pass

    @asyncSlot()
    async def updateFormData(self, bleItem: BLElistItem):
        if(bleItem.name != None):
            self.nameTxt.setText(bleItem.name)
        else:
            self.nameTxt.setText("None")
        self.addrTxt.setText(bleItem.address)
        self.detailsTxt.setText("UUIDS: {}\nRSSI: {}\nSIG: {}\nDATA: {}".format(bleItem.metadata["uuids"],bleItem.rssi,bleItem.metadata["manufacturer_data"]["cic"],bleItem.metadata["manufacturer_data"]["data"]))

    @asyncSlot()
    async def saveNow(self):
        dt = datetime.datetime.now()
        dumps = []
        for item in self.deviceList.values():
            try:
                dumps.append(item.__dict__)
            except Exception as e:
                print(e)
        with open("saves/{} - {}.{}.{}.json".format(dt.date(), dt.hour, dt.minute, dt.second), 'w') as f:
            json.dump(dumps, f, indent=4)
            
    
    @asyncSlot()
    async def scanNow(self):
        print("Scanning")
        self.list.clear()
        self.deviceList.clear()
        try:
            await self.scanner.scan_ble(5)
            print("total: ", len(self.deviceList))
        except Exception as e:
            print(e)
        else :
            if len(self.scanner.discovered_devices) == 0:
                print("Nothing")

async def main():
    def close_future(future, loop):
        loop.call_later(10, future.cancel)
        future.cancel()

    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    app = QApplication.instance()

    if hasattr(app, "aboutToQuit"):
        getattr(app, "aboutToQuit").connect(
            functools.partial(close_future, future, loop)
        )

    mw = TestWindow()
    mw.show()
    
    app.exec()

    await future
    return True

if __name__ == "__main__":
    try:
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        sys.exit(0)