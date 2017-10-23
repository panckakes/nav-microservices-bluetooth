from flask import Flask, Blueprint, render_template
from blue import search
# import requests
app = Flask(__name__)

users_blueprint = Blueprint('users', __name__, template_folder='./templates')



@app.route("/")
def hello():
    return "Hello Woapprld!"

@app.route('/bluetooth', methods=['GET'])
def bluetooth_scan():
    return render_template('bluetooth.html', search=search)

# @app.route('/temp', methods=['GET'])
# def web_temp():
#     try:
#         req = requests.get('http://localhost:9090/api/v1/query?query=navio_barometer_temp', timeout=0.01)
#         result = req.json()
#     except:
#         temp = 'timeout'
#     try:
#         temp = result['data']['result'][0]['value'][1]
#     except IndexError:
#         temp = 'null'
#     return render_template('temp.html', temp=temp)
#
# @app.route('/up', methods=['GET'])
# def up():
#     try:
#         req = requests.get('http://localhost:9090/api/v1/query?query=up', timeout=0.01)
#         result = req.json()
#     except:
#         up = 'timeout'
#     try:
#         up = result['data']['result'][0]['metric'][1]
#     except IndexError:
#         up = 'null'
#     return render_template('up.html', up=up)
