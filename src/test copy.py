import random
import json
import socketio
import eventlet
from flask import Flask, render_template
from flask import Flask, session, request, json as flask_json
from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
    Namespace, disconnect
import os
import socket
from pathlib import Path
from time import sleep
from threading import Thread, Event
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app)
socketio = SocketIO(app, cors_allowed_origins="*",
                    async_mode=None, logger=False, engineio_logger=True)
today = pd.datetime.now().date()
today1 = str(today)


def tail(file, n=1, bs=1024):
    f = open(file)
    f.seek(0, 2)
    l = 1-f.read(1).count('\n')
    B = f.tell()
    while n >= l and B > 0:
        block = min(bs, B)
        B -= block
        f.seek(B, 0)
        l += f.read(block).count('\n')
    f.seek(B, 0)
    l = min(l, n)
    lines = f.readlines()[-l:]
    f.close()
    return lines


def graph():
    try:
        while True:
            lines = tail(
                rf"/home/chetan/Desktop/Work/gdfShikha/finalGaph/graph/src/test.txt")
            for line in lines:
                data = json.loads(line)
                print(data)

                if data["type"] == "Reference":

                    list1 = [data["data0"], data["data1"], data["data2"],
                             data["data3"], data["data4"], data["data5"],
                             data["data6"], data["data7"], data["data8"], data["data9"]]
                    socketio.emit('data1', list1, broadcast=True)

            socketio.sleep(1)
    except ValueError:
        pass


@socketio.on('connect')
def test_connect():
    print('Client connected')
    socketio.start_background_task(graph)


if __name__ == ("__main__"):
    # socketio.run(app,host="192.168.1.62", port=5002)
    socketio.run(app, host="192.168.43.188", port=8002)
