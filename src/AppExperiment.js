import React, { Component } from "react";
import ReactFileReader from "react-file-reader";

const readLastLines = require("read-last-lines");

class Home extends Component {
  constructor(props) {
    super(props);
    this.handleFiles = this.handleFiles.bind(this);
  }

  /**
   * Function to upload file
   */
  handleFiles = (path) => {
    readLastLines.read('/home/chetan/Desktop/Work/gdfShikha/finalGaph/graph/src/test.txt', 2)
    .then((lines) => console.log(lines));
  }
  render() {
    return (
     <div>Hey</div>
    );
  }
}

export default Home;
