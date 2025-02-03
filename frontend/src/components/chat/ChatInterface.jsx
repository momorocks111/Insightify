import React from "react";
import ChatInput from "./ChatInput";
import FileUpload from "./FileUpload";
import MessageList from "./MessageList";
import { useChat } from "../../contexts/ChatContext";

function ChatInterface() {
  const { currentChat } = useChat();

  return (
    <div className="chat-interface">
      <div className="chat-messages">
        <MessageList messages={currentChat?.messages || []} />
      </div>
      <div className="chat-controls">
        <FileUpload />
        <ChatInput />
      </div>
    </div>
  );
}

export default ChatInterface;
