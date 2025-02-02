import React from "react";
import { useNavigate } from "react-router-dom";
import { useChat } from "../../contexts/ChatContext";

const NewChatButton = () => {
  const navigate = useNavigate();
  const { createNewChat } = useChat();

  const handleNewChat = () => {
    const newChatId = createNewChat();
    navigate(`/chat/${newChatId}`);
  };

  return (
    <button onClick={handleNewChat} className="new-chat-button">
      New Chat
    </button>
  );
};

export default NewChatButton;
