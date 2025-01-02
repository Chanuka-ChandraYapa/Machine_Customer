import React, { useState } from "react";
import ReusableCard from "../components/ReusableCard";
import Liquid from "../components/Liquid";
import Solid from "../components/Solid";
import Individual from "../components/Individual";
import "./Simulation.css";
import { sendProductUpdates } from "../services/modelService";

const Simulation = () => {
  const [milkVolume, setMilkVolume] = useState(1000); 
  const [butterMass, setButterMass] = useState(500); 
  const [eggCount, setEggCount] = useState(30); 
  const [bestProduct, setBestProduct] = useState(null); // State to store the best product

  const handleConsume = async (productName, remainingQuantity) => {
    try {
      const response = await sendProductUpdates({
        productName: productName,
        remainingQuantity: remainingQuantity,
      });
      console.log(`${productName} update sent successfully:`, response);
  
      // Directly access the best_product in the response object
      if (response.best_product) {
        setBestProduct(response.best_product);
      } else {
        console.error("Best product not found in the response.");
      }
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

      {/* If there's a best product, display it */}
      {bestProduct && (
        <ReusableCard
          title="Best Product to Buy"
          content={
            <div>
              <img src={bestProduct.thumbnail} alt={bestProduct.title} />
              <p>{bestProduct.title}</p>
              <p>{bestProduct.description}</p>
              <p>Price: ${bestProduct.price}</p>
              <button onClick={() => alert("Confirmed to buy! Proceeding...")}>
                Confirm to Buy
              </button>
            </div>
          }
          label="Product Recommendation"
        />
      )}
    </div>
  );
};

export default Simulation;
