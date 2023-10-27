import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

import { getAllData } from "../services/ParsingService";

import TableBottomUp from "../components/bottomUpAnalisys/TableBottomUp";
import Stack from "../components/bottomUpAnalisys/Stack";
import InputTape from "../components/bottomUpAnalisys/InputTape";
import CardStepByStep from "../components/bottomUpAnalisys/CardStepByStep";
import CardGrammar from "../components/bottomUpAnalisys/CardGrammar";
import LoadingCard from "../components/common/LoadingCard";

const BottomUpAnalisys = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const [stepCont, setStepCont] = useState(0);
  const [loading, setLoading] = useState(true);
  const [parsingTable, setParsingTable] = useState({});
  const [steps, setSteps] = useState([]);
  const [grammar, setGrammar] = useState([]);

  useEffect(() => {
    getAllData(
      location.state["grammar"],
      location.state["inputTape"],
      location.state["parsingType"]
    )
      .then((response) => {
        if (response.data["ERROR_CODE"] == 0) {
          setLoading(false);
          setGrammar(response.data["grammar"]);
          setSteps(response.data["stepsParsing"]);
          setParsingTable(response.data["parsingTable"]);
        } else {
          navigate("/error", {
            state: {
              message: response.data["errorMessage"],
            },
          });
        }
      })
      .catch((error) => console.error(error));
  }, []);

  return (
    <div className="container">
      {loading ? (
        <LoadingCard message={"Carregando dados para analise."} />
      ) : (
        <div className="row">
          <div className="col-md-6">
            <div className="row">
              <div className="col-md-9">
                <CardStepByStep
                  stepCont={stepCont}
                  setStepCont={setStepCont}
                  stepByStep={steps[stepCont]["stepByStep"]}
                  qtSteps={steps.length - 1}
                />
                <CardGrammar grammar={grammar} />
              </div>
              <div className="col-md-3">
                <Stack stack={steps[stepCont]["stack"]} />
              </div>
            </div>
          </div>
          <div className="col-md-6">
            <InputTape
              inputTape={steps[0]["input"]}
              pointer={steps[stepCont]["pointer"]}
            />
            <TableBottomUp
              parsingTable={parsingTable}
              stepMarker={steps[stepCont]["stepMarker"]}
            />
          </div>
        </div>
      )}
    </div>
  );
};

export default BottomUpAnalisys;
