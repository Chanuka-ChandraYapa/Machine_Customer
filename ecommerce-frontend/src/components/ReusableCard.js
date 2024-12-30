import React from "react";
import "./ReusableCard.css";

const ReusableCard = ({ title, content, onConsume, label }) => {
  return (
    <div className="item">
      <h2>{title}</h2>
      {content}
      <button onClick={onConsume} className="consume-button">
        Consume {title}
      </button>
      <p>{label}</p>
    </div>
  );
};

export default ReusableCard;
