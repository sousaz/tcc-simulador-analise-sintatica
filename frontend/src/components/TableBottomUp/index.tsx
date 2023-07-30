import PlotTable from '../PlotTable'

const ParsingTable = (props: any) => {
    return (
        <div className='container'>
            <h4>Tabela de ações</h4>
            <PlotTable tableJson={props["parsingTable"]["action_table"]} stepMarker={props["stepMarker"]} className="m-3" />
            <h4>Tabela de transições</h4>
            <PlotTable tableJson={props["parsingTable"]["goto_table"]} stepMarker={props["stepMarker"]} className="m-3" />
        </div>
    )
}

export default ParsingTable