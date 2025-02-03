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

      // Simulate chatbot response
      setTimeout(() => {
        const botMessage = {
          content: "I'm processing your request...",
          sender: "bot",
          timestamp: Date.now(),
        };
        const chatWithBotResponse = {
          ...updatedChat,
          messages: [...updatedChat.messages, botMessage],
        };
        setCurrentChat(chatWithBotResponse);
        setChats(
          chats.map((chat) =>
            chat.id === currentChat.id ? chatWithBotResponse : chat
          )
        );
      }, 1000);
    }
  };

  const uploadFile = (file) => {
    if (currentChat) {
      // For now, we'll just add a message indicating a file was uploaded
      const newMessage = {
        content: `File uploaded: ${file.name}`,
        sender: "user",
        timestamp: Date.now(),
      };
      const updatedChat = {
        ...currentChat,
        messages: [...currentChat.messages, newMessage],
      };
      setCurrentChat(updatedChat);
      setChats(
        chats.map((chat) => (chat.id === currentChat.id ? updatedChat : chat))
      );

      // Here you would typically process the file or send it to the backend
      console.log("File uploaded:", file);
    }
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
