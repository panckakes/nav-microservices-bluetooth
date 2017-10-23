FROM resin/raspberrypi3-python:2.7

# install dependencies
RUN apt-get update && apt-get install -y bluetooth bluez libbluetooth-dev

RUN pip install pybluez

# Enable systemd
ENV INITSYSTEM on

ADD . /usr/src/app

WORKDIR /usr/src/app

# install all npm (node.js) dependencies
# RUN npm install express eddystone-beacon socket.io tinyurl cpu-usage


# run start script when reaches device
CMD ["python", "/usr/src/app/bluetooth.py"]
