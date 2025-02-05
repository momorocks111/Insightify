import React from "react";
import { useDatabaseContext } from "../../contexts/DatabaseContext";

const TableDetails = ({ tableName }) => {
  const { databaseSchema } = useDatabaseContext();
  const tableInfo = databaseSchema[tableName];

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
        <tbody>
          {tableInfo.columns.map((column) => (
            <tr key={column.name}>
              <td>{column.name}</td>
              <td>{column.type}</td>
              <td>{column.constraints.join(", ")}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TableDetails;
