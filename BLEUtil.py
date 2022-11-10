from bleak import BleakScanner
import asyncio

class BLEUtil(BleakScanner):
    
    def __init__(self, callback = None) -> None:
        super().__init__(callback)
        self.callback = callback


    async def scan(self, duration=5):
        async with self:
            await asyncio.sleep(duration)