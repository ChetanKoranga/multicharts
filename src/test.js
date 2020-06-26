import React from 'react';
import io from 'socket.io-client';

const socket=io("http://127.0.0.1:5000");
socket.on('connect',() => {socket.send("Ack");})
socket.on('message',(msg) => {console.log(msg); const received_msg=msg})