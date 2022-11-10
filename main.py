import asyncio
from BLEUtil import BLEUtil
from bleak import BleakScanner

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QMainWindow,
    QStatusBar,
    QScrollArea
)

import functools, sys
import qasync
from qasync import asyncSlot, asyncClose, QApplication

### Constants
WIN_WIDTH = 800
WIN_HEIGHT = 600

devices:list = []

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setCentralWidget(MainWidget())
        status = QStatusBar(self)

class MainWidget(QWidget):

    def __init__(self, signal=None):
        super().__init__()

        self.scanner = BLEUtil(self.callback)

        self.setLayout(QVBoxLayout())

        label = QLabel("Bluetooth Utility")
        self.layout().addWidget(label)
        
        btn = QPushButton("Scan Now", self)
        btn.clicked.connect(self.scan_now)
        self.layout().addWidget(btn)

        self.scroll = QScrollArea()
        self.output = QLabel("No Devices")
        self.layout().addWidget(self.output)


    def callback(self, device, ad_data):
        if not device in devices:
            devices.append(device)
            self.output.setText("\n".join("{}".format(i) for i in self.scanner.discovered_devices))

    @asyncSlot()
    async def scan_now(self):
        self.output.setText("")

        devices.clear()

        try:
            await self.scanner.scan(3)
            pass
        except Exception as e:
            print(e)
        else :
            if len(devices) == 0:
                self.output.setText("No Devices Found")

        print("Done Scanning")

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
    mw.resize(WIN_WIDTH, WIN_HEIGHT)
    mw.show()

    await future
    return True

if __name__ == "__main__":
    try:
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)