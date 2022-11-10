from bleak import BleakScanner
import asyncio


class BLEUtility():

    def __init__(self, callback, duration=5) -> None:
        self.scanner = BleakScanner()

    async def scan(self):
        self.scanner.start()

    