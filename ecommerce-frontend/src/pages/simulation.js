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

  const handleConsume = async (productName, remainingQuantity) => {
    try {
      const response = await sendProductUpdates({
        productName: productName,
        remainingQuantity: remainingQuantity,
      });
      console.log(`${productName} update sent successfully:`, response);

      // Update recommended products based on the consumed product
      if (response.best_product) {
        if (productName === "Milk") {
          setRecommendedMilk(response.best_product);
        } else if (productName === "Butter") {
          setRecommendedButter(response.best_product);
        } else if (productName === "Eggs") {
          setRecommendedEgg(response.best_product);
        }
      } else {
        console.error("Best product not found in the response.");
      }
    } catch (error) {
      console.error(`Error sending update for ${productName}:`, error);
    }
  };

  const resetProduct = (productType) => {
    switch (productType) {
      case "Milk":
        setMilkVolume(1000);
        break;
      case "Butter":
        setButterMass(500);
        break;
      case "Eggs":
        setEggCount(30);
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
          onConsume={() => {
            setMilkVolume((prev) => {
              const newVolume = prev > 100 ? prev - 100 : 0;
              handleConsume("Milk", newVolume);
              return newVolume;
            });
          }}
          label={`Milk Volume: ${milkVolume} mL`}
          recommendedProduct={recommendedMilk} // Only pass recommendedMilk to Milk card
          productType="Milk"
          resetProduct={resetProduct} // Pass resetProduct function to ReusableCard
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
          recommendedProduct={recommendedButter} // Only pass recommendedButter to Butter card
          productType="Butter"
          resetProduct={resetProduct} // Pass resetProduct function to ReusableCard
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
          recommendedProduct={recommendedEgg} // Only pass recommendedEgg to Egg card
          productType="Eggs"
          resetProduct={resetProduct} // Pass resetProduct function to ReusableCard
        />
      </div>
    </div>
  );
};

export default Simulation;
