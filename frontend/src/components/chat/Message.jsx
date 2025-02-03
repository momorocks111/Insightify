import React from "react";

const Message = ({ message }) => {
  return (
    <div
      className={`message ${
        message.sender === "user" ? "user-message" : "ai-message"
      }`}
    >
      <div className="message-content">{message.content}</div>
      {message.data && (
        <div className="message-data">
          {/* Render data visualization or table here */}
        </div>
      )}
    </div>
  );
};

export default Message;
