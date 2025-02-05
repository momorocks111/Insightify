import React, { useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { useDatabaseContext } from "../../contexts/DatabaseContext";
import { CircularProgressbar } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

const FileUpload = ({ onFileUpload }) => {
  const { fetchDatabaseAnalysis, setError, uploadProgress, setUploadProgress } =
    useDatabaseContext();

  const onDrop = useCallback(
    async (acceptedFiles) => {
      const file = acceptedFiles[0];
      if (file) {
        try {
          await fetchDatabaseAnalysis(file);
          onFileUpload();
        } catch (error) {
          console.error("Error uploading file:", error);
          setError("Failed to upload file. Please try again.");
        }
      }
    },
    [fetchDatabaseAnalysis, setError, onFileUpload]
  );

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div {...getRootProps()} className="file-upload dashed-line">
      <input {...getInputProps()} />
      <div className="file-upload__content">
        {uploadProgress > 0 && uploadProgress < 100 ? (
          <div style={{ width: "200px", height: "200px" }}>
            <CircularProgressbar
              value={uploadProgress}
              text={`${Math.round(uploadProgress)}%`}
            />
          </div>
        ) : isDragActive ? (
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
