import { Link } from "react-router-dom";

const CardError = ({ message }) => {
  return (
    <div className="container">
      <div className="card text-white bg-danger mb-3">
        <div className="card-header">Houve um erro inesperado.</div>
        <div className="card-body">
          <p className="card-text">{message}</p>
          <Link to="/" className="link-light">
            Clique aqui para voltar ao início...
          </Link>
        </div>
      </div>
    </div>
  );
};

export default CardError;
