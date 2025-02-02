import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import "./App.css";
import Home from "./pages/Home";
import DataUpload from "./pages/DataUpload";
import Analysis from "./pages/Analysis";
import Chat from "./pages/Chat";
import ThemeToggle from "./components/ThemeToggle";

function App() {
  return (
    <Router>
      <div className="container">
        <ThemeToggle />
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/upload">Upload Data</Link>
            </li>
            <li>
              <Link to="/analysis">Analysis</Link>
            </li>
            <li>
              <Link to="/chat">Chat</Link>
            </li>
          </ul>
        </nav>

        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/upload" element={<DataUpload />} />
            <Route path="/analysis" element={<Analysis />} />
            <Route path="/chat" element={<Chat />} />
          </Routes>
        </main>

        <footer>
          <p>&copy; 2025 Insightify. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
