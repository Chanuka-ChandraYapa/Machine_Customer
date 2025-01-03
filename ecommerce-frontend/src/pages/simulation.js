import React, { useState, useEffect } from "react";
import ReusableCard from "../components/ReusableCard";
import Liquid from "../components/Liquid";
import Solid from "../components/Solid";
import Individual from "../components/Individual";
import NotificationModal from "../components/NotificationModal";
import { FaBell } from "react-icons/fa";
import "./Simulation.css";
import { sendProductUpdates } from "../services/modelService";

const Simulation = () => {
  const [milkVolume, setMilkVolume] = useState(1000); // Initial milk volume in mL
  const [butterMass, setButterMass] = useState(500); // Initial butter mass in grams
  const [eggCount, setEggCount] = useState(30); // Initial egg count

  // Recommended products
  const [recommendedMilk, setRecommendedMilk] = useState(null);
  const [recommendedButter, setRecommendedButter] = useState(null);
  const [recommendedEgg, setRecommendedEgg] = useState(null);

  // Thresholds
  const [milkThreshold, setMilkThreshold] = useState(200);
  const [butterThreshold, setButterThreshold] = useState(100);
  const [eggThreshold, setEggThreshold] = useState(5);

  // Automatic buying toggle
  const [automaticBuying, setAutomaticBuying] = useState(false);

  // For notifications
  const [notifications, setNotifications] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const checkThresholds = () => {
    const newNotifications = [];
    if (milkVolume < milkThreshold) {
      newNotifications.push({
        type: "Milk",
        message:
          "According to your past Consumption, milk stocks will ends within 2 days.",
      });
    }
    if (butterMass < butterThreshold) {
      newNotifications.push({
        type: "Butter",
        message:
          "According to your past Consumption, Butter stocks will ends within 2 days.",
      });
    }
    if (eggCount < eggThreshold) {
      newNotifications.push({
        type: "Eggs",
        message:
          "According to your past Consumption, Egg stocks will ends within 2 days.",
      });
    }
    setNotifications(newNotifications);
  };

  const handleConsume = async (productName, remainingQuantity) => {
    try {
      const response = await sendProductUpdates({
        productName: productName,
        remainingQuantity: remainingQuantity,
      });
      console.log(`${productName} update sent successfully:`, response);

      if (response.best_product) {
        if (productName === "Milk" && remainingQuantity < milkThreshold) {
          setRecommendedMilk(response.best_product);
        } else if (
          productName === "Butter" &&
          remainingQuantity < butterThreshold
        ) {
          setRecommendedButter(response.best_product);
        } else if (productName === "Eggs" && remainingQuantity < eggThreshold) {
          setRecommendedEgg(response.best_product);
        }
      }
    } catch (error) {
      console.error(`Error sending update for ${productName}:`, error);
    }
  };

  const handleRefill = (productType) => {
    switch (productType) {
      case "Milk":
        setMilkVolume(1000);
        setRecommendedMilk(null); // Reset recommended product
        break;
      case "Butter":
        setButterMass(500);
        setRecommendedButter(null); // Reset recommended product
        break;
      case "Eggs":
        setEggCount(30);
        setRecommendedEgg(null); // Reset recommended product
        break;
      default:
        break;
    }
  };

  useEffect(() => {
    checkThresholds();
  }, [milkVolume, butterMass, eggCount]);

  return (
    <div className="simulation-container">
      <h1 className="title">Smart Refrigerator</h1>
      {/* Notification Bell */}
      <div
        className="notification-bell-container"
        onClick={() => setIsModalOpen(true)}
      >
        <FaBell size={24} className="bell-icon" color="#61dafb" />
        {notifications.length > 0 && <span className="notification-dot"></span>}
      </div>
      {/* Notification Modal */}
      {isModalOpen && (
        <NotificationModal
          notifications={notifications}
          onClose={() => setIsModalOpen(false)}
        />
      )}
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
          productType="Milk"
          resetProduct={handleRefill}
        />

        <ReusableCard
          title="Butter"
          content={<Solid mass={butterMass} maxMass={500} />}
          onConsume={() => {
            setButterMass((prev) => Math.max(0, prev - 50));
            handleConsume("Butter", butterMass - 50);
          }}
          label={`Butter Mass: ${butterMass} g`}
          recommendedProduct={recommendedButter}
          threshold={butterThreshold}
          productType="Butter"
          resetProduct={handleRefill}
        />

        <ReusableCard
          title="Eggs"
          content={<Individual count={eggCount} />}
          onConsume={() => {
            setEggCount((prev) => Math.max(0, prev - 1));
            handleConsume("Eggs", eggCount - 1);
          }}
          label={`Eggs Remaining: ${eggCount}`}
          recommendedProduct={recommendedEgg}
          threshold={eggThreshold}
          productType="Eggs"
          resetProduct={handleRefill}
        />
      </div>
    </div>
  );
};

export default Simulation;
