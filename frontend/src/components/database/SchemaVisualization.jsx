import React, { useCallback } from "react";
import ReactFlow, { Background, Controls } from "reactflow";
import "reactflow/dist/style.css";
import { useDatabaseContext } from "../../contexts/DatabaseContext";

const SchemaVisualization = () => {
  const { fileInfo } = useDatabaseContext();

  const generateNodes = useCallback(() => {
    if (!fileInfo || !fileInfo.analysis || !fileInfo.analysis.tables) return [];

    return fileInfo.analysis.tables.map((table, index) => ({
      id: table.name,
      data: { label: table.name, columns: table.columns },
      position: { x: 250 * index, y: 0 },
      type: "tableNode",
    }));
  }, [fileInfo]);

  const nodeTypes = {
    tableNode: TableNode,
  };

  return (
    <div style={{ height: "500px", width: "100%" }}>
      <ReactFlow nodes={generateNodes()} nodeTypes={nodeTypes} fitView>
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  );
};

const TableNode = ({ data }) => (
  <div
    style={{
      padding: "10px",
      border: "1px solid #ddd",
      borderRadius: "5px",
      background: "white",
    }}
  >
    <h3>{data.label}</h3>
    <ul style={{ listStyleType: "none", padding: 0 }}>
      {data.columns.map((column, index) => (
        <li key={index}>
          {column.name}: {column.type}
        </li>
      ))}
    </ul>
  </div>
);

export default SchemaVisualization;
