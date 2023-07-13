import { useState } from "react";
import { useNavigate } from "react-router-dom";

const FormParsing = () => {
  const [grammar, setGrammar] = useState("S->id.");
  const [parsingType, setParsingType] = useState("slr1");
  const [inputTape, setInputTape] = useState("id");

  const navigate = useNavigate();

  const handleSubmit = (event: any) => {
    event.preventDefault();

    navigate("/bottom-up",
      {
        state: {
          grammar: grammar,
          parsingType: parsingType,
          inputTape: inputTape,
        }
      });
  };

  return (
    <nav className="container my-3">
      <div className="card">
        <div className="card-header"><h4>Analisar gramática</h4></div>
        <form action="#" onSubmit={handleSubmit}>
          <div className="row m-2 ">
            <div className="col-md-6 my-3">
              <label htmlFor="grammarInput mt-3" className="form-label">Gramatica</label>
              <textarea
                className="form-control mb-3"
                id="grammarInput"
                rows={6}
                required
                onChange={(event) => setGrammar(event.target.value)}
                value={grammar}
              />
            </div>
            <div className="col-md-6 my-3">
              <label htmlFor="inputTape mt-3" className="form-label">Fita de entrada</label>
              <input
                type="text"
                className="form-control mb-3"
                id="inputTape"
                aria-describedby="inputTape"
                required
                onChange={(event) => setInputTape(event.target.value)}
                value={inputTape}
              />

              <label htmlFor="algorithmType" className="form-label">Tipo de algoritmo</label>
              <select
                className="form-select mb-3"
                id="algorithmType"
                aria-label="algorithmType"
                required
                onChange={(event) => setParsingType(event.target.value)}
                value={parsingType}
              >
                <option value="slr1">SLR</option>
              </select>

              <button type="submit" className="btn btn-primary mb-3">Analisar</button>
            </div>
          </div>
        </form>
      </div>
    </nav>
  );
}

export default FormParsing