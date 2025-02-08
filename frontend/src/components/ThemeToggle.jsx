import React, { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPalette } from "@fortawesome/free-solid-svg-icons";
import { useTheme } from "../contexts/ThemeContext";
import ThemeModal from "./ThemeModal";

function ThemeToggle() {
  const { currentTheme, setCurrentTheme } = useTheme();
  const [isModalOpen, setIsModalOpen] = useState(false);

  const openModal = () => setIsModalOpen(true);
  const closeModal = () => setIsModalOpen(false);

  const handleSelectTheme = (themeId) => {
    setCurrentTheme(themeId);
    closeModal();
  };

  return (
    <>
      <button onClick={openModal} className="theme-toggle">
        <FontAwesomeIcon icon={faPalette} />
        <span className="sr-only">Change Theme</span>
      </button>
      <ThemeModal
        isOpen={isModalOpen}
        onClose={closeModal}
        onSelectTheme={handleSelectTheme}
        currentTheme={currentTheme}
      />
    </>
  );
}

export default ThemeToggle;
