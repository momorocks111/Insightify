import React from "react";
import { useChat } from "../../contexts/ChatContext";

function FileUpload() {
  const { sendMessage } = useChat();

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      sendMessage(null, file);
    }
  };

  return (
    <div className="file-upload">
      <input
        type="file"
        onChange={handleFileUpload}
        accept=".csv,.xlsx,.json,.sql"
      />
    </div>
  );
}

export default FileUpload;
