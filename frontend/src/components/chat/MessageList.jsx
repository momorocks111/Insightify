import React from "react";
import Message from "./Message";

const MessageList = ({ messages, isLoading }) => {
  return (
    <div className="message-list">
      {messages.map((message, index) => (
        <div key={index} className="message-wrapper">
          <Message message={message} />
          {isLoading && index === messages.length - 1 && (
            <div className="loading-spinner"></div> // Circular loading spinner
          )}
        </div>
      ))}
    </div>
  );
};

export default MessageList;
