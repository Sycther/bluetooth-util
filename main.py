import asyncio
from bleak import BleakScanner
import ble_util

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QMainWindow
)

import functools, sys
import qasync
from qasync import asyncSlot, asyncClose, QApplication


### Constants
WIN_WIDTH = 800
WIN_HEIGHT = 600

devices:list = []

class MainWidget(QWidget):

    def __init__(self, signal=None):
        super().__init__()

        self.setLayout(QVBoxLayout())

        label = QLabel("Bluetooth Utility")
        self.layout().addWidget(label)
        
        btn = QPushButton("Scan Now", self)
        btn.clicked.connect(self.scan_now)
        self.layout().addWidget(btn)

        self.output = QLabel("No Devices")
        self.layout().addWidget(self.output)


    def callback(self, device, ad_data):
        if not device in devices:
            devices.append(device)
            self.output.setText("\n".join("{}".format(i) for i in devices))

    @asyncSlot()
    async def scan_now(self):
        self.output.setText("Devices Found: ")

        devices.clear()

        try:
            async with BleakScanner(self.callback) as scanner:
                await asyncio.sleep(10)
        except Exception as e:
            self.output.setText(e)
        else :
            if len(devices) == 0:
                self.output.setText("No Devices Found")

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

    mw = MainWidget()
    mw.show()

    await future
    return True

if __name__ == "__main__":
    try:
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)