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

  // Separate recommended products for each product type
  const [recommendedMilk, setRecommendedMilk] = useState(null);
  const [recommendedButter, setRecommendedButter] = useState(null);
  const [recommendedEgg, setRecommendedEgg] = useState(null);

  // Track whether the backend has been called for each product
  const [hasCalledBackendMilk, setHasCalledBackendMilk] = useState(false);
  const [hasCalledBackendButter, setHasCalledBackendButter] = useState(false);
  const [hasCalledBackendEgg, setHasCalledBackendEgg] = useState(false);

  // Generic function to send product updates to the backend
  const handleConsume = async (productName, remainingQuantity) => {
    try {
      const response = await sendProductUpdates({
        productName,
        remainingQuantity,
      });
      console.log(`${productName} update sent successfully:`, response);

      if (response.best_product) {
        if (productName === "Milk") setRecommendedMilk(response.best_product);
        else if (productName === "Butter")
          setRecommendedButter(response.best_product);
        else if (productName === "Eggs")
          setRecommendedEgg(response.best_product);
      }
    } catch (error) {
      console.error(`Error sending update for ${productName}:`, error);
    }
  };

  // Milk consume logic
  const handleMilkConsume = () => {
    setMilkVolume((prev) => {
      const newVolume = prev > 100 ? prev - 100 : 0;

      // Call backend when volume < 500 and no recent call
      if (newVolume < 500 && !hasCalledBackendMilk) {
        setHasCalledBackendMilk(true);
        handleConsume("Milk", newVolume);
      }

      // Reset flag when volume goes back above 500
      if (newVolume >= 500) {
        setHasCalledBackendMilk(false);
      }

      return newVolume;
    });
  };

  // Butter consume logic
  const handleButterConsume = () => {
    setButterMass((prev) => {
      const newMass = prev > 50 ? prev - 50 : 0;

      // Call backend when mass < 250 and no recent call
      if (newMass < 250 && !hasCalledBackendButter) {
        setHasCalledBackendButter(true);
        handleConsume("Butter", newMass);
      }

      // Reset flag when mass goes back above 250
      if (newMass >= 250) {
        setHasCalledBackendButter(false);
      }

      return newMass;
    });
  };

  // Eggs consume logic
  const handleEggConsume = () => {
    setEggCount((prev) => {
      const newCount = prev > 0 ? prev - 1 : 0;

      // Call backend when count < 10 and no recent call
      if (newCount < 10 && !hasCalledBackendEgg) {
        setHasCalledBackendEgg(true);
        handleConsume("Eggs", newCount);
      }

      // Reset flag when count goes back above 10
      if (newCount >= 10) {
        setHasCalledBackendEgg(false);
      }

      return newCount;
    });
  };

  // Reset logic
  const resetProduct = (productType) => {
    switch (productType) {
      case "Milk":
        setMilkVolume(1000);
        setHasCalledBackendMilk(false);
        break;
      case "Butter":
        setButterMass(500);
        setHasCalledBackendButter(false);
        break;
      case "Eggs":
        setEggCount(30);
        setHasCalledBackendEgg(false);
        break;
      default:
        break;
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
          onConsume={handleMilkConsume}
          label={`Milk Volume: ${milkVolume} mL`}
          recommendedProduct={recommendedMilk}
          productType="Milk"
          resetProduct={resetProduct}
        />

        {/* Butter */}
        <ReusableCard
          title="Butter"
          content={<Solid mass={butterMass} maxMass={500} />}
          onConsume={handleButterConsume}
          label={`Butter Mass: ${butterMass} g`}
          recommendedProduct={recommendedButter}
          productType="Butter"
          resetProduct={resetProduct}
        />

        {/* Eggs */}
        <ReusableCard
          title="Eggs"
          content={<Individual count={eggCount} />}
          onConsume={handleEggConsume}
          label={`Eggs Remaining: ${eggCount}`}
          recommendedProduct={recommendedEgg}
          productType="Eggs"
          resetProduct={resetProduct}
        />
      </div>
    </div>
  );
};

export default Simulation;
