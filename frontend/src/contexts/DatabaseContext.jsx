import React, { createContext, useContext, useState } from "react";

const DatabaseContext = createContext();

export const DatabaseProvider = ({ children }) => {
  const [databaseFile, setDatabaseFile] = useState(null);
  const [databaseSchema, setDatabaseSchema] = useState(null);
  const [fileInfo, setFileInfo] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [uploadProgress, setUploadProgress] = useState(0);

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
