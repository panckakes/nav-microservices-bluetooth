# manage.py


# import unittest
# import coverage

from flask_script import Manager
from project import create_app, db
from project.api.models import User, Bluetooth
from blue import *
#
# #python multi-threading imports
# import threading
# import time

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




# def start_runner():
    # def recreate_test_databases(engine = None, session = None):
    #   if engine == None:
    #     engine = db.engine
    #   if session == None:
    #     session = db.session
    #
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)

    # with app.app_context():
    #     scan_devices_thread.start()
    # # def start_loop():
    #     not_started = True
    #     while not_started:
    #         print('In start loop')
    #         try:
    #             r = requests.get('http://127.0.0.1:5000/')
    #             if r.status_code == 200:
    #                 print('Server started, quiting start_loop')
    #                 not_started = False
    #             print(r.status_code)
    #         except:
    #             print('Server not yet started')
    #         time.sleep(2)
    #
    # print('Started runner')
    # thread = threading.Thread(target=start_loop)
    # thread.start()

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
    manager.run()
    #start bluetooth scan
