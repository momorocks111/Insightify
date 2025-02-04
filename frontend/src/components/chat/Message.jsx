import React from "react";
import ReactMarkdown from "react-markdown";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { tomorrow } from "react-syntax-highlighter/dist/esm/styles/prism";

const Message = ({ message }) => {
  return (
    <div className={`message ${message.sender}-message`}>
      <div className="message-content">
        <ReactMarkdown
          children={message.content}
          components={{
            code({ node, inline, className, children, ...props }) {
              const match = /language-(\w+)/.exec(className || "");
              return !inline && match ? (
                <SyntaxHighlighter
                  children={String(children).replace(/\n$/, "")}
                  style={tomorrow}
                  language={match[1]}
                  PreTag="div"
                  {...props}
                />
              ) : (
                <code className={className} {...props}>
                  {children}
                </code>
              );
            },
          }}
        />
      </div>
      {message.fileInfo && (
        <div className="file-info">
          <p>File: {message.fileInfo.filename}</p>
          <p>Rows: {message.fileInfo.rows}</p>
          <p>Columns: {message.fileInfo.columns}</p>
        </div>
      )}
      <div className="message-timestamp">
        {new Date(message.timestamp).toLocaleTimeString()}
      </div>
    </div>
  );
};

export default Message;
