import asyncio
import ble_util

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel
    
async def App():
    app = QApplication(sys.argv)
    ble_util.get_previous_scans()
    devices = await ble_util.scan_now()

    label = QLabel(devices[0].name, alignment=Qt.AlignCenter)
    label.show()
    sys.exit(app.exec_())




if __name__ == "__main__":
    asyncio.run(App())

