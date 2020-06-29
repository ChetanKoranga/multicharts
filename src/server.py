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
from pathlib import Path
import os.path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app)
socketio = SocketIO(app, cors_allowed_origins="*",
                    async_mode=None, logger=False, engineio_logger=True)
today = pd.datetime.now().date()
today1 = str(today)


def tail(file):
    print(file)
    exist = os.path.isfile(file)
    print("EXIST=== ", exist)
    if exist:
        with open(file, 'r') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            print('TAIL====', last_line)
            return last_line


def tailing(path, *filename):
    while True:
        print(filename)
        for file in filename:
            line = tail(f'{path}{file}')
            if line:
                datapoints = json.loads(line)
                print('Tailing===', datapoints)

                data = {'chart_name': datapoints['chartname'], 'list1': [datapoints["data0"], datapoints["data1"], datapoints["data2"],
                                                                         datapoints["data3"], datapoints["data4"], datapoints["data5"],
                                                                         datapoints["data6"], datapoints["data7"], datapoints["data8"], datapoints["data9"], datapoints["data10"]]}

                if datapoints["type"] == "Reference1":

                    socketio.emit('data1', data, broadcast=True)

                if datapoints["type"] == "Reference2":

                    socketio.emit('data2', data, broadcast=True)

                if datapoints["type"] == "Reference3":

                    socketio.emit('data3', data, broadcast=True)

                if datapoints["type"] == "Reference4":

                    socketio.emit('data4', data, broadcast=True)

                if datapoints["type"] == "Reference5":

                    socketio.emit('data5', data, broadcast=True)

                if datapoints["type"] == "Reference6":

                    socketio.emit('data6', data, broadcast=True)

                if datapoints["type"] == "Reference7":

                    socketio.emit('data7', data, broadcast=True)

                if datapoints["type"] == "Reference8":

                    socketio.emit('data8', data, broadcast=True)

                if datapoints["type"] == "Reference9":

                    socketio.emit('data9', data, broadcast=True)

                if datapoints["type"] == "Reference10":

                    socketio.emit('data10', data, broadcast=True)
        socketio.sleep(2)


def graph():
    try:
        file_list = ['test1.txt', 'test2.txt', 'test3.txt',
                     'test4.txt', 'test5.txt', 'test6.txt', 'test7.txt', 'test8.txt', 'test9.txt', 'test10.txt']
        tailing(
            '/home/chetan/Desktop/Work/gdfShikha/finalGaph/graph/src/datafiles/', *file_list)
    except ValueError:
        pass


@socketio.on('connect')
def test_connect():
    print('Client connected')
    socketio.start_background_task(graph)


if __name__ == ("__main__"):
    # socketio.run(app,host="192.168.1.62", port=5002)
    socketio.run(app, host="192.168.43.188", port=8002)
