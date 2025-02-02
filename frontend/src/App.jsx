import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout/Layout";
import Home from "./pages/Home";
import Chat from "./pages/Chat";
import Analysis from "./pages/Analysis";
import { ChatProvider } from "./contexts/ChatContext";

function App() {
  return (
    <Router>
      <ChatProvider>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/chat/:id?" element={<Chat />} />
            <Route path="/analysis" element={<Analysis />} />
          </Routes>
        </Layout>
      </ChatProvider>
    </Router>
  );
}

export default App;
