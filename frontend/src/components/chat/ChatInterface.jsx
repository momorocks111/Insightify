import React from "react";
import ChatInput from "./ChatInput";
import FileUpload from "./FileUpload";
import MessageList from "./MessageList";

function ChatInterface() {
  return (
    <div className="chat-interface">
      <MessageList />
      <div className="input-area">
        <FileUpload />
        <ChatInput />
      </div>
    </div>
  );
}

export default ChatInterface;
