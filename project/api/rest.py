from flask import jsonify, request, make_response
from flask_restful import Resource

from sqlalchemy import exc

from project.api.models import Bluetooth
from project import db


class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class BluetoothDevices(Resource):
    def get(self):
        blueteeth = Bluetooth.query.order_by(Bluetooth.created_at.desc()).all()
        bluetooth_list = []
        for bluetooth in blueteeth:
            bluetooth_object = {
                'name': bluetooth.name,
                'address': bluetooth.address,
                'created_at': bluetooth.created_at
            }
            bluetooth_list.append(bluetooth_object)
        response_object = {
            'status': 'success',
            'data': {
                'bluetooths': bluetooth_list
            }
        }
        return jsonify(response_object)
