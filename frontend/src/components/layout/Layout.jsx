import React from "react";
import Sidebar from "../Sidebar/Sidebar";
import "../../css/Layout.css";

function Layout({ children }) {
  return (
    <div className="layout">
      <Sidebar />
      <main className="main-content">{children}</main>
    </div>
  );
}

export default Layout;
