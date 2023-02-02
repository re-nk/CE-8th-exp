## Descrição da Hipótese Causal

A hipótese trabalhada neste laboratório busca comprovar a influência da saúde das árvores e consequentemente das florestas na retardação de incêndios florestais e na capacidade de autorrecuperação da área.

A pesquisa bibliométrica feita anteriormente demonstrou um interesse da comunidade científica em explorar variáveis independentes que afetam os ambientes florestais e que os tornam, ou não, mais propícios aos incêndios. Desse modo, nesta primeira alteração do modelo de simulação uma nova variável independente, que foi pensada como fator universal de todos as características que podem influenciar ambientalmente a flora de uma área, foi adicionada.

  

## Justificativas para Mudanças

### Alteração dos agentes
Foi adicionado um novo atributo ao agente "árvore" da simulação. O atributo saúde pode conter dois valores: "Healthy" e "Unhealthy".

- Justificativa:
	> Com esse novo atributo é possível condicionar ainda mais a possibilidade de árvore aderir ao fogo, de modo que as árvores saudáveis permanecerão desta forma independente do estado atual de suas vizinhas. 

### Alteração do modelo
"health_percentage", um novo argumento, foi adicionado ao modelo.

- Justificativa:
	>A alteração permite a definição da quantidade de árvores percentuais completamente saudáveis na área simulada.
  

## Orientações de uso do Simulador
As alterações feitas no simulador não afetaram os métodos de execução do simulador. Desse modo, o comando de execução continua o mesmo apresentado abaixo. No entanto, a nova variável de percentual de árvores saudáveis deve ser manipulada para que hajam resultados diferentes ao padrão.
``` 
 $ mesa runserver
```

Abrir o servidor no navegador através da URL:
```
 http://127.0.0.1:8521/
```


## Descrição das variáveis
### Independentes
- Tree Density
	>Variável padrão do modelo. Regula a quantidade de árvores colocadas de forma aleatória no grid de simulação. Nesse modelo, a densidade da área é importante porque o fogo do incêndio só é transmitido por proximidade/vizinhança. 

- Healthy Tree Percentage
	>Variável adicionada nesta alteração do modelo. Ela visa definir de forma aleatória o percentual de árvores da simulação que serão completamente saudáveis, ou seja, que não aderirão ao incêndio.

### Dependentes
- Área preservada e Queimada
	>Relaciona a quantidade de árvores queimadas, em chamas e sadias
- Capacidade de Recuperação da Área Queimada
	>Variável que considera a capacidade de uma árvore não queimada de recuperar no mínimo mais uma árvore queimada após o incêndio.
