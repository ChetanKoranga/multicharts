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
                data = json.loads(line)
                print('Tailing===', data)

                if data["type"] == "Reference1":

                    list1 = [data["data0"], data["data1"], data["data2"],
                             data["data3"], data["data4"], data["data5"],
                             data["data6"], data["data7"], data["data8"], data["data9"]]
                    socketio.emit('data1', list1, broadcast=True)

                if data["type"] == "Reference2":

                    list1 = [data["data0"], data["data1"], data["data2"],
                             data["data3"], data["data4"], data["data5"],
                             data["data6"], data["data7"], data["data8"], data["data9"]]
                    socketio.emit('data2', list1, broadcast=True)

                if data["type"] == "Reference3":

                    list1 = [data["data0"], data["data1"], data["data2"],
                             data["data3"], data["data4"], data["data5"],
                             data["data6"], data["data7"], data["data8"], data["data9"]]
                    socketio.emit('data3', list1, broadcast=True)

                if data["type"] == "Reference4":

                    list1 = [data["data0"], data["data1"], data["data2"],
                             data["data3"], data["data4"], data["data5"],
                             data["data6"], data["data7"], data["data8"], data["data9"]]
                    socketio.emit('data4', list1, broadcast=True)

                if data["type"] == "Reference5":

                    list1 = [data["data0"], data["data1"], data["data2"],
                             data["data3"], data["data4"], data["data5"],
                             data["data6"], data["data7"], data["data8"], data["data9"]]
                    socketio.emit('data5', list1, broadcast=True)

                if data["type"] == "Reference6":

                    list1 = [data["data0"], data["data1"], data["data2"],
                             data["data3"], data["data4"], data["data5"],
                             data["data6"], data["data7"], data["data8"], data["data9"]]
                    socketio.emit('data6', list1, broadcast=True)

                if data["type"] == "Reference7":

                    list1 = [data["data0"], data["data1"], data["data2"],
                             data["data3"], data["data4"], data["data5"],
                             data["data6"], data["data7"], data["data8"], data["data9"]]
                    socketio.emit('data7', list1, broadcast=True)

                if data["type"] == "Reference8":

                    list1 = [data["data0"], data["data1"], data["data2"],
                             data["data3"], data["data4"], data["data5"],
                             data["data6"], data["data7"], data["data8"], data["data9"]]
                    socketio.emit('data8', list1, broadcast=True)

                if data["type"] == "Reference9":

                    list1 = [data["data0"], data["data1"], data["data2"],
                             data["data3"], data["data4"], data["data5"],
                             data["data6"], data["data7"], data["data8"], data["data9"]]
                    socketio.emit('data9', list1, broadcast=True)

                if data["type"] == "Reference10":

                    list1 = [data["data0"], data["data1"], data["data2"],
                             data["data3"], data["data4"], data["data5"],
                             data["data6"], data["data7"], data["data8"], data["data9"]]
                    socketio.emit('data10', list1, broadcast=True)
        socketio.sleep(1)
        sleep(0.5)


def graph():
    try:
        file_list = ['test1.txt', 'test2.txt', 'test3.txt',
                     'test4.txt', 'test5.txt', 'test6.txt', 'test7.txt', 'test8.txt', 'test9.txt', 'test10.txt']
        tailing('/home/chetan/Desktop/Work/gdfShikha/finalGaph/graph/src/', *file_list)
    except ValueError:
        pass


@socketio.on('connect')
def test_connect():
    print('Client connected')
    socketio.start_background_task(graph)


if __name__ == ("__main__"):
    # socketio.run(app,host="192.168.1.62", port=5002)
    socketio.run(app, host="192.168.43.188", port=8002)
