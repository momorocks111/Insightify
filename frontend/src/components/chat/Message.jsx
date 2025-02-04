import React from "react";

const Message = ({ message }) => {
  return (
    <div className={`message ${message.sender}-message`}>
      <div className="message-content">{message.content}</div>
      {message.fileInfo && (
        <div className="file-info">
          <p>File: {message.fileInfo.filename}</p>
          <p>Rows: {message.fileInfo.rows}</p>
          <p>Columns: {message.fileInfo.columns}</p>
        </div>
      )}
      <div className="message-timestamp">
        {new Date(message.timestamp).toLocaleTimeString()}
      </div>
    </div>
  );
};

export default Message;
