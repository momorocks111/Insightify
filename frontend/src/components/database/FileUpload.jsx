import React, { useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { useDatabaseContext } from "../../contexts/DatabaseContext";
import { CircularProgressbar } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

const FileUpload = ({ onFileUpload }) => {
  const {
    setDatabaseSchema,
    setFileInfo,
    setIsLoading,
    setError,
    uploadProgress,
    setUploadProgress,
  } = useDatabaseContext();

  const onDrop = useCallback(
    async (acceptedFiles) => {
      const file = acceptedFiles[0];
      if (file) {
        const formData = new FormData();
        formData.append("file", file);
        try {
          setIsLoading(true);
          setError(null);
          setUploadProgress(0);

          const xhr = new XMLHttpRequest();
          xhr.open("POST", "http://127.0.0.1:5000/api/database_analysis");

          xhr.upload.onprogress = (event) => {
            if (event.lengthComputable) {
              const percentComplete = (event.loaded / event.total) * 100;
              setUploadProgress(percentComplete);
            }
          };

          xhr.onload = () => {
            if (xhr.status === 200) {
              const data = JSON.parse(xhr.responseText);
              setFileInfo(data.file_info);
              setDatabaseSchema(data.file_info.analysis);
              onFileUpload();
            } else {
              setError("An error occurred while uploading the file.");
            }
            setIsLoading(false);
          };

          xhr.onerror = () => {
            console.error("Error uploading file");
            setError("Failed to upload file. Please try again.");
            setIsLoading(false);
          };

          xhr.send(formData);
        } catch (error) {
          console.error("Error uploading file:", error);
          setError("Failed to upload file. Please try again.");
          setIsLoading(false);
        }
      }
    },
    [
      setDatabaseSchema,
      setFileInfo,
      setIsLoading,
      setError,
      setUploadProgress,
      onFileUpload,
    ]
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
