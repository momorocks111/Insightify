import React, { useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { useDatabaseContext } from "../../contexts/DatabaseContext";

const FileUpload = ({ onFileUpload }) => {
  const { setDatabaseFile } = useDatabaseContext();

  const onDrop = useCallback(
    (acceptedFiles) => {
      const file = acceptedFiles[0];
      const validExtensions = [".db", ".sql", ".sqlite", ".mdb", ".accdb"];
      const fileExtension = file.name
        .substring(file.name.lastIndexOf("."))
        .toLowerCase();

      if (file && validExtensions.includes(fileExtension)) {
        setDatabaseFile(file);
        onFileUpload();
      } else {
        alert(
          "Please upload a valid database file (.db, .sql, .sqlite, .mdb, .accdb)"
        );
      }
    },
    [setDatabaseFile, onFileUpload]
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
