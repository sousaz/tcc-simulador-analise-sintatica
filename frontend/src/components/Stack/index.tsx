import { useEffect, useState } from "react";

import '../Stack/index.css'

const StackParsing = (props: any) => {
  const [stack, setStack] = useState([]);

  useEffect(() => {
    let aux = props["stack"].reverse()
    console.log(aux)
    setStack(aux)
  }, [props["stack"]]);

  return (
    <div className="border border-primary px-3 pb-3 mb-3 stack-card">
      <h4 className='mt-3 border-bottom border-primary'>Pilha</h4>
      <div className="vstack gap-3">
        {props["stack"].reverse().map((element: any) => (
          <div className="bg-secondary border p-2 stack-element">{element}</div>
        ))}
      </div>
    </div>
  )
}

export default StackParsing