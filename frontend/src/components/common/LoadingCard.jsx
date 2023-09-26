import React from "react";
import HelpCard from "../common/HelpCard";

const LoadingCard = ({ message }) => {
  return (
    <div className="row">
      <div className="col-md-6">
        <div className="loader"></div>
      </div>
      <div className="col-md-6">
        <HelpCard
          title={"Um momento! A entrada está sendo analisada!"}
          message={
            "Pequena explicação sobre o funcionamento da analise Bottom-Up"
          }
          message_button={"Saiba mais"}
          url={"https://www.google.com.br/?hl=pt-BR"}
        />
      </div>
    </div>
  );
};

export default LoadingCard;
