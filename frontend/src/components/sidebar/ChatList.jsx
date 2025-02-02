import React from "react";
import { Link } from "react-router-dom";
import { useChat } from "../../contexts/ChatContext";

const ChatList = () => {
  const { chats } = useChat();

  return (
    <div className="chat-list">
      <h2>Your Chats</h2>
      <ul>
        {chats.map((chat) => (
          <li key={chat.id}>
            <Link to={`/chat/${chat.id}`}>Chat {chat.id}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ChatList;
