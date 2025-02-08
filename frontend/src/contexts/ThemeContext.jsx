import React, { createContext, useContext, useState, useEffect } from "react";
import { themes } from "../services/themes";

const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  const [currentTheme, setCurrentTheme] = useState(() => {
    // Get the theme from local storage on initial load
    const savedTheme = localStorage.getItem("theme") || "dark";
    return savedTheme;
  });

  useEffect(() => {
    // Apply the theme whenever currentTheme changes
    const theme = themes.find((t) => t.id === currentTheme);
    if (theme) {
      Object.entries(theme.variables).forEach(([key, value]) => {
        document.documentElement.style.setProperty(key, value);
      });
      localStorage.setItem("theme", currentTheme);
    }
  }, [currentTheme]);

  const value = {
    currentTheme,
    setCurrentTheme,
  };

  return (
    <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>
  );
}

export function useTheme() {
  return useContext(ThemeContext);
}
