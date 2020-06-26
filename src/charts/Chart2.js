import React, { Component } from "react";
// import io from "socket.io-client";
import "./App.css";
import CanvasJSReact from "./canvasjs.react";
var CanvasJSChart = CanvasJSReact.CanvasJSChart;
// var CanvasJS = CanvasJSReact.CanvasJS;

let dps1 = [];

class Chart2 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      nn: {
        title: {
          text: "Reference2",
        },
        data: [],
      },
    };
  }

  componentDidMount = (event) => {
   const socket = this.props.socket;
    socket.on("data2", (msg) => {
      dps1 = msg;
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
            text: "Reference2",
          },
          data: dataa,
        },
      });
      console.log(this.state.nn);
    });
  };
  render() {
    console.log('CHART1==',this.state)
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


export default Chart2;
