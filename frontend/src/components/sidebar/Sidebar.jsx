import React from "react";
import { Link } from "react-router-dom";
import ChatList from "./ChatList";
import NewChatButton from "./NewChatButton";

function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <h2 className="sidebar-title">Insightify</h2>
      </div>
      <nav className="sidebar-nav">
        <ul className="sidebar-nav-list">
          <li className="sidebar-nav-item">
            <Link to="/" className="sidebar-nav-link">
              Home
            </Link>
          </li>
          <li className="sidebar-nav-item">
            <Link to="/chat" className="sidebar-nav-link">
              Chat
            </Link>
          </li>
          <li className="sidebar-nav-item">
            <Link to="/analysis" className="sidebar-nav-link">
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
