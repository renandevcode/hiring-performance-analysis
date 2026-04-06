import pandas as pd
from tabulate import tabulate

#realiza leitura de arquivo por performance('Avaliacao Desempenho') e meio usado para contratação
def employee_hiring(performance):
    df = pd.read_excel("data/HRDadosLimpos.xlsx", sheet_name="Avaliacao fonte recrutamento ru")
    # index da coluna no excel
    index_of_networks = 11
    index_of_performance=10

    hiring_networks = [] # meios de contratação
    json_format = {} # inicializa o formato de retorno em json

    for i in df.values:
        # filtra redes de contratação por performance desejada
        if i[index_of_performance]==performance:
            hiring_networks.append(i[index_of_networks])


    hiring_networks = list(dict.fromkeys(hiring_networks)) # elimina duplicatas
    hiring_numbers=[0]*len(hiring_networks) # inicializa o array de quantidade contratada por rede


    for i in df.values:
        if i[index_of_performance]==performance:
            hiring_numbers[hiring_networks.index(i[index_of_networks])]+=1 # contador de ocorrências : pessoas cotratadas por rede

    for i in range(len(hiring_networks)):
        json_format[hiring_networks[i]]=hiring_numbers[i] # atribui quantidade à rede de contratação

    sorted_networks=sorted(json_format,key=lambda x:json_format[x],reverse=True) # ordenação decrescente da redes utilizadas
    return [json_format, sorted_networks]

def ranking(performance,table=False):
    json_format, sorted_networks=employee_hiring(performance)
    # retorno em array - especifíco para a biblioteca tabulate
    if table :
        rank_array = []
        for i, network in enumerate(sorted_networks):
            rank_array.append([i + 1, network, json_format[network]])
        return rank_array

    # retorno de mensagem formatada para terminal
    rank=""
    for i in range (len(json_format)):
        rank += f"{i + 1}º {sorted_networks[i]} : {json_format[sorted_networks[i]]}\n"
    return rank

# retorna tabela no terminal
def terminal_table(performance):
    data=ranking(performance,table=True)
    headers=["rank","network","hired quantity"]
    return tabulate(data, headers=headers, tablefmt='grid')

# salva dados em formato tabela por arquivo .xsml
def to_excel(performance):
    dados = ranking(performance, table=True)
    df = pd.DataFrame(dados)
    df.columns = ["rank", "network", "hiring_numbers"]
    file="excel/"+(str(performance).split(" ")[0]).lower()+".xlsx"
    df.to_excel(file, index=False)




print(ranking("Atende totalmente"))
print('-'*20)
print(ranking("Excede"))
print('-'*20)
print(terminal_table("Atende totalmente"))
print('-'*20)
print(terminal_table("Excede"))
to_excel("Excede")
to_excel("Atende totalmente")




