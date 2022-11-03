import bluetooth

def scan_nearby():
    nearby_devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
    print("Found {} devices.".format(len(nearby_devices)))

    for addr, name, clss in nearby_devices:
        print("  {} - {} - {}".format(addr, name, hex(clss)))

    
    print(bluetooth.find_service())
