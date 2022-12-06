from bleak import BleakScanner
import asyncio

class Scanner(BleakScanner):    

    def __init__(self, callback = None) -> None:
        super().__init__(callback, scanning_mode='active')
        self.callback = callback
        self.current_devices: list = []


    async def scan(self, duration=5):
        self.current_devices = []
        async with self:
            await asyncio.sleep(duration)

        for dev in self.discovered_devices:
            if dev.name == "Bepob":
                print(dev)