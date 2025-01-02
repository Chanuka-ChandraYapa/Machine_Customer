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

  // Thresholds
  const [milkThreshold, setMilkThreshold] = useState(200);
  const [butterThreshold, setButterThreshold] = useState(100);
  const [eggThreshold, setEggThreshold] = useState(5);

  // Automatic buying toggle
  const [automaticBuying, setAutomaticBuying] = useState(false);

  // For threshold editing modal
  const [editingThreshold, setEditingThreshold] = useState({
    type: null,
    value: null,
  });

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

  const handleEditThreshold = (type, value) => {
    console.log("Editing Threshold:", { type, value });
    setEditingThreshold({ type, value });
  };

  const handleSaveThreshold = () => {
    const { type, value } = editingThreshold;
    if (type === "Milk") setMilkThreshold(value);
    if (type === "Butter") setButterThreshold(value);
    if (type === "Eggs") setEggThreshold(value);
    setEditingThreshold({ type: null, value: null }); // Close the editor
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
      <h1 className="title">Food Simulation</h1>
      <div className="toggle-container">
        <label className="toggle-label">
          Enable Automatic Buying
          <input
            type="checkbox"
            checked={automaticBuying}
            onChange={(e) => setAutomaticBuying(e.target.checked)}
          />
          <span className="slider"></span>
        </label>
      </div>
      <div className="food-items">
        {/* Milk */}
        <ReusableCard
          title="Milk"
          content={<Liquid volume={milkVolume} maxVolume={1000} />}
          onConsume={() => {
            setMilkVolume((prev) => Math.max(0, prev - 100));
            handleConsume("Milk", milkVolume - 100);
          }}
          label={`Milk Volume: ${milkVolume} mL`}
          recommendedProduct={recommendedMilk}
          threshold={milkThreshold}
          showSettings={!automaticBuying}
          onEditThreshold={() => handleEditThreshold("Milk", milkThreshold)}
          productType="Milk"
          resetProduct={resetProduct} // Pass resetProduct function to ReusableCard
        />

        {/* Butter */}
        <ReusableCard
          title="Butter"
          content={<Solid mass={butterMass} maxMass={500} />}
          onConsume={() => {
            setButterMass((prev) => Math.max(0, prev - 50));
          }}
          label={`Butter Mass: ${butterMass} g`}
          recommendedProduct={recommendedButter}
          threshold={butterThreshold}
          showSettings={!automaticBuying}
          onEditThreshold={() => handleEditThreshold("Butter", butterThreshold)}
          resetProduct={resetProduct} // Pass resetProduct function to ReusableCard
        />

        {/* Eggs */}
        <ReusableCard
          title="Eggs"
          content={<Individual count={eggCount} />}
          onConsume={() => {
            setEggCount((prev) => Math.max(0, prev - 1));
          }}
          label={`Eggs Remaining: ${eggCount}`}
          recommendedProduct={recommendedEgg}
          threshold={eggThreshold}
          showSettings={!automaticBuying}
          onEditThreshold={() => handleEditThreshold("Eggs", eggThreshold)}
          resetProduct={resetProduct} // Pass resetProduct function to ReusableCard
        />
      </div>

      {/* Threshold Editing Modal */}
      {editingThreshold.type && (
        <div className="threshold-modal">
          <div className="modal-content">
            <h2>Edit Threshold for {editingThreshold.type}</h2>
            <input
              type="range"
              min="0"
              max="1000"
              value={editingThreshold.value}
              onChange={(e) =>
                setEditingThreshold({
                  ...editingThreshold,
                  value: Number(e.target.value),
                })
              }
            />
            <p>Current Value: {editingThreshold.value}</p>
            <button onClick={handleSaveThreshold}>Save</button>
            <button
              onClick={() => setEditingThreshold({ type: null, value: null })}
            >
              Cancel
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Simulation;
