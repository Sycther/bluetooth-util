import asyncio
from BLEUtil import BLEUtil

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
from qasync import asyncSlot, QApplication
import logging

### Constants
WIN_WIDTH = 800
WIN_HEIGHT = 600


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

        logging.basicConfig(filename="output",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

        logging.info("Running Urban Planning")

        self.logger = logging.getLogger('urbanGUI')


    def callback(self, device, ad_data):
        self.output.setText("\n".join("{} - {} - {}".format(i,i.metadata ,self.scanner.parse_device_data(i)) for i in self.scanner.discovered_devices))

    @asyncSlot()
    async def scan_now(self):
        self.output.setText("")

        try:
            await self.scanner.scan(3)
            pass
        except Exception as e:
            print(e)
        else :
            if len(self.scanner.discovered_devices) == 0:
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
    mw.resize(WIN_WIDTH, WIN_HEIGHT)
    mw.show()

    await future
    return True

if __name__ == "__main__":
    try:
        qasync.run(main())
    except asyncio.exceptions.CancelledError:
        sys.exit(0)