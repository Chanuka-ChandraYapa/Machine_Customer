import React, { useState } from "react";
import "./Simulation.css"; // Optional for styling

const Simulation = () => {
  const [milkLevel, setMilkLevel] = useState(100); // Initial milk level at 100%

  const consumeMilk = () => {
    setMilkLevel((prev) => (prev > 10 ? prev - 10 : 0)); // Reduce milk by 10%, not below 0
  };

  return (
    <div className="simulation-container">
      <h1>Milk</h1>
      <div className="milk-container">
        <div className="lid"></div>
        <div className="bottle">
          <div
            className="milk-level"
            style={{ height: `${milkLevel}%` }} // Adjust the milk level height
          ></div>
        </div>
      </div>
      <button onClick={consumeMilk} className="consume-button">
        Consume Milk
      </button>
      <p>Milk Level: {milkLevel}%</p>
    </div>
  );
};

export default Simulation;
