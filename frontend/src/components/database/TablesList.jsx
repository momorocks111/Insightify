import React from "react";
import { useDatabaseContext } from "../../contexts/DatabaseContext";

const TablesList = ({ onSelectTable }) => {
  const { fileInfo } = useDatabaseContext();

  const renderTables = () => {
    if (!fileInfo || !fileInfo.analysis) return null;

    const { type, analysis } = fileInfo;

    if (type === "list" && Array.isArray(analysis)) {
      // SQL statements
      return analysis
        .filter((stmt) => stmt.type === "CREATE")
        .map((stmt) => (
          <li
            key={stmt.table}
            className="tables-list__item"
            onClick={() => onSelectTable(stmt.table)}
          >
            {stmt.table}
          </li>
        ));
    } else if (type === "dict" && analysis.tables) {
      // SQLite database
      return Object.keys(analysis.tables).map((tableName) => (
        <li
          key={tableName}
          className="tables-list__item"
          onClick={() => onSelectTable(tableName)}
        >
          {tableName}
        </li>
      ));
    } else if (type === "DataFrame") {
      // Single table (CSV/Excel)
      return (
        <li className="tables-list__item" onClick={() => onSelectTable("data")}>
          Data
        </li>
      );
    }

    return null;
  };

  return (
    <div className="tables-list">
      <h2 className="tables-list__title">Database Tables</h2>
      <ul className="tables-list__items">{renderTables()}</ul>
    </div>
  );
};

export default TablesList;
