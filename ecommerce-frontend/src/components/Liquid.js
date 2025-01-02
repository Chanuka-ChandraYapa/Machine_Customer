import React from "react";
import "./ReusableCard.css";

const Liquid = ({ volume, maxVolume }) => {
  const heightPercentage = (volume / maxVolume) * 100;

  return (
    <div className="liquid-container">
      <div className="lid"></div>
      <div className="bottle">
        <div
          className="liquid-level"
          style={{ height: `${heightPercentage}%` }}
        ></div>
      </div>
    </div>
  );
};

export default Liquid;
