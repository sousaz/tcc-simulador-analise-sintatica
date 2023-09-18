import React from "react";

const LoadingCard = ({ message }) => {
  return (
    <div className="row">
      <div className="col-md-6">
        <div className="loader"></div>
      </div>
      <div className="col-md-6">{message}</div>
    </div>
  );
};

export default LoadingCard;
