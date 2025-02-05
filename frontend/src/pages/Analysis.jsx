import React, { useState } from "react";
import FileUpload from "../components/database/FileUpload";
import DatabaseInfo from "../components/database/DatabaseInfo";
import { DatabaseProvider } from "../contexts/DatabaseContext";

const Analysis = () => {
  const [fileUploaded, setFileUploaded] = useState(false);

  return (
    <DatabaseProvider>
      <div className="database-analysis">
        <h1 className="database-analysis__title">Database Analysis</h1>
        {!fileUploaded ? (
          <FileUpload onFileUpload={() => setFileUploaded(true)} />
        ) : (
          <DatabaseInfo />
        )}
      </div>
    </DatabaseProvider>
  );
};

export default Analysis;
