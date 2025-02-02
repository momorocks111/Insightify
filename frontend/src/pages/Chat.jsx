import React from "react";
import ChatInterface from "../components/chat/ChatInterface";
import DataVisualization from "../components/data/DataTable";

function Chat() {
  return (
    <div className="chat-page">
      <h1>Chat</h1>
      <ChatInterface />
      <DataVisualization />
    </div>
  );
}

export default Chat;
