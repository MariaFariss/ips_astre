import React from "react";
import Roundy from "roundy";
import "../App.css";

export default function  CircularLiner({hypothesis ,weightData, onChange}) {
  return (
    <div className="CircularLinerComponent">
      <Roundy
        value={Math.abs(weightData)*20}
        stepSize={20}
        sliced={5}
        radius={100}
        color="pink"
        arcSize={180}
        strokeWidth={8}
        onChange={(e) => onChange(e, hypothesis)}
      />
      <p>{hypothesis.join(' - ')}</p>

    </div>
  );
}

