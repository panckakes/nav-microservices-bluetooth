# project/__init__.py


import os

from flask import Flask, jsonify, current_app
# from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from blue import *

#python multi-threading imports
import threading
import time



# instantiate the db
db = SQLAlchemy()

@app.before_first_request
def scan_bluetooth_job():
    scan_devices_thread.start()

def create_app():

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    # CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5435/users_dev'



    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.views import bluetooth_blueprint
    app.register_blueprint(bluetooth_blueprint)



    return app
