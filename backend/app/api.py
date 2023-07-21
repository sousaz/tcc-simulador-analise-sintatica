# Imortacoes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar funcoes
from app import parsing_table
from app import parsing_algorithm

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#Testar API
@app.get("/test/")
async def read_root() -> dict:
    return {"message": "Testando api"}


@app.get("/analyze/{grammar}/{input}/{analysis_type}")
async def get_table(input: str, grammar: str, analysis_type: str):
    goto_action_tables = parsing_table.get_goto_action_tables(grammar, analysis_type)
    
    steps_parsing = parsing_algorithm.bottom_up_algorithm(goto_action_tables['action_table'],
                                                        goto_action_tables['goto_table'],
                                                      input
                                                      )
    return {'parsingTable': goto_action_tables, 'stepsParsing': steps_parsing}
