# manage.py


# import unittest
# import coverage

from flask_script import Manager
from project import create_app, db
from project.api.models import Bluetooth
# from blue import *
#
#python multi-threading imports
import threading
import time
import bluetooth


# COV = coverage.coverage(
#     branch=True,
#     include='project/*',
#     omit=[
#         'project/tests/*'
#     ]
# )
# COV.start()


app = create_app()
manager = Manager(app)

@app.before_first_request
def scan_bluetooth_job():

    def scan_devices(threadName, counter):
        print("scanning bluetooth devices...")
        while counter:

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
                        print ('Checking to see if device is in database')
                        #check to see if the device is already in the database
                        check = db.session.query(db.exists().where(Bluetooth.address == addr)).scalar()
                        #if does not exist, add to database
                        print check
                        if check == False:
                            print ('device not in databse')
                            try:
                                print("Adding  %s - %s to databse" % (addr, name))
                                #add MAC address and device name to database
                                db.session.add(Bluetooth(address=addr, name=name))
                                db.session.commit()
                                print ('great success!')
                            except UnicodeEncodeError:
                                print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
                                db.session.add(Bluetooth(addr=address, name=name.encode('utf-8', 'replace')))
                                db.session.commit()


            counter = 1

            #exits the thread
            if exitFlag:
                threadName.exit()

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

    scan_devices_thread = scanDevicesThread(1, "scan_devices", 10)

    scan_devices_thread.start()



@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1

@manager.command
def scan():
    scan_devices()

@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='michael', email="michael@realpython.com"))
    db.session.add(User(username='michaelherman', email="michael@mherman.org"))
    db.session.add(Bluetooth(name='michaels_iphone', address="00:11:22:33:FF:EE"))
    db.session.add(Bluetooth(name='michaels_other_iphone', address="04:64:22:DE:AC:EE"))
    db.session.commit()


if __name__ == '__main__':
    # start_runner()
    scan_bluetooth_job()
    manager.run()
    #start bluetooth scan
