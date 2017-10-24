# project/api/models.py


import datetime

from project import db

class Bluetooth(db.Model):
    __tablebluetooth_= "bluetooth"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, address, created_at=datetime.datetime.now()):
        self.name = name
        self.address = address
        self.created_at = created_at
