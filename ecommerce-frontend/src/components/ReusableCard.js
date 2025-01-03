import React, { useState } from "react";
import "./ReusableCard.css";
import ProductCard from "./productCard";

const ReusableCard = ({
  title,
  content,
  onConsume,
  label,
  recommendedProduct,
  productType,
  resetProduct,
  currentThreshold, // Current threshold passed as a prop
  onThresholdChange, // Callback function for threshold changes
}) => {
  const [showRecommendation, setShowRecommendation] = useState(true);
  const [isEditingThreshold, setIsEditingThreshold] = useState(false); // State for editing threshold
  const [newThreshold, setNewThreshold] = useState(currentThreshold);

  const handleBuyNow = () => {
    resetProduct(productType);
    // setShowRecommendation(false);
  };

  const openThresholdEditor = () => {
    setIsEditingThreshold(true);
  };

  const saveThreshold = () => {
    onThresholdChange(productType, newThreshold); // Pass new threshold to parent
    setIsEditingThreshold(false);
  };

  return (
    <div className="item">
      <h2>{title}</h2>
      {content}
      <button onClick={onConsume} className="consume-button">
        Consume {title}
      </button>
      <p>{label}</p>

      <div className="settings">
        <span className="three-dots" onClick={openThresholdEditor}>
          &#x22EE; {/* Three dots menu */}
        </span>
      </div>

      {isEditingThreshold && (
        <div className="threshold-editor">
          <h4>Edit Threshold for {title}</h4>
          <input
            type="range"
            min="0"
            max="1000"
            value={newThreshold}
            onChange={(e) => setNewThreshold(Number(e.target.value))}
          />
          <p>New Threshold: {newThreshold}</p>
          <button onClick={saveThreshold} className="save-button">
            Save
          </button>
          <button
            onClick={() => setIsEditingThreshold(false)}
            className="cancel-button"
          >
            Cancel
          </button>
        </div>
      )}

      {showRecommendation && recommendedProduct && (
        <div className="recommendation-section">
          <h3>Recommended Product:</h3>
          <ProductCard product={recommendedProduct} />
          <p>Stock is reducing. If you want to purchase more, click below:</p>
          <button onClick={handleBuyNow} className="buy-now-button">
            Buy Now
          </button>
        </div>
      )}
    </div>
  );
};

export default ReusableCard;
