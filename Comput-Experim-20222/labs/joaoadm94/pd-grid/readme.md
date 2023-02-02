# Projeto de alteração no modelo "Demographic Prisoner's Dilemma on a Grid"

O modelo neste repositório é baseado no exemplo PD_Grid do framework Mesa.

No modelo original existe uma grade de agentes interagindo segundo as regras do Dilema do Prisioneiro. Há uma tabela de valores predefinidos para as interações possíveis, sendo elas: 1 ponto para cooperação mútua, 1.6 ponto para traição com sucesso, e 0 pontos para traição mútua ou traição sem sucesso. 

A única variável acessível no modelo original é o Escalonador dos agentes - ou *Scheduler Type* - com as opções Sequencial (*Sequential*), Aleatório (*Random*) ou Simultâneo (*Simultaneous*). Essa configuração determina a ordem de atualização de cada agente dado que ele considera o estado dos vizinhos para determinar seu próprio estado seguinte.

Adicionou-se as seguintes modificações no modelo: 
* Um seletor do tipo *slider* chamado *Defect multiplier* para configurar a recompensa da interação de traição com sucesso. Este é o valor dado ao agente traidor em uma rodada onde o vizinho cooperou. O valor padrão é 1.6, e pode ser alterado em 50% para mais ou para menos.
* Um gráfico para visualizarmos quantos agentes de cada estratégia temos na grade a cada etapa.

Foi necessário adicionar os elementos *Slider* e *Chart Module*. Adicionamos também uma variável para armazenar o valor original da recompensa, visto que este será modificado ao longo das simulações. Há também uma lógica simples para multiplicar o valor no dicionário *payoff* pelo percentual escolhido.

### Hipótese causal
No modelo original o comportamento do sistema nos modos Aleatório e Sequencial é bastante estável entre as simulações. É esperado que até os 20 primeiros passos o tabuleiro seja tomado pela estratégia de traição. Em seguida, nos próximos 20 passos, a estratégia de cooperação retoma o tabuleiro. Por volta dos 40 passos o tabuleiro está dominado pela estratégia cooperativa, com poucos clusters de agentes traidores - as vezes não sobra nenhum.

Criamos uma configuração da recompensa por traição, podendo aumentá-la ou diminuí-la. Para avaliar os efeitos, formulou-se a seguinte hipóteses:

* A recompensa por traição tem impacto proporcional na variação da população de agentes traidores.

De acordo com a hipótese, ao aumentar a recompensa por traição o número de agentes traidores teria aumento rápido em comparação com o valor padrão.

Da mesma forma, esperamos que uma recompensa menor cause uma redução da população de traidores em comparação com o cenário padrão.

### Uso do modelo

Para executar o modelo, basta ter o framework Mesa instalado. Ao executar o comando 

```mesa runserver PD_Grid" ```

no diretório que contém a pasta "PD_Grid" - onde ficam os arquivos do modelo - será iniciada a interface pelo navegador.

Para interagir com a nova funcionalidade, basta arrastar o seletor para a direita para aumentar a recompensa; para a esquerda, diminuimos a recompensa. Cada nível altera em 10% o valor. As alterações terão efeito após apertar o botão "Reset" no menu superior esquerdo.


## Descrição original do modelo

### Demographic Prisoner's Dilemma on a Grid
#### Summary

The Demographic Prisoner's Dilemma is a family of variants on the classic two-player [Prisoner's Dilemma]. The model consists of agents, each with a strategy of either Cooperate or Defect. Each agent's payoff is based on its strategy and the strategies of its spatial neighbors. After each step of the model, the agents adopt the strategy of their neighbor with the highest total score.

The model payoff table is:

|               | Cooperate | Defect|
|:-------------:|:---------:|:-----:|
| **Cooperate** | 1, 1      | 0, D  |
| **Defect**    | D, 0      | 0, 0  |

Where *D* is the defection bonus, generally set higher than 1. In these runs, the defection bonus is set to $D=1.6$.

The Demographic Prisoner's Dilemma demonstrates how simple rules can lead to the emergence of widespread cooperation, despite the Defection strategy dominating each individual interaction game. However, it is also interesting for another reason: it is known to be sensitive to the activation regime employed in it.

### How to Run

##### Web based model simulation

To run the model interactively, run ``mesa runserver`` in this directory.

##### Jupyter Notebook

Launch the ``Demographic Prisoner's Dilemma Activation Schedule.ipynb`` notebook and run the code.

### Files

* ``run.py`` is the entry point for the font-end simulations.
* ``pd_grid/``: contains the model and agent classes; the model takes a ``schedule_type`` string as an argument, which determines what schedule type the model uses: Sequential, Random or Simultaneous.
* ``Demographic Prisoner's Dilemma Activation Schedule.ipynb``: Jupyter Notebook for running the scheduling experiment. This runs the model three times, one for each activation type, and demonstrates how the activation regime drives the model to different outcomes.

### Further Reading

This model is adapted from:

Wilensky, U. (2002). NetLogo PD Basic Evolutionary model. http://ccl.northwestern.edu/netlogo/models/PDBasicEvolutionary. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

The Demographic Prisoner's Dilemma originates from:

[Epstein, J. Zones of Cooperation in Demographic Prisoner's Dilemma. 1998.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.8.8629&rep=rep1&type=pdf)
