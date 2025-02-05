import React from "react";
import { useDatabaseContext } from "../../contexts/DatabaseContext";

const TablesList = ({ onSelectTable }) => {
  const { databaseSchema } = useDatabaseContext();

  const renderTables = () => {
    if (Array.isArray(databaseSchema)) {
      // SQL statements
      return databaseSchema
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
    } else if (databaseSchema.tables) {
      // SQLite database
      return Object.keys(databaseSchema.tables).map((tableName) => (
        <li
          key={tableName}
          className="tables-list__item"
          onClick={() => onSelectTable(tableName)}
        >
          {tableName}
        </li>
      ));
    } else {
      // Single table (CSV/Excel)
      return (
        <li className="tables-list__item" onClick={() => onSelectTable("data")}>
          Data
        </li>
      );
    }
  };

  return (
    <div className="tables-list">
      <h2 className="tables-list__title">Database Tables</h2>
      <ul className="tables-list__items">{renderTables()}</ul>
    </div>
  );
};

export default TablesList;
