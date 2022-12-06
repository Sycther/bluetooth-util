import asyncio
import BLEUtil
import ble_dict
import datetime
import json
from bleak import BLEDevice

from GUI import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow, QListWidgetItem

import functools, sys
import qasync
from qasync import asyncSlot, QApplication

### Constants
WIN_WIDTH = 950
WIN_HEIGHT = 600


class BLElistItem(QListWidgetItem):

    def __init__(self, device = None):
        super().__init__()
        self.address = device.address
        self.name = device.name
        #self.details:str = device.details
        self.rssi = device.rssi
        self.metadata = device.metadata

        self.setSelfText()
    
    def parse_device_data(self) -> str:
        out = ""

        try:
            data = self.metadata['manufacturer_data'].popitem()
        except KeyError:
            return "No Data Given"
        cic = data[0]
        cod = data[1]
        try:
            out = ble_dict.SIG_MAP[cic]
        except KeyError:
            return "Unrecognized SIG"

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
        elif self.rssi < -100:
            return "No signal"

    def setSelfText(self):
        self.setText(self.__str__())

    def __eq__(self, other) -> bool:
        return self.address == other.address

    def __str__(self) -> str:
        return "{}\n - {}\n - {}\n-{}".format(self.name, self.address,self.parse_device_data(), self.parse_rssi())

class TestWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(TestWindow, self).__init__()
        self.setupUi(self)
        self.scanner = BLEUtil.Scanner(self.callback)
        self.deviceList : BLElistItem = []

    def callback(self, device, advertisment_data):
        if not device in self.deviceList:
            #out = "{}\n - {}\n - {}\n - {}\n - {}".format(device.name, device.address, self.scanner.parse_device_data(device), device.metadata,advertisment_data)
            ## Create
            dev = BLElistItem(device)
            self.list.addItem(dev)
            self.deviceList.append(dev)
        else :
            #Update
            #index = self.deviceList.index(device)
            #self.deviceList[index].metadata = device.metadata
            #self.deviceList[index].setSelfText()
            pass

    @asyncSlot()
    async def saveNow(self):
        dt = datetime.datetime.now()
        dumps = []
        for device in self.deviceList:
            dumps.append(device.__dict__)
        with open("saves/{} - {}.{}.{}.json".format(dt.date(), dt.hour, dt.minute, dt.second), 'w') as f:
            json.dump(dumps, f, indent=4)
            
    
    @asyncSlot()
    async def scanNow(self):
        print("Scanning")
        self.list.clear()
        self.deviceList = []
        try:
            await self.scanner.scan(10)
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
    #except asyncio.exceptions.CancelledError:
    except Exception as e:
        print(e)
        sys.exit(0)