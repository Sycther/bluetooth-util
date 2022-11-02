import bluetooth

def scan_nearby():
   print("Scanning for bluetooth devices: ")
   devices = bluetooth.discover_devices(lookup_names = True, lookup_class=True)
   number_of_devices = len(devices)
   print(number_of_devices, "devices found")
   for addr,name,clss in devices:
      print("\n")
      print("Device Name: %s" % (name))
      print("Device MAC Address: %s" % (addr))
      print("Class: %s" % (clss))
      print("Services Found:")
      services = bluetooth.find_service(address=addr)
      if len(services) <=0:
          print("zero services found on", addr)
      else:
          for serv in services:
              print(serv['name'])
      print("\n")
   return()