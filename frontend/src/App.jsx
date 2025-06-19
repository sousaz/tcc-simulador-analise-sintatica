import { Outlet } from "react-router-dom";

import "intro.js/introjs.css";
import "./index.css";

import Header from "./components/common/Header";
import Footer from "./components/common/Footer";
import GrammarProvider from "./context/GrammarContext";

const App = () => {
  return (
    <>
      <GrammarProvider>
        <Header />
        <Outlet />
        <Footer />
      </GrammarProvider>
    </>
  );
};

export default App;
