import React from "react";
import { Link, useNavigate } from "react-router-dom";
import ChatList from "./ChatList";
import NewChatButton from "./NewChatButton";
import ThemeToggle from "../ThemeToggle";

function Sidebar({ isOpen, onClose }) {
  const navigate = useNavigate();

  const handleNavigation = (event, path) => {
    event.preventDefault();
    navigate(path);
    onClose();
  };

  return (
    <aside className={`sidebar ${isOpen ? "open" : ""}`}>
      <div className="sidebar-header">
        <h2 className="sidebar-title">Insightify</h2>
        <ThemeToggle />
      </div>
      <nav className="sidebar-nav">
        <ul className="sidebar-nav-list">
          <li className="sidebar-nav-item">
            <Link
              to="/"
              onClick={(e) => handleNavigation(e, "/")}
              className="sidebar-nav-link"
            >
              Home
            </Link>
          </li>
          <li className="sidebar-nav-item">
            <Link
              to="/chat"
              onClick={(e) => handleNavigation(e, "/chat")}
              className="sidebar-nav-link"
            >
              Chat
            </Link>
          </li>
          <li className="sidebar-nav-item">
            <Link
              to="/analysis"
              onClick={(e) => handleNavigation(e, "/analysis")}
              className="sidebar-nav-link"
            >
              Analysis
            </Link>
          </li>
        </ul>
      </nav>
      <div className="sidebar-actions">
        <NewChatButton />
      </div>
      <div className="sidebar-chats">
        <ChatList />
      </div>
    </aside>
  );
}

export default Sidebar;
