import { useEffect } from 'react'
import { useLocation } from 'react-router-dom'
import axios from 'axios'

const AnlBottomUp = () => {
  const location = useLocation();

  useEffect(() => {
    console.log('INICIO');
  }, []);

  return (
    <>
      <h1>Bottom UP - {location.state['inputTape']} - {location.state['grammar']} - {location.state['parsingType']}</h1>
    </>
  )
}

export default AnlBottomUp