import React from "react";
import { useDatabaseContext } from "../../contexts/DatabaseContext";

const TablesList = () => {
  const { databaseSchema } = useDatabaseContext();

  return (
    <div className="tables-list">
      <h2 className="tables-list__title">Database Tables</h2>
      <ul className="tables-list__items">
        {Object.keys(databaseSchema).map((tableName) => (
          <li
            key={tableName}
            className="tables-list__item"
            onClick={() => onSelectTable(tableName)}
          >
            {tableName}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TablesList;
