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

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask about your data..."
      />
      <button type="submit">Send</button>
    </form>
  );
}

export default ChatInput;
