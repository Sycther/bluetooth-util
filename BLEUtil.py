from bleak import BleakScanner
import asyncio
import ble_dict

class BLEUtil(BleakScanner):    

    def __init__(self, callback = None) -> None:
        super().__init__(callback)
        self.callback = callback
        self.current_devices: list = []


    async def scan(self, duration=5):
        async with self:
            await asyncio.sleep(duration)

        self.current_devices = self.discovered_devices

    def parse_device_data(self, device) -> str:
        out = ""

        try:
            data = device.metadata['manufacturer_data'].popitem()
        except KeyError:
            return "No Data Given"
        cic = data[0]
        cod = data[1]
        
        out = ble_dict.CIC_MAP[cic]
        if not out:
            return "Unable to find Matching CIC"

        return out