import React from "react";
import MessageList from "./MessageList";
import { useChat } from "../../contexts/ChatContext";
import ChatInput from "./ChatInput";
import FileUpload from "./FileUpload";

function ChatInterface() {
  const { currentChat } = useChat();

  return (
    <div className="chat-interface">
      <div className="chat-messages">
        <MessageList
          messages={currentChat?.messages || []}
          isLoading={currentChat?.isLoading}
        />
      </div>
      <div className="chat-controls">
        <FileUpload />
        <ChatInput />
      </div>
    </div>
  );
}

export default ChatInterface;
