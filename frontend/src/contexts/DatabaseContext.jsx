import react, { createContext, useContext, useState } from "react";

const DatabaseContext = createContext();

export const DatabaseProvider = ({ children }) => {
  const [databaseFile, setDatabaseFile] = useState(null);
  const [databaseSchema, setDatabaseSchema] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const value = {
    databaseFile,
    setDatabaseFile,
    databaseSchema,
    setDatabaseSchema,
    isLoading,
    setIsLoading,
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
    throw new error(
      "useDatabaseContext must be used within a DatabaseProvider"
    );
  }

  return context;
};
