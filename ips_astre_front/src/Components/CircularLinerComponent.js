import React from "react";
import ReactDOM from "react-dom";
// import {} from "@thomasloven/round-slider";
import Roundy from "roundy";
import "../App.css";

const test = (event) => {
  console.log(event);
};

/* <round-slider
  min="0"
  max="100"
  value="100"
  arclength="180"
  startangle="180"
  value-changed={event => test()}
/> */

export default function  CircularLiner() {
  const [value, setValue] = React.useState(0);
  return (
    <div className="CircularLinerComponent">
      {/* <h1 style={{ position: "absolute", marginTop: "40px" }}>$100</h1> */}
      <Roundy
        value={19}
        // min={10}
        // max={30}
        stepSize={20}
        sliced={5}
        radius={100}
        color="pink"
        // render={(e) => <p>ss</p>}
        arcSize={180}
        strokeWidth={8}
        onChange={(value) => setValue(value)}
        //  onAfterChange={(value, props) => ... }
        //  overrideStyle={ ... string template as CSS ...}
      />
      <h2>Start editing to see some magic happen!</h2>
    </div>
  );
}

