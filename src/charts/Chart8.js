import React, { Component } from "react";
// import io from "socket.io-client";
import "./App.css";
import CanvasJSReact from "./canvasjs.react";
var CanvasJSChart = CanvasJSReact.CanvasJSChart;
// var CanvasJS = CanvasJSReact.CanvasJS;

let dps1 = [];

class Chart8 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      nn: {
        title: {
          text: "",
        },
        data: [],
      },
    };
  }

  componentDidMount = (event) => {
   const socket = this.props.socket;
    socket.on("data8", (msg) => {
      console.log("DATA8===",msg)
      dps1 = msg.list1;
      const dataa = [
        {
          type: "line",
          indexLabel: "{y}",
          dataPoints: dps1,
        },
      ];
      this.setState({
        nn: {
          title: {
            text: msg.chart_name,
          },
          data: dataa,
        },
      });
      // console.log(this.state.nn);
    });
  };
  render() {
    // console.log('CHART1==',this.state)
    return (
      <div>
        <CanvasJSChart
          options={this.state.nn}
          onRef={(ref) => (this.chart = ref)}
        />
      </div>
    );
  }
}


export default Chart8;