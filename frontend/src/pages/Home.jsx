import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="home-container">
      <header className="home-header">
        <h1 className="home-title">Welcome to Insightify</h1>
        <p className="home-subtitle">Your AI-powered data navigator</p>
      </header>

      <section className="home-cta">
        <Link to="/chat" className="home-cta-button home-cta-button--primary">
          Start Chatting
        </Link>
        <Link
          to="/analysis"
          className="home-cta-button home-cta-button--secondary"
        >
          Analyze Data
        </Link>
      </section>

      <section className="home-features">
        <h2 className="home-features-title">Key Features</h2>
        <ul className="home-features-list">
          <li className="home-features-item">
            Analyze CSV, Excel, and database files
          </li>
          <li className="home-features-item">AI-powered data insights</li>
          <li className="home-features-item">Interactive chat interface</li>
          <li className="home-features-item">Visualize your data</li>
        </ul>
      </section>

      <section className="home-how-it-works">
        <h2 className="home-section-title">How It Works</h2>
        <ol className="home-steps-list">
          <li className="home-steps-item">Upload your data files</li>
          <li className="home-steps-item">Ask questions about your data</li>
          <li className="home-steps-item">
            Receive AI-powered insights and visualizations
          </li>
          <li className="home-steps-item">
            Explore and analyze your data interactively
          </li>
        </ol>
      </section>

      <section className="home-use-cases">
        <h2 className="home-section-title">Use Cases</h2>
        <ul className="home-use-cases-list">
          <li className="home-use-cases-item">Business Intelligence</li>
          <li className="home-use-cases-item">Scientific Research</li>
          <li className="home-use-cases-item">Financial Analysis</li>
          <li className="home-use-cases-item">Market Research</li>
        </ul>
      </section>
    </div>
  );
}

export default Home;
