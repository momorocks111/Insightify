import React, { useState } from "react";
import TablesList from "./TablesList";
import TableDetails from "./TableDetails";
import SchemaVisualization from "./SchemaVisualization";
import { useDatabaseContext } from "../../contexts/DatabaseContext";

const DatabaseInfo = () => {
  const [activeTab, setActiveTab] = useState("tables");
  const [selectedTable, setSelectedTable] = useState(null);
  const { databaseSchema } = useDatabaseContext();

  const renderContent = () => {
    switch (activeTab) {
      case "tables":
        return <TablesList onSelectTable={setSelectedTable} />;
      case "details":
        return selectedTable ? (
          <TableDetails tableName={selectedTable} />
        ) : (
          <p>Select a table to view details</p>
        );
      case "schema":
        return <SchemaVisualization />;
      default:
        return null;
    }
  };

  return (
    <div className="database-info">
      <nav className="database-info__nav">
        <button
          className={`database-info__nav-btn ${
            activeTab === "tables" ? "active" : ""
          }`}
          onClick={() => setActiveTab("tables")}
        >
          Tables
        </button>
        <button
          className={`database-info__nav-btn ${
            activeTab === "details" ? "active" : ""
          }`}
          onClick={() => setActiveTab("details")}
        >
          Table Details
        </button>
        <button
          className={`database-info__nav-btn ${
            activeTab === "schema" ? "active" : ""
          }`}
          onClick={() => setActiveTab("schema")}
        >
          Schema Visualization
        </button>
      </nav>
      <div className="database-info__content">
        {databaseSchema ? (
          renderContent()
        ) : (
          <p className="database-info__loading">
            Loading database information...
          </p>
        )}
      </div>
    </div>
  );
};

export default DatabaseInfo;
