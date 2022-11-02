import json

"""
Json BLE Format
{
    devices:[
        {
            name: Donates Device Name
            addr: Device's MacAddress
            role: Central/Peripheral device
        }
    ]
}
"""

def parse_to_dict(file: str)-> dict:
    with open(file, 'r') as f:
        s = json.load(f)
    return s["devices"]