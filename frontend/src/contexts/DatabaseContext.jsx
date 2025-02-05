import react, { createContext, useContext, useState } from "react";

const DatabaseContext = createContext();

export const DatabaseProvider = ({ children }) => {
  const [databaseFile, setDatabaseFile] = useState(null);
  const [databaseSchema, setDatabaseSchema] = useState(null);

  const value = {
    databaseFile,
    setDatabaseFile,
    databaseSchema,
    setDatabaseSchema,
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
