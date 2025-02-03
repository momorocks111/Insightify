import React, { useState } from "react";
import Sidebar from "../sidebar/Sidebar";
import "../../css/Layout.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars } from "@fortawesome/free-solid-svg-icons";

function Layout({ children }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <div className={`layout ${sidebarOpen ? "sidebar-open" : ""}`}>
      <button className="sidebar-toggle" onClick={toggleSidebar}>
        <FontAwesomeIcon icon={faBars} />
      </button>
      <Sidebar isOpen={sidebarOpen} />
      <main className="main-content">{children}</main>
    </div>
  );
}

export default Layout;
