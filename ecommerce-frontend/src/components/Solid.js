import React from "react";
import "./ReusableCard.css";

const Solid = ({ mass, maxMass }) => {
  const heightPercentage = (mass / maxMass) * 100;

  return (
    <div className="solid-container">
      <div
        className="solid-block"
        style={{ height: `${heightPercentage}%` }}
      ></div>
    </div>
  );
};

export default Solid;
