import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="home">
      <h1>Welcome to Insightify</h1>
      <p>Your AI-powered data navigator</p>
      <div className="cta-buttons">
        <Link to="/chat" className="btn btn-primary">
          Start Chatting
        </Link>
        <Link to="/analysis" className="btn btn-secondary">
          Analyze Data
        </Link>
      </div>
      <section className="features">
        <h2>Key Features</h2>
        <ul>
          <li>Analyze CSV, Excel, and database files</li>
          <li>AI-powered data insights</li>
          <li>Interactive chat interface</li>
          <li>Visualize your data</li>
        </ul>
      </section>
    </div>
  );
}

export default Home;
