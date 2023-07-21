# Importacoes
import pandas as pd

#Obter tabela do site
def get_parsing_table(grammar, analysis_type):
    if (analysis_type == 'll1'):
        aux_type = 'll1-table'
    elif (analysis_type == 'slr1'):
        aux_type = 'lr0'
    else:
        aux_type = analysis_type

    url = f'https://smlweb.cpsc.ucalgary.ca/{aux_type}.php?grammar={grammar}'
    url = url.replace(" ", "%20")

    print(url)

    print('TESTE 0')

    parsing_table = pd.read_html(url)
    print(parsing_table)
    if (analysis_type == 'lr0' or analysis_type == 'lr1'):
        print('LR0 ou LR1')
        return parsing_table[2]
    elif (analysis_type == 'll1'):
        print('LL1')
        return parsing_table[1]
    elif (analysis_type == 'slr1' or analysis_type == 'lalr1'):
        print('SLR1')
        print(parsing_table[3])
        return parsing_table[3]
    else:
        return {'Erro': 'Houve um erro!'}


#Converter tabela em dicionario
def get_parsing_dict(parsing_table):
    parsing_table = parsing_table.drop([0], axis=1)
    parsing_table.columns = parsing_table.iloc[0]
    parsing_table = parsing_table[1:]
    parsing_table = parsing_table.fillna('error')

    return parsing_table.to_dict()


#Separar terminais e nao-terminais
def sep_terminals_nonterminals(grammar):
    terminals = []
    nonterminals = []

    grammar_array = grammar.split('.')
    grammar_array.pop()

    for line in grammar_array:
        aux = line.split('->')
        nonterminals.append(aux[0])
        aux1 = aux[1].split('|')
        for i in aux1:
            aux2 = i.split(' ')
            for j in aux2:
                terminals.append(j)

    for i in nonterminals:
        for j in terminals:
            if (i == j):
                terminals.remove(i)

    return {'terminals': list(set(terminals)), 'nonterminals': list(set(nonterminals))}

#Separar tabela de acoes e transicoes
def get_goto_action_tables(grammar, analysis_type):
    parsing_table = get_parsing_dict(get_parsing_table(grammar, analysis_type))
    term_nterm = sep_terminals_nonterminals(grammar)

    action = {key: parsing_table[key] for key in parsing_table.keys() & term_nterm['terminals']}
    action['$'] = parsing_table['$']
    goto = {key: parsing_table[key] for key in parsing_table.keys() & term_nterm['nonterminals']}

    return {'terminals_nonterminals': term_nterm, 'action_table': action, 'goto_table': goto}

# open_site('https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/')
#print(get_parsing_table('SOMA->A|d.A->b.A->c.', 'slr1'))
#print(get_parsing_dict(get_parsing_table('SOMA->A|d.A->b.A->c.', 'slr1')))
# print(get_goto_action_tables('E->E v T.E->T.T->T and F.T->F.F->parenteses_esq E parenteses_dir.F->id.', 'slr1'))
