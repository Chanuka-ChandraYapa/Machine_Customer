import React, { useState } from "react";
import ReusableCard from "../components/ReusableCard";
import Liquid from "../components/Liquid";
import Solid from "../components/Solid";
import Individual from "../components/Individual";
import "./Simulation.css";
import { sendProductUpdates } from "../services/modelService";

const Simulation = () => {
  const [milkVolume, setMilkVolume] = useState(1000); // Initial milk volume in mL
  const [butterMass, setButterMass] = useState(500); // Initial butter mass in grams
  const [eggCount, setEggCount] = useState(30); // Initial egg count

  const handleConsume = async (productName, remainingQuantity) => {
    try {
      const response = await sendProductUpdates({ productName: productName, remainingQuantity: remainingQuantity });
      console.log(`${productName} update sent successfully:`, response);
    } catch (error) {
      console.error(`Error sending update for ${productName}:`, error);
    }
  };

  return (
    <div className="simulation-container">
      <h1>Food Simulation</h1>
      <div className="food-items">

        {/* Milk */}
        <ReusableCard
          title="Milk"
          content={<Liquid volume={milkVolume} maxVolume={1000} />}
          onConsume={() => {
            setMilkVolume((prev) => {
              const newVolume = prev > 100 ? prev - 100 : 0;
              handleConsume("Milk", newVolume);
              return newVolume;
            });
          }}
          label={`Milk Volume: ${milkVolume} mL`}
        />

        {/* Butter */}
        <ReusableCard
          title="Butter"
          content={<Solid mass={butterMass} maxMass={500} />}
          onConsume={() => {
            setButterMass((prev) => {
              const newMass = prev > 50 ? prev - 50 : 0;
              handleConsume("Butter", newMass);
              return newMass;
            });
          }}
          label={`Butter Mass: ${butterMass} g`}
        />

        {/* Eggs */}
        <ReusableCard
          title="Eggs"
          content={<Individual count={eggCount} />}
          onConsume={() => {
            setEggCount((prev) => {
              const newCount = prev > 0 ? prev - 1 : 0;
              handleConsume("Eggs", newCount);
              return newCount;
            });
          }}
          label={`Eggs Remaining: ${eggCount}`}
        />

      </div>
    </div>
  );
};

export default Simulation;
