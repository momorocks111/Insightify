import React, {
  createContext,
  useState,
  useContext,
  useEffect,
  useCallback,
} from "react";
import axios from "axios";

const ChatContext = createContext();

export function ChatProvider({ children }) {
  const [chats, setChats] = useState([]);
  const [currentChat, setCurrentChat] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);

  // Load chats from localStorage on initial render
  useEffect(() => {
    try {
      const savedChats = JSON.parse(localStorage.getItem("chats") || "[]");
      setChats(savedChats);
      if (savedChats.length > 0) {
        setCurrentChat(savedChats[0]);
      }
    } catch (error) {
      console.error("Error loading chats from localStorage:", error);
    }
  }, []);

  // Save chats to localStorage whenever they change
  useEffect(() => {
    try {
      localStorage.setItem("chats", JSON.stringify(chats));
    } catch (error) {
      console.error("Error saving chats to localStorage:", error);
    }
  }, [chats]);

  const createNewChat = useCallback(() => {
    const newChat = {
      id: Date.now(),
      title: `Chat ${Date.now()}`,
      messages: [],
      isLoading: false, // Added isLoading flag for each chat
    };
    setChats((prevChats) => [newChat, ...prevChats]);
    setCurrentChat(newChat);
    return newChat.id;
  }, []);

  const switchChat = useCallback(
    (chatId) => {
      const chat = chats.find((c) => c.id === chatId);
      if (chat) {
        setCurrentChat(chat);
      }
    },
    [chats]
  );

  const deleteChat = useCallback(
    (chatId) => {
      setChats((prevChats) => prevChats.filter((chat) => chat.id !== chatId));
      if (currentChat && currentChat.id === chatId) {
        setCurrentChat((prevChats) => prevChats[0] || null);
      }
    },
    [currentChat]
  );

  const sendMessage = async (content) => {
    if (currentChat) {
      const newMessage = { content, sender: "user", timestamp: Date.now() };
      const updatedChat = {
        ...currentChat,
        messages: [...currentChat.messages, newMessage],
        isLoading: true,
      };

      setCurrentChat(updatedChat);
      setChats(
        chats.map((chat) => (chat.id === currentChat.id ? updatedChat : chat))
      );

      try {
        let response;
        if (selectedFile) {
          const formData = new FormData();
          formData.append("file", selectedFile);
          formData.append("chat_id", currentChat.id);
          formData.append("message", content);

          response = await axios.post(
            "http://127.0.0.1:5000/api/analyze_with_file",
            formData,
            {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            }
          );
          setSelectedFile(null);
        } else {
          response = await axios.post(
            "http://127.0.0.1:5000/api/echo",
            { message: content },
            { headers: { "Content-Type": "application/json" } }
          );
        }

        const botMessage = {
          content: response.data.message,
          sender: "bot",
          timestamp: Date.now(),
          fileInfo: response.data.file_info,
        };

        const chatWithBotResponse = {
          ...updatedChat,
          messages: [...updatedChat.messages, botMessage],
          isLoading: false,
        };

        setCurrentChat(chatWithBotResponse);
        setChats(
          chats.map((chat) =>
            chat.id === currentChat.id ? chatWithBotResponse : chat
          )
        );
      } catch (error) {
        console.error("Error sending message:", error);
        const errorMessage = {
          content: "Failed to connect to the server.",
          sender: "bot",
          timestamp: Date.now(),
        };
        const chatWithErrorResponse = {
          ...updatedChat,
          messages: [...updatedChat.messages, errorMessage],
          isLoading: false,
        };
        setCurrentChat(chatWithErrorResponse);
        setChats(
          chats.map((chat) =>
            chat.id === currentChat.id ? chatWithErrorResponse : chat
          )
        );
      }
    }
  };

  const uploadFile = (filename) => {
    if (currentChat) {
      const newMessage = {
        content: `File uploaded: ${filename}`,
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
    }
  };

  return (
    <ChatContext.Provider
      value={{
        chats,
        currentChat,
        createNewChat,
        sendMessage,
        uploadFile,
        switchChat,
        deleteChat,
        setSelectedFile, // Add this
      }}
    >
      {children}
    </ChatContext.Provider>
  );
}

export const useChat = () => useContext(ChatContext);
