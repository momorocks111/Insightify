import React, { useState } from "react";
import { useChat } from "../../contexts/ChatContext";

function ChatInput() {
  const [input, setInput] = useState("");
  const { sendMessage } = useChat();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim()) {
      sendMessage(input);
      setInput("");
    }
  };

  const isDisabled = input.trim() === "";

  return (
    <form onSubmit={handleSubmit} className="chat-input-form">
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask about your data..."
        className="chat-input"
      />
      <button
        type="submit"
        className={`chat-submit-button ${isDisabled ? "disabled" : ""}`}
        disabled={isDisabled}
      >
        Send
      </button>
    </form>
  );
}

export default ChatInput;
