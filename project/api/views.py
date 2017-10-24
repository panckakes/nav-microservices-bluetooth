# project/api/views.py


from flask import Blueprint, jsonify, request, make_response, render_template
from sqlalchemy import exc

from project.api.models import Bluetooth
from project import db


bluetooth_blueprint = Blueprint('bluetooth', __name__, template_folder='./templates')

@bluetooth_blueprint.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    #     if request.form['submit']:
    #         username = request.form['username']
    #         email = request.form['email']
    #         db.session.add(User(username=username, email=email))
    #         db.session.commit()
    #     elif request.form['Search']:
            # scan_devices()

    # users = User.query.order_by(User.created_at.desc()).all()
    devices = Bluetooth.query.order_by(Bluetooth.created_at.desc()).all()
    return render_template('index.html', devices=devices)

# some function needs to run when the container starts to attempt to connect
# to the last device connected and start scanning devices in the area

# @bluetooth_blueprint.route('/scan_devices', methods=['GET'])
# #returns devices from last minute of scan results
# def bluetooth_scan_devices():
#     # latest_scan =
#
# @bluetooth_blueprint.route('/connect_device', methods=['GET'])
# #disconnects any connected devices and connects selected device
# def bluetooth_connect_device():
#
# @bluetooth_blueprint.route('/disconnect_device', methods=['GET'])
# #disconnects currently connected device
# def bluetooth_disconnect_device():



@bluetooth_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


# @users_blueprint.route('/users', methods=['POST'])
# def add_user():
#     post_data = request.get_json()
#     if not post_data:
#         response_object = {
#             'status': 'fail',
#             'message': 'Invalid payload.'
#         }
#         return make_response(jsonify(response_object)), 400
#     username = post_data.get('username')
#     email = post_data.get('email')
#     try:
#         user = User.query.filter_by(email=email).first()
#         if not user:
#             db.session.add(User(username=username, email=email))
#             db.session.commit()
#             response_object = {
#                 'status': 'success'
#                 # 'message': f'{email} was added!'
#             }
#             return make_response(jsonify(response_object)), 201
#         else:
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Sorry. That email already exists.'
#             }
#             return make_response(jsonify(response_object)), 400
#     except exc.IntegrityError as e:
#         db.session().rollback()
#         response_object = {
#             'status': 'fail',
#             'message': 'Invalid payload.'
#         }
#         return make_response(jsonify(response_object)), 400
#
# # @users_blueprint.route('/users', methods['POST'])
# # def scan_bluetooth_devices():
#
#
#
#
# @users_blueprint.route('/users/<user_id>', methods=['GET'])
# def get_single_user(user_id):
#     """Get single user details"""
#     response_object = {
#         'status': 'fail',
#         'message': 'User does not exist'
#     }
#     try:
#         user = User.query.filter_by(id=int(user_id)).first()
#         if not user:
#             return make_response(jsonify(response_object)), 404
#         else:
#             response_object = {
#                 'status': 'success',
#                 'data': {
#                   'username': user.username,
#                   'email': user.email,
#                   'created_at': user.created_at
#                 }
#             }
#             return make_response(jsonify(response_object)), 200
#     except ValueError:
#         return make_response(jsonify(response_object)), 404
#
#
# @users_blueprint.route('/users', methods=['GET'])
# def get_all_users():
#     """Get all users"""
#     users = User.query.order_by(User.created_at.desc()).all()
#     users_list = []
#     for user in users:
#         user_object = {
#             'id': user.id,
#             'username': user.username,
#             'email': user.email,
#             'created_at': user.created_at
#         }
#         users_list.append(user_object)
#     response_object = {
#         'status': 'success',
#         'data': {
#           'users': users_list
#         }
#     }
#     return make_response(jsonify(response_object)), 200
#
# @users_blueprint.route('/bluetooth', methods=['GET'])
# def get_all_bluetooth_devices():
#     """Get all bluetooth devices"""
#     bluetooths = Bluetooth.query.order_by(Bluetooth.created_at.desc()).all()
#     bluetooth_list = []
#     for bluetooth in bluetooths:
#         bluetooth_object = {
#             'name': bluetooth.name,
#             'address': bluetooth.address,
#             'created_at': bluetooth.created_at
#         }
#         bluetooth_list.append(bluetooth_object)
#     response_object = {
#         'status': 'success',
#         'data': {
#             'bluetooths': bluetooth_list
#         }
#     }
#     return make_response(jsonify(response_object)), 200
