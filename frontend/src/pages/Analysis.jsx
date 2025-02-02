import React from "react";
import Chart from "../components/data/Chart";

const Analysis = () => {
  return (
    <div className="analysis-page">
      <h1>Data Analysis</h1>
      <Chart />
      <p>Select a dataset to analyze or upload a new one.</p>
    </div>
  );
};

export default Analysis;
