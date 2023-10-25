import { useLocation } from "react-router-dom";

import CardInfo from "../components/common/CardInfo";

const Error = (message) => {
  const location = useLocation();

  return (
    <>
      <CardInfo message={location.state["message"]} />
    </>
  );
};

export default Error;
