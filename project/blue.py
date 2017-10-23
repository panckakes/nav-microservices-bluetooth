#pybluez import
import bluetooth
# from project.bluetooth import *

#python multi-threading imports
import threading
import time

from flask import Flask, current_app, app

#flask squ alchemy DB
from sqlalchemy import exc

from project.api.models import Bluetooth
from project import db

app = Flask(__name__)
##############################################

####
###### - BLUETEETH FUNCTIONS - ######
####
def scan_devices(threadName, counter):
    while counter:
        print("scanning devices...")

        #turn on discover on the bluetooth device --
        #returns 'addr' and 'name' for output
        #duration scans on units of 1.28 seconds
        nearby_devices = bluetooth.discover_devices(
                duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

        #if devices were found from the scan
        if len(nearby_devices) != 0:
            print("found %d devices" % len(nearby_devices))
            #loop through the devices
            for addr, name in nearby_devices:
                with app.app_context():
                    #check to see if the device is already in the database
                    check = db.session.query(db.exists().where(Bluetooth.address == addr)).scalar()
                    #if does not exist, add to database
                    if check == False:
                        try:
                            print("  %s - %s" % (addr, name))
                            #add MAC address and device name to database
                            db.session.add(Bluetooth(addr=address, name=name))
                            db.session.commit()
                        except UnicodeEncodeError:
                            print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
                            db.session.add(Bluetooth(addr=address, name=name.encode('utf-8', 'replace')))
                            db.session.commit()


        counter -= 1

        #exits the thread
        if exitFlag:
            threadName.exit()




def connect_device():
    name = name      # Device name
    addr = addr      # Device Address
    port = 1         # RFCOMM port
    passkey = "1111" # passkey of the device you want to connect


    # kill any "bluetooth-agent" process that is already running
    subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)

    # Start a new "bluetooth-agent" process where XXXX is the passkey
    status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)


    print("scanning devices...")
    nearby_devices = bluetooth.discover_devices(
            duration=8, lookup_names=True, flush_cache=True, lookup_class=False)


    # Now, connect in the same way as always with PyBlueZ
    try:
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        s.connect((addr,port))
    except bluetooth.btcommon.BluetoothError as err:
        # Error handler
        pass

# def disconnect_device():

def bluetooth_server(counter):
    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)


    while counter:
        uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ef"
        advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
#                   protocols = [ OBEX_UUID ]
                    )
        time.sleep(20)
        counter = 0

    if exitFlag:
       bluetooth.stop_advertising(server_sock)
       threadName.exit()

def stop_server():
    server_sock=bluetooth.BluetoothSocket( bluetooth.L2CAP )

    bluetooth.stop_advertising(server_sock)
###########################################3



####
###### - MULTITHREADING FUNCTIONS - ######
####
exitFlag = 0

class scanDevicesThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print "Starting " + self.name
      scan_devices(self.name, self.counter)
      print "Exiting " + self.name

# class startServerThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print "Starting " + self.name
#       bluetooth_server(self.counter)
#       print "Exiting " + self.name


# Create new threads
scan_devices_thread = scanDevicesThread(1, "scan_devices", 2)
# bluetooth_server_thread = startServerThread(1, "bluetooth_server", 2)




####
###### - TERNIMAL MENU - ######
####
# class switch(object):
#     value = None
#     def __new__(class_, value):
#         class_.value = value
#         return True
#
# #gather input from user - assign to 'n'
# # input = raw_input('Choose a number: \n0  for scan devices\n1  for starting scan devices in a threadded process\n2  Start bluetooth server\n3  Connect to device')
#
# n = -1
#
# def case(*args):
#     return any((arg == switch.value for arg in args))
# while n != 9:
#
# #gather input from user - assign to 'n'
#     input = raw_input('Choose a number: \n0  for scan devices\n1  for starting scan devices in a threadded process\n2  Start bluetooth server\n3  Connect to device')
#
#     n = int(input)
#     #the actual switch case
#     while switch(n):
#
#         if case(0):
#             print ("Calling scan_devices function")
#             scan_devices()
#             break
#         if case(1):
#             print ("Connect to device")
#             #start thread
#             scan_devices_thread.start()
#             # print("HHHAAAH its not done yet..")
#             break
#         if case(2):
#             print ("starting server")
#             #start thread
#             bluetooth_server_thread.start()
#             break
#         if case(3):
#             print ('stopping server')
#             connect_device()
#             break
#         if case(4):
#             print ('test text')
#             break
###############################################
