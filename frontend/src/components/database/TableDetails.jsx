import React from "react";
import { useDatabaseContext } from "../../contexts/DatabaseContext";

const TableDetails = ({ tableName }) => {
  const { fileInfo } = useDatabaseContext();

  if (!fileInfo || !fileInfo.analysis) return null;

  const { type, analysis } = fileInfo;

  let tableInfo;
  if (type === "list" && Array.isArray(analysis)) {
    tableInfo = analysis.find(
      (stmt) => stmt.type === "CREATE" && stmt.table === tableName
    );
  } else if (type === "dict" && analysis.tables) {
    tableInfo = analysis.tables[tableName];
  } else if (type === "DataFrame") {
    tableInfo = analysis;
  }

  if (!tableInfo) return <p>Table information not found.</p>;

  const renderColumns = () => {
    if (type === "list") {
      // Parse SQL CREATE statement to extract column info
      const columnRegex = /\((.+)\)/;
      const columnsMatch = tableInfo.columns.match(columnRegex);
      if (columnsMatch) {
        const columns = columnsMatch[1].split(",").map((col) => col.trim());
        return columns.map((col) => {
          const [name, ...rest] = col.split(" ");
          return (
            <tr key={name}>
              <td>{name}</td>
              <td>{rest.join(" ")}</td>
              <td></td>
            </tr>
          );
        });
      }
    } else if (type === "dict" || type === "DataFrame") {
      return Object.entries(tableInfo.dtypes).map(([name, dtype]) => (
        <tr key={name}>
          <td>{name}</td>
          <td>{dtype}</td>
          <td></td>
        </tr>
      ));
    }
    return null;
  };

  return (
    <div className="table-details">
      <h2 className="table-details__title">{tableName}</h2>
      <h3 className="table-details__subtitle">Columns</h3>
      <table className="table-details__info">
        <thead>
          <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Constraints</th>
          </tr>
        </thead>
        <tbody>{renderColumns()}</tbody>
      </table>
    </div>
  );
};

export default TableDetails;
