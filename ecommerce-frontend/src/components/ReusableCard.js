import React, { useState } from "react";
import "./ReusableCard.css";
import ProductCard from "./productCard";

const ReusableCard = ({ title, content, onConsume, label, recommendedProduct, productType, resetProduct }) => {
  const [showRecommendation, setShowRecommendation] = useState(true);

  const handleBuyNow = () => {
    // Reset product quantity to its full value
    resetProduct(productType);
    // Hide the recommendation section after purchase
    setShowRecommendation(false);
  };

  return (
    <div className="item">
      <h2>{title}</h2>
      {content}
      <button onClick={onConsume} className="consume-button">
        Consume {title}
      </button>
      <p>{label}</p>

      {/* Show the recommendation section if the threshold is reached and the product is not bought */}
      {showRecommendation && recommendedProduct && (
        <div className="recommendation-section">
          <h3>Recommended Product:</h3>
          <ProductCard product={recommendedProduct} /> {/* Render recommended product */}
          <p>
            Stock is reducing. If you want to purchase more, click below:
          </p>
          <button onClick={handleBuyNow} className="buy-now-button">
            Buy Now
          </button>
        </div>
      )}
    </div>
  );
};
export default ReusableCard;
