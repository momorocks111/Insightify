import React, { createContext, useState, useContext } from "react";

const ChatContext = createContext();

export function ChatProvider({ children }) {
  const [chats, setChats] = useState([]);
  const [currentChat, setCurrentChat] = useState(null);

  const createNewChat = () => {
    const newChat = { id: Date.now(), messages: [], data: null };
    setChats([...chats, newChat]);
    setCurrentChat(newChat);
    return newChat.id;
  };

  const sendMessage = (content) => {
    if (currentChat) {
      const newMessage = { content, sender: "user", timestamp: Date.now() };
      const updatedChat = {
        ...currentChat,
        messages: [...currentChat.messages, newMessage],
      };
      setCurrentChat(updatedChat);
      setChats(
        chats.map((chat) => (chat.id === currentChat.id ? updatedChat : chat))
      );

      // Here you would typically send the message to your AI backend
      // and then add the AI's response to the chat
    }
  };

  const uploadFile = (file) => {
    // Implement file upload logic here
    // This should process the file and update the currentChat.data
  };

  return (
    <ChatContext.Provider
      value={{ chats, currentChat, createNewChat, sendMessage, uploadFile }}
    >
      {children}
    </ChatContext.Provider>
  );
}

export const useChat = () => useContext(ChatContext);
