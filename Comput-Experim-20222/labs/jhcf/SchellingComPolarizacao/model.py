import mesa

class SchellingAgentPolarized(mesa.Agent):
    """
    Schelling segregation agent, 
    Alterado para tratar de polarização
    """

    def __init__(self, pos, model, agent_type, polarization):
        """
        Create a new Schelling agent.

        Args:
           unique_id: Unique identifier for the agent.
           x, y: Agent initial location.
           agent_type: Indicator for the agent's type (minority=1, majority=0)
           polarization: Indicator for the agent's level of political polarization, i.e. anger against oponents
        """
        super().__init__(pos, model)
        self.pos = pos
        self.type = agent_type
        self.polarization = polarization
        self.happy = False

    def step(self):
        similar = 0
        for neighbor in self.model.grid.iter_neighbors(self.pos, True):
            if neighbor.type == self.type:
                similar += 1

        # If unhappy, move:
        if similar < self.model.homophily:
            # the agent is not happy
            self.model.grid.move_to_empty(self)
        else:
            self.happy = True
            self.model.happy += 1
            # minha implementação do modelo comporamental de um agente polarizado
            # se ele tem muitos vizinhos parecidos com ele, estará feliz, 
            # se estiver muito polarizado vai quere expulsar os vizinhos que não são iguais a ele 
            threshold = self.random.random()
            if (self.polarization >= threshold):
                qtd_neighbors_evicted = 0
                for neighbor in self.model.grid.iter_neighbors(self.pos, True):
                    if neighbor.type != self.type:
                        qtd_neighbors_evicted = qtd_neighbors_evicted + 1
                        self.model.grid.move_to_empty(neighbor)  
                if (qtd_neighbors_evicted > 0):
                    #print("Foram expulsos %d vizinhos pelo agente na posição %s"%(qtd_neighbors_evicted,self.pos))
                    self.model.qty_evictions = self.model.qty_evictions + qtd_neighbors_evicted

class SchellingPolarized(mesa.Model):
    """
    Modelo de simulação de Schelling, com introdução de uma variável que indica a polarização política da sociedade.
    Numa alta polarização, os vizinhos diferentes podem ser expulsos por vizinhos da outra facção que se sentem "felizes" 
    O Modelo é interrompido quando a quantidade de agentes felizes se estabiliza por três rodadas consecutivas.
    """

    def __init__(self, width=20, height=20, density=0.8, minority_pc=0.2, homophily=3, polarization=30):
        """ """

        self.width = width
        self.height = height
        self.density = density
        self.minority_pc = minority_pc
        self.homophily = homophily
        self.polarization = polarization
        self.qty_evictions = 0

        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.SingleGrid(width, height, torus=True)

        self.happy = 0
        self.stable = 0 # quando stable ficar em um, alcançamos o estado estávl na smulação
        self.happy_1 = -1 # qtd de pessoas felizes no passo anterior (n-1)
        self.happy_2 = -1 # qtd de pessoas felizes no passo anterior (n-2)

        # Set up agents
        # We use a grid iterator that returns
        # the coordinates of a cell as well as
        # its contents. (coord_iter)
        self.qty_agents = 0
        self.datacollector = mesa.DataCollector(
            model_reporters={"stable": "stable","running":"running","stepCount":"stepCount",
                             "happy": "happy", "happy_1":"happy_1", "happy_2":"happy_2",
                             "qty_agents":"qty_agents","qty_evictions":"qty_evictions"}  # Model-level count of happy agents
            # For testing purposes, agent's individual x and y
#            agent_reporters={"x": lambda a: a.pos[0], "y": lambda a: a.pos[1]},
        )

        for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]
            if self.random.random() < self.density:
                if self.random.random() < self.minority_pc:
                    agent_type = 1
                else:
                    agent_type = 0

                agent = SchellingAgentPolarized((x, y), self, agent_type, polarization)
                self.qty_agents = self.qty_agents + 1
                self.grid.position_agent(agent, (x, y))
                self.schedule.add(agent)

        self.running = True
        self.stepCount = 0
        #self.datacollector.collect(self)

    def step(self):
        """
        Run one step of the model. If All agents are happy, halt the model.
        """
        # verificação de estabilidade
        if (self.happy_1 >= 0 and self.happy_2 >= 0): 
        # Já existem dados suficientes para calcular estabilidade?
            if (self.happy_1 == self.happy_2 and self.happy_2 == self.happy):
                # A quantidade de cidadãos felizes nos últimos três passos é igual?
                if self.happy > (self.qty_agents/2):
                    # A maioria dos cidadãos já está feliz?
#                    print("parar")
#                    print("happy==%d"%self.happy)
#                    print("happy_1==%d"%self.happy_1)
#                    print("happy_2==%d"%self.happy_2)
#                    print("stepCount==%d"%self.stepCount)
#                    print("qtd_expulsoes_totais==%d"%self.qtd_expulsoes_totais)
                    self.stable = 1
                    self.running = False
                    self.datacollector.collect(self)
                    return
        self.stepCount = self.stepCount + 1
        self.happy = 0  # Reset counter of happy agents
        self.schedule.step()
        # encerrou esse passo da simulação => coleto os dados
        self.datacollector.collect(self)
        # após encerrado o passo, atualizo as informações para teste no próximo passo
        if (self.happy_1 >= 0):
            self.happy_2 = self.happy_1
        self.happy_1 = self.happy
