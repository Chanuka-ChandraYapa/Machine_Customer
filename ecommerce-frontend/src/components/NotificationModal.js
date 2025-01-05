import React from "react";
import "./NotificationModal.css";

const NotificationModal = ({ notifications, onClose }) => {
  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <button className="modal-close" onClick={onClose}>
          ×
        </button>
        <h2>Notifications</h2>
        {notifications.length > 0 ? (
          <ul>
            {notifications.map((notif, index) => (
              <li key={index}>
                <strong>{notif.type}: </strong>
                {notif.message}
              </li>
            ))}
          </ul>
        ) : (
          <p>No notifications available.</p>
        )}
      </div>
    </div>
  );
};

export default NotificationModal;
