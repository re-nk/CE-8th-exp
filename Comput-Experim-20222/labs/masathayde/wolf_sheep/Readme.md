# Modelo de Predação Wolf-Sheep, com canibalismo

## Resumo

O modelo é uma adaptação do exemplo Wolf-Sheep oferecido pelo framework Mesa. Ao modelo, foi adicionado a possibilidade de lobos poderem canibalizar outros lobos em situações de fome.

## Hipótese causal

O intuito dessa alteração é estudar os efeitos do canibalismo em um sistema predatório. A hipótese guiadora do trabalho é que a existência de canibalismo pode ser benéfica para a espécie, até sendo capaz de prevenir sua extinção em cenários extremos de fome.

## Como usar o simulador

Para utilizar o simulador, instalar o módulo Mesa para Python, acessar o diretório principal do projeto, e executar o comando "mesa runserver". Uma janela do navegador será aberta, na qual uma interface gráfica permite o controle de parâmetros da simulação.

## Variáveis da simulação

Variáveis Independentes:

- Grass: Grama. Presença ou não de grama na simulação. Caso não, as ovelhas não se alimentam de grama e nunca perdem energia.
- Grass Regrowth Rate: Taxa de regeneração da grama. Quantos passos até um espaço com grama amadurecer a ponto de ser consumível por ovelhas.
- Initial Sheep Population: População inicial de ovelhas
- Sheep Reproduction Rate: Taxa de reprodução de ovelhas: Representa a chance de uma ovelha reproduzir-se a cada passo
- Initial Wolf Population: População inicial de lobos
- Wolf Reproduction Rate: Taxa de reprodução de lobos: Representa a chance de um lobo reproduzir-se a cada passo
- Wolf Gain From Food: Ganho de energia de um lobo quando se alimenta de uma ovelha.
- Sheep Gain From Food: Ganho de energia de uma ovelha quando se alimenta de grama.
- Cannibalism Threshold: Nível de energia abaixo do qual lobos passam a considerar canibalismo.
- Wolf Gain From Cannibalism: Ganho de energia de um lobo quando se alimenta de outro lobo.

Variáveis Dependentes:

- Wolves: Quantidade lobos vivos.
- Sheep: Quantidade ovelhas vivas.
- Grass: Quantidade de espaços com grama madura.
- Cannibalism Occurrences: Número de vezes que houve canibalismo.