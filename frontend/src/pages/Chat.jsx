import React from "react";
import ChatInterface from "../components/chat/ChatInterface";
import DataVisualization from "../components/data/DataVisualization";
import { useChat } from "../contexts/ChatContext";

function Chat() {
  const { currentChat } = useChat();

  return (
    <div className="chat-page">
      <header className="chat-header">
        <h1>Data Analysis Chat</h1>
        {currentChat && <p>Chat ID: {currentChat.id}</p>}
      </header>
      <div className="chat-content">
        <ChatInterface />
        <DataVisualization />
      </div>
    </div>
  );
}

export default Chat;
