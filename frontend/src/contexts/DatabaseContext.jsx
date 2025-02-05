import React, { createContext, useContext, useState } from "react";

const DatabaseContext = createContext();

export const DatabaseProvider = ({ children }) => {
  const [databaseFile, setDatabaseFile] = useState(null);
  const [databaseSchema, setDatabaseSchema] = useState(null);
  const [fileInfo, setFileInfo] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [uploadProgress, setUploadProgress] = useState(0);

  const fetchDatabaseAnalysis = async (file) => {
    setIsLoading(true);
    setError(null);
    setUploadProgress(0);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:5000/api/database_analysis",
        {
          method: "POST",
          body: formData,
        }
      );

      if (!response.ok) {
        throw new Error("Failed to upload file");
      }

      const data = await response.json();
      setFileInfo(data.file_info);
      setDatabaseSchema(data.file_info.analysis);
      setIsLoading(false);
      return data;
    } catch (error) {
      setError(error.message);
      setIsLoading(false);
      throw error;
    }
  };

  const value = {
    databaseFile,
    setDatabaseFile,
    databaseSchema,
    setDatabaseSchema,
    fileInfo,
    setFileInfo,
    isLoading,
    setIsLoading,
    error,
    setError,
    uploadProgress,
    setUploadProgress,
    fetchDatabaseAnalysis,
  };

  return (
    <DatabaseContext.Provider value={value}>
      {children}
    </DatabaseContext.Provider>
  );
};

export const useDatabaseContext = () => {
  const context = useContext(DatabaseContext);
  if (!context) {
    throw new Error(
      "useDatabaseContext must be used within a DatabaseProvider"
    );
  }
  return context;
};
