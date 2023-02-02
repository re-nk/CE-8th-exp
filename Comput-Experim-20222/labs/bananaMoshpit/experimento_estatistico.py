# Experimentos estatísticos
import numpy as np

# algumas configurações de experimentos que produziram efeitos com alta variabilidade na exploração interativa do fenômeno.
# configuracao_instavel_do_fenomeno = {"width":20, "height":20,"density": 0.3, "minority_pc": 0.3, "homophily": range(3,5,1), "polarizacao": 0.9}

# planejamento do experimento
# hipótese 1 - quanto menor a homofilia mais rápido o sistema estabilizamb run teachers?
#!TODO: UPDATE VARS, MENTION PERC, FOCUS LIL CHANGE. controle, vars, processadores, RERUN W updated vsrs. 
controles_e_seus_niveis = {
    "width":40, 
    "height":40
#,    "density": 0.5
#,    "minority_pc": 0.3
#,    "homophily": 3 
#,    "polarization": .3
}
# usando o framework mesa e as facilidades da computação experimental, 
# combinado com as orientações em https://www.voxco.com/blog/factorial-experimental-design/
# vamos realizar o "desenho fatorial de experimentos", onde estudaremos os efeitos de múltiplos fatores.
# vamos usar a técnica de "desenho totalmente cruzado", onde cada um dos fatores possui múltiplos níveis de tratamento
# "Using this design, all the possible combinations of factor levels can be investigated in each replication"
variaveis_independentes_e_seus_niveis = {
    "density": np.arange(0.1,1,0.2), # 4x
    "minority_pc": np.arange(0.1,1,0.2), # 4x
    "homophily": np.arange(1,9,1), # 7x
}
lista_de_fatores = variaveis_independentes_e_seus_niveis.keys()
print("Lista de Fatores: "+str(lista_de_fatores))
lista_de_niveis_por_fator = variaveis_independentes_e_seus_niveis.values()
print("Lista de tratamentos ou níveis por fator: "+str(lista_de_niveis_por_fator))
qtd_de_tratamentos_por_fator = [f.size for f in lista_de_niveis_por_fator]
print("Quantidade de tratamentos ou níveis por fator: "+str(qtd_de_tratamentos_por_fator))
qtd_total_tratamentos = np.prod([f.size for f in variaveis_independentes_e_seus_niveis.values()])
print("Quantidade total de tratamentos a serem aplicados: "+str(qtd_total_tratamentos))

# soma os dois dicionários 
experimental_design_of_independent_plus_control_variables = controles_e_seus_niveis.copy()
experimental_design_of_independent_plus_control_variables.update(variaveis_independentes_e_seus_niveis)

replicacoes=50 # no desenho experimental, esse parâmetro é chamado de replicação, e indica a quantidade de replicações de cada tratamento 
print("Quantidade de replicações para cada tratamento:"+str(replicacoes))

print("Quantidade total de simulações independentes a serem realizadas:"+str(replicacoes*qtd_total_tratamentos))

print("Uma vez que cada simulação é um sujeito novo, completamente definido por variáveis aleatórias, estaremos fazendo um 'Between Subject Factorial Design'")


import mesa
from model import Schelling
qtd_maxima_passos_para_estabilizar = 800 # qtd de interações necessárias para o fenômeno é estabilizar

from datetime import datetime
inicio_experimento = datetime.now()

qtd_processadores = 6
print("No âmbito da algoritmica experimental, estamos interessados em saber se a computação multithead reduz o tempo... ")
print("Qtd de processadores: "+str(qtd_processadores))

def get_segregation(model):
    """
    Find the % of agents that only have neighbors of their same type.
    """
    segregated_agents = 0
    for agent in model.schedule.agents:
        segregated = True
        for neighbor in model.grid.iter_neighbors(agent.pos, True):
            if neighbor.type != agent.type:
                segregated = False
                break
        if segregated:
            segregated_agents += 1
    return segregated_agents / model.schedule.get_agent_count()
model_reporters = {"Segregated_Agents": get_segregation}

results = mesa.batch_run(
    Schelling,
    parameters=experimental_design_of_independent_plus_control_variables,
    iterations=replicacoes,
    max_steps=qtd_maxima_passos_para_estabilizar,
    number_processes=qtd_processadores, # usar todos os processadores disponíveis em um arranjo multithread
    data_collection_period=-1,
    display_progress=True,
   # model_reporters=model_reporters,
)

# gera uma string com data e hora
fim_experimento = datetime.now()
duracao_experimento = fim_experimento - inicio_experimento
fim_experimento_str = str ( fim_experimento )


file_name_suffix = (
    "_fatores[" +str(lista_de_fatores).replace("[","").replace("]","").replace("(","").replace(")","").replace("-","").replace("dict_keys","")+"]"
    "_tratam[" + str(qtd_total_tratamentos) +"]" +
    "_replic[" + str (replicacoes) +"]"+
    "_passos["+ str (qtd_maxima_passos_para_estabilizar)+"]"+
    "_process["+ str (qtd_processadores)+ "]"+
    "_segs["+ str(duracao_experimento.seconds) + "]"+
    "_final["+ fim_experimento_str +"]"
). replace ( ":" , "-" ). replace ( " " , "-" )
# define um prefixo para o nome para o arquivo de dados
model_name_preffix = " "
# define o nome do arquivo
file_name = model_name_preffix + file_name_suffix + ".csv"
print(file_name)

import pandas as pd
results_df = pd.DataFrame(results)
results_df.to_csv(file_name)
