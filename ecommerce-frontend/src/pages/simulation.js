import React, { useState } from "react";
import ReusableCard from "../components/ReusableCard";
import Liquid from "../components/Liquid";
import Solid from "../components/Solid";
import Individual from "../components/Individual";
import "./Simulation.css";

const Simulation = () => {
  const [milkVolume, setMilkVolume] = useState(2000); // Initial milk volume in mL
  const [butterMass, setButterMass] = useState(500); // Initial butter mass in grams
  const [eggCount, setEggCount] = useState(30); // Initial egg count

  return (
    <div className="simulation-container">
      <h1>Food Simulation</h1>
      <div className="food-items">

        {/* Milk */}
        <ReusableCard
          title="Milk"
          content={<Liquid volume={milkVolume} maxVolume={1000} />}
          onConsume={() => setMilkVolume((prev) => (prev > 100 ? prev - 100 : 0))}
          label={`Milk Volume: ${milkVolume} mL`}
        />

        {/* Butter */}
        <ReusableCard
          title="Butter"
          content={<Solid mass={butterMass} maxMass={500} />}
          onConsume={() => setButterMass((prev) => (prev > 50 ? prev - 50 : 0))}
          label={`Butter Mass: ${butterMass} g`}
        />

        {/* Eggs */}
        <ReusableCard
          title="Eggs"
          content={<Individual count={eggCount} />}
          onConsume={() => setEggCount((prev) => (prev > 0 ? prev - 1 : 0))}
          label={`Eggs Remaining: ${eggCount}`}
        />

      </div>
    </div>
  );
};

export default Simulation;
