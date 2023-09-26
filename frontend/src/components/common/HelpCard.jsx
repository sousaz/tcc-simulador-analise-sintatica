import React from "react";

const HelpCard = ({ title, message, message_button, url }) => {
  return (
    <div className="card">
      <div className="card-header">{title}</div>
      <div className="card-body">
        <p className="card-text">{message}</p>
        <a href={url} className="btn btn-primary" target="_blank">
          {message_button}
        </a>
      </div>
    </div>
  );
};

export default HelpCard;
