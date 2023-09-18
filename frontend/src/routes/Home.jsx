import CardInfo from "../components/common/CardInfo";
import FormParsing from "../components/home/FormParsing";

const Home = () => {
  return (
    <>
      <CardInfo
        message={
          "Bem-vindo ao SASC - Simulador de análise sintática em compiladores."
        }
      />
      <FormParsing />
    </>
  );
};

export default Home;
