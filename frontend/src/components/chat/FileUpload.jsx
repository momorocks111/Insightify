import React, { useState } from "react";
import { useChat } from "../../contexts/ChatContext";
import axios from "axios";

function FileUpload() {
  const { setSelectedFile, currentChat } = useChat();
  const [loading, setLoading] = useState(false);
  const [buttonText, setButtonText] = useState("Upload CSV/Excel");

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setButtonText(file.name);
    setSelectedFile(file);
  };

  return (
    <div className="file-upload">
      <input
        type="file"
        id="file-upload-input"
        accept=".csv,.xlsx,.sql,.db,.sqlite"
        onChange={handleFileChange}
        disabled={loading}
        style={{ display: "none" }}
      />

      <label htmlFor="file-upload-input" className="file-upload-label">
        {buttonText}
      </label>
    </div>
  );
}

export default FileUpload;
