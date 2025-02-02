import React, { createContext, useState, useContext } from "react";

const ChatContext = createContext();

export function ChatProvider({ children }) {
  const [chats, setChats] = useState([]);
  const [currentChat, setCurrentChat] = useState(null);

  const createNewChat = () => {
    const newChat = { id: Date.now(), messages: [] };
    setChats([...chats, newChat]);
    setCurrentChat(newChat);
    return newChat.id;
  };

  const sendMessage = (message, file = null) => {
    // Implement logic to send message to AI and update chat
  };

  return (
    <ChatContext.Provider
      value={{ chats, currentChat, createNewChat, sendMessage }}
    >
      {children}
    </ChatContext.Provider>
  );
}

export const useChat = () => useContext(ChatContext);
