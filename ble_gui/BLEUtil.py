from bleak import BleakScanner
import asyncio

class Scanner(BleakScanner):    

    def __init__(self, callback = None) -> None:
        super().__init__(callback)
        self.callback = callback
        self.current_devices: list = []


    async def scan_ble(self, duration=5):
        self.current_devices = []
        async with self:
            await asyncio.sleep(duration)