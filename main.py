import asyncio
from BLEUtil import BLEUtil

from GUI import Ui_MainWindow

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

class TestWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(TestWindow, self).__init__()
        self.setupUi(self)
        self.scanner = BLEUtil(self.callback)

    def callback(self, device, advertisment_data):
        if not device in self.scanner.current_devices:
            out = "{}  ({})\n - {}".format(device.name, device.address, advertisment_data)
            self.list.addItem(out)
            self.scanner.current_devices.append(device)

    @asyncSlot()
    async def scanNow(self):
        print("Scanning")
        try:
            await self.scanner.scan(3)
            pass
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
    mw.resize(WIN_WIDTH, WIN_HEIGHT)
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