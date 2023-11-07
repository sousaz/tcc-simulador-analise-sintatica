import { Outlet } from "react-router-dom";

import "intro.js/introjs.css";
import "./index.css";

import Header from "./components/common/Header";

const App = () => {
  return (
    <>
      <Header />
      <Outlet />
    </>
  );
};

export default App;
