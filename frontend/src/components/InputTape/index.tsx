import '../InputTape/index.css'

const InputTape = (props: any) => {
  return (
    <div className='border border-primary px-3 pb-3'>
      <h4 className='mt-3 border-bottom border-primary '>Fita de entrada</h4>
      <div className="hstack gap-3">
        {props["inputTape"].map((element: any, index: number) => {
          if (props["pointer"] == index)
            return <div>
                      <div className="bg-info p-2 tape-element pointed" key={index}>{element}</div>
                      <div className='arrow'></div>
                    </div>;
          return <div className="bg-info p-2 tape-element" key={index}>{element}</div>;
        })}
      </div>
    </div>
  )
}

export default InputTape