from bleak import BleakScanner
import asyncio

class BLEUtil(BleakScanner):    

    def __init__(self, callback = None) -> None:
        super().__init__(callback)
        self.callback = callback
        self.current_devices: list = []


    async def scan(self, duration=5):
        async with self:
            await asyncio.sleep(duration)

        self.current_devices = self.discovered_devices

    def code_to_desc(code: int) -> str:
        mask = 1 << 21
        if code & mask:
            print(code & mask)
            print("Audio Device")
        pass