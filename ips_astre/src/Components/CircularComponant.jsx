import React, { useEffect, useState, useRef } from "react";
import ReactDOM from "react-dom";
import { CircleSlider } from "react-circle-slider";

import "../App.css";

export default function CircularComponant() {
  const [value, changeValue] = useState(20);

  const handle = (q) => {
    if (q === value) return;
    console.log(q);

    changeValue(q);
  };

  // useEffect(() => {
  //   // slider.current.setAttribute("width", "280px");
  //   console.log(value);
  // }, [value]);

  return (
    <div className="CircularComponant">
      <div className="textContainer">
        {value}
        <div className="minute">MINUTES</div>
      </div>
      <CircleSlider
        value={value}
        stepSize={1}
        onChange={(value) => handle(value)}
        size={250}
        max={100}
        gradientColorFrom="#ec008c"
        gradientColorTo="#fc6767"
        knobRadius={20}
        circleWidth={20}
        
      />
    </div>
  );
}
