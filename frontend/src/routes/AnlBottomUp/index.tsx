import { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'

// @ts-ignore
import { getAllData } from '../../services/ParsingService'

import TableBottomUp from '../../components/TableBottomUp'
import Stack from '../../components/Stack'
import InputTape from '../../components/InputTape'
import CardStepByStep from '../../components/CardStepByStep'
import CardGrammar from '../../components/CardGrammar'

const AnlBottomUp = () => {
  const location = useLocation();

  const [stepCont, setStepCont] = useState(0);
  const [loading, setLoading] = useState(true);
  const [parsingTable, setParsingTable] = useState({});
  const [steps, setSteps] = useState([])

  useEffect(() => {
    getAllData(location.state['grammar'], location.state['inputTape'], location.state['parsingType'])
      .then((response: any) => {
        setLoading(false);
        console.log(response.data);

        setSteps(response.data['stepsParsing']);
        setParsingTable(response.data['parsingTable']);
      })
      .catch((error: any) => console.error(error))
  }, []);

  return (
    <div className="container">
      {loading ? <h1>Carregando...</h1> :
        <div className="row">

          <div className="col-md-6">
            <div className="row">
              <div className="col-md-9">
                <CardStepByStep stepCont={stepCont} setStepCont={setStepCont} />
                <CardGrammar />
              </div>
              <div className="col-md-3">
                <Stack stack={steps[stepCont]['stack']} />
              </div>
            </div>
          </div>
          <div className="col-md-6">
            <InputTape inputTape={steps[0]['input']} pointer={0} />
            <TableBottomUp parsingTable={parsingTable} stepMarker={["id", 0]} />
          </div>
        </div>
      }
    </div>
  )
}

export default AnlBottomUp