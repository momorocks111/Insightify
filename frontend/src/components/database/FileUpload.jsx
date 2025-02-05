import React, { useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { useDatabaseContext } from "../../contexts/DatabaseContext";

const FileUpload = ({ onFileUpload }) => {
  const { setDatabaseSchema } = useDatabaseContext();

  const onDrop = useCallback(
    async (acceptedFiles) => {
      const file = acceptedFiles[0];
      if (file) {
        const formData = new FormData();
        formData.append("file", file);
        try {
          const response = await fetch(
            "http://127.0.0.1:5000/api/analyze_with_file",
            {
              method: "POST",
              body: formData,
            }
          );
          const data = await response.json();
          setDatabaseSchema(data.file_info.analysis);
          onFileUpload();
        } catch (error) {
          console.error("Error uploading file:", error);
          alert("Failed to upload file.");
        }
      }
    },
    [setDatabaseSchema, onFileUpload]
  );

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div {...getRootProps()} className="file-upload">
      <input {...getInputProps()} />
      <div className="file-upload__content">
        {isDragActive ? (
          <p className="file-upload__text">Drop the database file here...</p>
        ) : (
          <p className="file-upload__text">
            Drag and drop a database file here, or click to select a file
          </p>
        )}
        <p className="file-upload__formats">
          Supported formats: .db, .sql, .sqlite, .mdb, .accdb
        </p>
      </div>
    </div>
  );
};

export default FileUpload;
