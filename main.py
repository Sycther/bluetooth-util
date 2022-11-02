import json_ble 

def App():
    current_scan = json_ble.parse_to_dict("test.json")

    print(current_scan[0])

if __name__ == "__main__":
    App()

