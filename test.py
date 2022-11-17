import bluetooth

def find():
    services = bluetooth.find_service(address="04:21:44:BF:74:61")
    print(services)

def scan():
    devices = bluetooth.discover_devices(lookup_class=True, lookup_names=True)
    for device in devices:
        print("{}\n- {}\n- {}".format(device[1], device[0], hex(device[2])))

scan()