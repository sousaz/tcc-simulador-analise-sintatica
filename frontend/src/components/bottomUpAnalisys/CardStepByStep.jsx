const CardStepByStep = ({ stepByStep, stepCont, setStepCont, qtSteps }) => {
  return (
    <div className="border border-primary px-3 pb-3 mb-3 stack-card">
      <h4 className="mt-3 border-bottom border-primary">Passo a passo</h4>
      <div className="vstack gap-3">
        {stepByStep.map((element, index) => (
          <div className="bg-primary-subtle p-2" key={index}>
            {element}
          </div>
        ))}
      </div>
      <div className="mt-3 pt-3 px-2 border-top border-primary btn-group step-buttons">
        <button
          className="btn btn-primary"
          disabled={stepCont <= 0}
          type="button"
          onClick={() => setStepCont((prevState) => prevState - 1)}
        >
          Anterior
        </button>
        <button
          className="btn btn-success"
          disabled={stepCont >= qtSteps}
          type="button"
          onClick={() => setStepCont((prevState) => prevState + 1)}
        >
          Próximo
        </button>
      </div>
    </div>
  );
};

export default CardStepByStep;
