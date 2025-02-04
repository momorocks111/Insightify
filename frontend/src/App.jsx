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
        <Routes>
          <Route
            path="/"
            element={
              <Layout>
                <Home />
              </Layout>
            }
          />
          <Route
            path="/chat/"
            element={
              <Layout>
                <Chat />
              </Layout>
            }
          />
          <Route
            path="/chat/:chatId"
            element={
              <Layout>
                <Chat />
              </Layout>
            }
          />
          <Route
            path="/analysis"
            element={
              <Layout>
                <Analysis />
              </Layout>
            }
          />
        </Routes>
      </ChatProvider>
    </Router>
  );
}

export default App;
