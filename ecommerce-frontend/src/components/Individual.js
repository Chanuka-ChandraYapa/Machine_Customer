import React from "react";
import "./ReusableCard.css";

const Individual = ({ count }) => {
  // Calculate styles based on the count
  const itemSize = Math.max(100 / Math.ceil(Math.sqrt(count)), 10); // Adjust item size proportionally
  const itemStyle = {
    width: `${itemSize * 0.8}%`,
    height: `${itemSize * 0.5}%`, 
    margin: `${Math.max(2 - count * 0.02, 0.5)}%`, // Reduce margin as count increases
  };

  return (
    <div className="individual-container">
      {Array.from({ length: count }, (_, index) => (
        <div key={index} className="individual-item" style={itemStyle}></div>
      ))}
    </div>
  );
};

export default Individual;
