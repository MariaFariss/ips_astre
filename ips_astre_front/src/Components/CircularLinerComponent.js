import React from "react";
import ReactDOM from "react-dom";
// import {} from "@thomasloven/round-slider";
import Roundy from "roundy";
import "../App.css";

const test = (event) => {
  console.log(event);
};


export default function  CircularLiner({hypothesis ,weightData, onChange}) {
  return (
    <div className="CircularLinerComponent">
      {/* <h1 style={{ position: "absolute", marginTop: "40px" }}>$100</h1> */}
      <Roundy
        value={Math.abs(weightData)*20}
        // min={10}
        // max={30}
        stepSize={20}
        sliced={5}
        radius={100}
        color="pink"
        // render={(e) => <p>ss</p>}
        arcSize={180}
        strokeWidth={8}
        onChange={(e) => onChange(e, hypothesis)}
      />
      <p>{hypothesis.join(' - ')}</p>

    </div>
  );
}

