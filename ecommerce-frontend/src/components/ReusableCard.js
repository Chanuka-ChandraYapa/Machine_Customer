import React from "react";
import "./ReusableCard.css";
import ProductCard from "./productCard";

const ReusableCard = ({ title, content, onConsume, label, recommendedProduct }) => {
  return (
    <div className="item">
      <h2>{title}</h2>
      {content}
      <button onClick={onConsume} className="consume-button">
        Consume {title}
      </button>
      <p>{label}</p>

      {/* If there's a recommended product, show it in the card */}
      {recommendedProduct && (
        <div className="recommendation-section">
          <h3>Your product is redusing. Buy Now</h3>
          <h3>Recommended Product:</h3>
          <ProductCard product={recommendedProduct} />  {/* Render recommended product */}
        </div>
      )}
    </div>
  );
};

export default ReusableCard;
