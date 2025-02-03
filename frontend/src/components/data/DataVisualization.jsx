import React from "react";
import { useChat } from "../../contexts/ChatContext";

const DataVisualization = () => {
  const { currentChat } = useChat();

  // This component will render different visualizations based on the current chat's data
  return (
    <div className="data-visualization">
      <h2>Data Visualization</h2>
      {/* Render charts, graphs, or tables based on currentChat.data */}
    </div>
  );
};

export default DataVisualization;
