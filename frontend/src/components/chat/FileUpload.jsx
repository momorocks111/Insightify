import React, { useState } from "react";
import { useChat } from "../../contexts/ChatContext";
import axios from "axios";

function FileUpload() {
  const { uploadFile, currentChat } = useChat(); // Add currentChat here
  const [loading, setLoading] = useState(false);
  const [buttonText, setButtonText] = useState("Upload CSV/Excel");

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setLoading(true);
    setButtonText("Uploading...");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("chat_id", currentChat.id); // Now currentChat is defined

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/api/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      // Notify the user of successful upload
      uploadFile(file.name);
      alert(response.data.message);
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("Failed to upload file.");
    } finally {
      setLoading(false);
      setButtonText("Upload CSV/Excel");
    }
  };

  return (
    <div className="file-upload">
      <input
        type="file"
        id="file-upload-input"
        accept=".csv,.xlsx"
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
