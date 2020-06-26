import React, { Component, Fragment } from 'react';
import io from "socket.io-client";
import Chart1 from './charts/Chart1';
import Chart2 from './charts/Chart2';
import Chart3 from './charts/Chart3';
import Chart4 from './charts/Chart4';
import Chart5 from './charts/Chart5';
import Chart6 from './charts/Chart6';
import Chart7 from './charts/Chart7';
import Chart8 from './charts/Chart8';
import Chart9 from './charts/Chart9';
import Chart10 from './charts/Chart10';

const socket = io("http://192.168.43.188:8002"); 

class App extends Component {
  
  render() {
    return (
      <Fragment>
        <div className = 'container'>
        <div className='chartleft'><Chart1 socket={socket} /></div>
        <div className='chartright'><Chart2 socket={socket} /></div>
        <div className='chartleft'><Chart3 socket={socket} /></div>
        <div className='chartright'><Chart4 socket={socket} /></div>
        <div className='chartleft'><Chart5 socket={socket} /></div>
        <div className='chartright'><Chart6 socket={socket} /></div>
        <div className='chartleft'><Chart7 socket={socket} /></div>
        <div className='chartright'><Chart8 socket={socket} /></div>
        <div className='chartleft'><Chart9 socket={socket} /></div>
        <div className='chartright'><Chart10 socket={socket} /></div>
        </div>
      </Fragment>
    );
  }
}

export default App;

