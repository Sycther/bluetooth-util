from bleak import BleakScanner
import asyncio
import ble_dict

class Scanner(BleakScanner):    

    def __init__(self, callback = None) -> None:
        super().__init__(callback)
        self.callback = callback
        self.current_devices: list = []


    async def scan(self, duration=5):
        self.current_devices = []
        async with self:
            await asyncio.sleep(duration)

        for dev in self.discovered_devices:
            print(dev, dev.metadata)



def parse_device_data(device) -> str:
    out = ""

    try:
        data = device.metadata['manufacturer_data'].popitem()
    except KeyError:
        return "No Data Given"
    cic = data[0]
    cod = data[1]
    try:
        out = ble_dict.SIG_MAP[cic]
    except KeyError:
        return "Unrecognized SIG"

    return out
