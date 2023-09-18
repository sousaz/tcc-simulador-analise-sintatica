import PlotTable from "../bottomUpAnalisys/PlotTable";

const ParsingTable = ({ parsingTable, stepMarker }) => {
  return (
    <div className="container">
      <h4>Tabela de ações</h4>
      <PlotTable
        tableJson={parsingTable["action_table"]}
        stepMarker={stepMarker}
        className="m-3"
      />
      <h4>Tabela de transições</h4>
      <PlotTable
        tableJson={parsingTable["goto_table"]}
        stepMarker={stepMarker}
        className="m-3"
      />
    </div>
  );
};

export default ParsingTable;
