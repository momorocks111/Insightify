import React, { useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import ChatInterface from "../components/chat/ChatInterface";
import DataVisualization from "../components/data/DataVisualization";
import { useChat } from "../contexts/ChatContext";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChartLine, faRobot } from "@fortawesome/free-solid-svg-icons";

function Chat() {
  const { id } = useParams();
  const { currentChat, switchChat, createNewChat } = useChat();
  const navigate = useNavigate();

  useEffect(() => {
    if (id) {
      switchChat(Number(id));
    }
  }, [id, switchChat]);

  if (!currentChat) {
    return (
      <div className="no-chat-message">
        <h2>Select or create a chat to begin analyzing data.</h2>
      </div>
    );
  }

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
