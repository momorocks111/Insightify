import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { themes } from "../services/themes";

function ThemeModal({ isOpen, onClose, onSelectTheme, currentTheme }) {
  if (!isOpen) return null;

  return (
    <div className="theme-modal">
      <div className="theme-modal__overlay" onClick={onClose}></div>
      <div className="theme-modal__content">
        <h2 className="theme-modal__title">Select a Theme</h2>
        <div className="theme-modal__list">
          {themes.map((theme) => (
            <button
              key={theme.id}
              className={`theme-modal__item ${
                currentTheme === theme.id ? "theme-modal__item--active" : ""
              }`}
              onClick={() => onSelectTheme(theme.id)}
            >
              <FontAwesomeIcon
                icon={theme.icon}
                className="theme-modal__icon"
              />
              <span className="theme-modal__theme-name">{theme.name}</span>
            </button>
          ))}
        </div>
        <button className="theme-modal__close-btn" onClick={onClose}>
          Close
        </button>
      </div>
    </div>
  );
}

export default ThemeModal;
