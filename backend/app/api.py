# Importacoes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar funcoes
from app import parsing_table
from app import parsing_algorithm
from app import utils

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://localhost:5173",
    "localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Testar API
@app.get("/test/")
async def read_root() -> dict:
    return {"message": "Testando api"}


@app.get("/analyze/{grammar}/{input}/{analysis_type}")
async def get_table(input: str, grammar: str, analysis_type: str):
    print("TESTE")
    new_grammar = utils.grammar_formatter(grammar)
    goto_action_tables = parsing_table.get_goto_action_tables(grammar, analysis_type)
    print(goto_action_tables)

    steps_parsing = parsing_algorithm.bottom_up_algorithm(
        goto_action_tables["action_table"], goto_action_tables["goto_table"], input
    )
    print(steps_parsing)
    return {
        "parsingTable": goto_action_tables,
        "stepsParsing": steps_parsing,
        "grammar": new_grammar,
    }
