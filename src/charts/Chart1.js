import React, { Component } from "react";
// import io from "socket.io-client";
import "./App.css";
import CanvasJSReact from "./canvasjs.react";
var CanvasJSChart = CanvasJSReact.CanvasJSChart;
// var CanvasJS = CanvasJSReact.CanvasJS;

let dps1 = [];

class Chart1 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dp: {},
    };
  }

  componentDidMount = (event) => {
    const socket = this.props.socket;
    socket.on("data1", (msg) => {
      dps1 = msg;
      
      this.setState({
          dp: dps1,
        },
      );
      
    });
  };
  render() {
    console.log(this.state)
    return (
      <div>
        <CanvasJSChart
          options={{
            animationEnabled: true,
            exportEnabled: true,
            theme: "light2", // "light1", "dark1", "dark2"
            title:{
              text: "Reference1"
            },
            data: [
              {
                type: "line",
                indexLabel: "{y}",
                dataPoints: this.props.dp,
              },
            ],
          }}
          onRef={(ref) => (this.chart = ref)}
        />
      </div>
    );
  }
}


export default Chart1;
