import json

"""
Json BLE Format
{
    devices:[
        {
            name: Donates Device Name
            addr: Device's MacAddress
            role: Central/Peripheral device
            class: Device Class in hex
            type: Description of Device Class
        }
    ]
}
"""

def parse_to_dict(file: str)-> dict:
    with open(file, 'r') as f:
        s= f.read()
        d = json.loads(s)
    return d["devices"]
