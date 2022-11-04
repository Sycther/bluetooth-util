import bluetooth
import json

def scan_nearby():
    nearby_devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
    print("Found {} devices.".format(len(nearby_devices)))

    f = open("temp/out.txt", 'w')


    for addr, name,clss in nearby_devices:
        print("  {} - {} - {}".format(addr, name,hex(clss)))

        services = bluetooth.find_service(address=addr)
        f.write(str(services))

# Parsing the Device Class into A Description of it's Usage
# Broken down into Major "Service Class | Major Device Class | Minor Device Class"

def test_doc():
    doc_parse(2360340)

def doc_parse(doc: int) -> str:
    doc_bin = bin(doc)[2:]
    
    # Major Service
    match doc :
        case 1:
            pass

    # Major Device


    # Minor Device
    return "NA"
