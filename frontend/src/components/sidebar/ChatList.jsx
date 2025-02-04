import React from "react";
import { useNavigate, useParams } from "react-router-dom";
import { useChat } from "../../contexts/ChatContext";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash, faComment } from "@fortawesome/free-solid-svg-icons";

const ChatList = () => {
  const { chats, switchChat, deleteChat } = useChat();
  const navigate = useNavigate();
  const params = useParams();
  const activeChatId = params.chatId;

  const handleChatClick = (chatId) => {
    switchChat(chatId);
    navigate(`/chat/${chatId}`);
  };

  const handleDeleteClick = (e, chatId) => {
    e.stopPropagation();
    deleteChat(chatId);
  };

  const truncate = (str, n) => {
    return str.length > n ? str.substr(0, n - 1) + "..." : str;
  };

  return (
    <div className="chat-list">
      <h2 className="chat-list-title">Your Chats</h2>
      {chats.length === 0 ? (
        <p className="chat-list-empty">
          No chats yet. Start a new conversation!
        </p>
      ) : (
        <ul className="chat-list-items">
          {chats.map((chat) => (
            <li
              key={chat.id}
              className={`chat-list-item ${
                String(chat.id) === String(activeChatId) ? "active" : ""
              }`}
              onClick={() => handleChatClick(chat.id)}
            >
              <div className="chat-list-item-content">
                <FontAwesomeIcon icon={faComment} className="chat-icon" />
                <span className="chat-title">{truncate(chat.title, 25)}</span>
              </div>
              <button
                className="delete-button"
                onClick={(e) => handleDeleteClick(e, chat.id)}
                aria-label="Delete chat"
              >
                <FontAwesomeIcon icon={faTrash} className="delete-icon" />
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ChatList;
