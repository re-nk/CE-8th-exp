# Lethal Virus on a Network

## Resumo

Esse modelo é baseado no modelo NetLogo "Virus on Network" com algumas adaptações feitas por @seraphritt.

As adaptações feitas foram:
- [x] Nova variável dependente ``Virus Letal Chance`` foi adicionada.
- [x] Nova variável independente ``Dead`` foi adicionada.
- [X] Nova variável ``Stable`` foi adicionada, definindo assim a estabilidade do modelo na condição: "O modelo é considerado estável se não houver mais nenhum agente com estado ``Infected`` no grafo".
- [X] Adicionada função de captura de dados feitos pelo experimento em arquivos .csv.

Para mais informações, leia a página: http://ccl.northwestern.edu/netlogo/models/VirusonaNetwork.

Biblioteca JavaScript utilizada para renderizar a rede: [d3.js](https://d3js.org/).

## Hipótese Causal

A hipótese causal que se deseja provar é:

"A letalidade de um vírus não é a única
variável independente responsável por uma grande taxa de mortes por causa viral."

Em outras palavras, com esse modelo deseja-se provar que somente a letalidade do vírus não pode ser a única responsável pela grande taxas de mortes no caso de uma epidemia viral. Procura-se provar que um vírus precisa de mais de uma característica (por ex. grande taxa de transmissão) além da alta letalidade para que cause um grande número de mortes.  

## Justificativas para as mudanças no código

O código original não tinha nenhuma variável ou forma de mensurar os agentes mortos ou a letalidade de um vírus, possuindo apenas 3 estados (``Dead``, ``Suscetible``, ``Resistant``). Isso posto, para a comprovação da hipótese causal foi necessário adicionar as 2 variáveis já mencionadas anteriormente.

## Variáveis do modelo
Variáveis independentes:

* ``Number of agents`` define a quantidade de agentes na simulação, ou seja, o quantidade de
vértices no grafo, em um intervalo de 10 a 100.
* ``Virus Letal Chance`` define a probabilidade do vírus mudar a cor do agente de vermelho
(infected) para amarelo (dead), em um intervalo de 0 a 1.
* ``Avg Node Degree`` é a quantidade média de arestas que cada vértice possui, em um intervalo
de 3 a 8.
* ``Initial Outbreak Size`` controla a quantidade de agentes na cor vermelha (infected no primeiro
passo da simulação, em um intervalo de 1 a 10.
* ``Virus Spread Chance`` define a probabilidade dos vizinhos de um agente com a cor vermelha
fazer com que seus vizinhos também fiquem com a cor vermelha, ou seja, infectados, em
um intervalo de 0 a 1.
* ``Virus Check Frequency`` controla a probabilidade da simulação mudar o estado de um agente
para infected ou dead, em um intervalo de 0 a 1.
* ``Recovery Chance`` define a probabilidade de um agente ter sua cor mudada para verde (suscetible)
dado que está com a cor vermelha (infected), em um intervalo de 0 a 1.
* ``Gain Resistance Chance`` controla a probabilidade de um agente ter sua cor mudada para
cinza (resistant), em um intervalo de 0 a 1.

Variáveis dependentes:

* ``Infected`` apresenta a quantidade de agentes infectados.
* ``Suscetible`` apresenta a quantidade de agentes suscetíveis a serem infectados.
* ``Resistant`` apresenta a quantidade de agentes resistentes ao vírus, ou seja, mesma que tenham
contato com um agente infectado, esses agentes resistentes não serão infectados.
* ``Dead`` apresenta a quantidade de agentes mortos. Esses agentes não trasmitem o vírus.

## Instalação

Para instalar as dependências use pip e o arquivo ``requirements.txt`` presente nesse diretório.

```
    $ pip install -r requirements.txt
```

## Como executar

Para executar o modelo interativamente, digite ``mesa runserver`` nesse diretório.

```
    $ mesa runserver
```

Ou execute-o utilizando o comando python após instalar as dependências
```
    $ python run.py
```

Uma janela irá abrir-se automaticamente na porta [http://127.0.0.1:8521/](http://127.0.0.1:8521/), então precisone ``Start``.

## Arquivos

* ``run.py``: Executa o modelo e a interface do servidor.
* ``model.py``: Contem a classe do agente do modelo e a classe geral do modelo.
* ``server.py``: Define as classes que serão visualizadas no navegador por meio do servidor do modelo Mesa.

## Para mais informações

[Stonedahl, F. and Wilensky, U. (2008). NetLogo Virus on a Network model](http://ccl.northwestern.edu/netlogo/models/VirusonaNetwork).
Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.


[Wilensky, U. (1999). NetLogo](http://ccl.northwestern.edu/netlogo/)
Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

