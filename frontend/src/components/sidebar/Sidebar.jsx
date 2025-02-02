import React from "react";
import { Link } from "react-router-dom";
import ChatList from "./ChatList";
import NewChatButton from "./NewChatButton";

function Sidebar() {
  return (
    <aside className="sidebar">
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/chat">Chat</Link>
          </li>
          <li>
            <Link to="/analysis">Analysis</Link>
          </li>
        </ul>
      </nav>
      <NewChatButton />
      <ChatList />
    </aside>
  );
}

export default Sidebar;
