import React from "react";
import { useChat } from "../../contexts/ChatContext";

function FileUpload() {
  const { uploadFile } = useChat();

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      uploadFile(file);
    }
  };

  return (
    <div className="file-upload">
      <input
        type="file"
        onChange={handleFileUpload}
        accept=".csv,.xlsx,.json,.sql"
        id="file-upload"
        className="file-upload-input"
      />
      <label htmlFor="file-upload" className="file-upload-label">
        Upload Data File
      </label>
    </div>
  );
}

export default FileUpload;
