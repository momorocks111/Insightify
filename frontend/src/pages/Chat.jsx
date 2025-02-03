import React from "react";
import ChatInterface from "../components/chat/ChatInterface";
import DataVisualization from "../components/data/DataVisualization";
import { useChat } from "../contexts/ChatContext";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChartLine, faRobot } from "@fortawesome/free-solid-svg-icons";

function Chat() {
  const { currentChat } = useChat();

  return (
    <div className="chat-page">
      <header className="chat-header">
        <h1>
          <FontAwesomeIcon icon={faRobot} /> AI Data Analysis
        </h1>
        {currentChat && <p className="chat-id">Chat ID: {currentChat.id}</p>}
      </header>
      <div className="chat-content">
        <div className="chat-main">
          <ChatInterface />
        </div>
        <div className="chat-sidebar">
          <h2>
            <FontAwesomeIcon icon={faChartLine} /> Data Insights
          </h2>
          <DataVisualization />
        </div>
      </div>
    </div>
  );
}

export default Chat;
