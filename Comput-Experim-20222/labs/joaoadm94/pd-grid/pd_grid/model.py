import mesa

from .agent import PDAgent

def get_num_coop_agents(model):
    """return number of cooperating agents"""

    coop_agents = [a for a in model.schedule.agents if a.isCooperating(a)]
    return len(coop_agents)


def get_num_def_agents(model):
    """return number of defecting agents"""

    def_agents = [a for a in model.schedule.agents if not a.isCooperating(a)]
    return len(def_agents)


class PdGrid(mesa.Model):
    """Model class for iterated, spatial prisoner's dilemma model."""

    schedule_types = {
        "Sequential": mesa.time.BaseScheduler,
        "Random": mesa.time.RandomActivation,
        "Simultaneous": mesa.time.SimultaneousActivation,
    }

    # This dictionary holds the payoff for this agent,
    # keyed on: (my_move, other_move)

    defect_multiplier = 1

    payoff = {("C", "C"): 1, ("C", "D"): 0, ("D", "C"): 1.6, ("D", "D"): 0}

    starting_payoff_dc = payoff[('D', 'C')]

    def __init__(
        self, width=50, height=50, schedule_type="Random", defect_multiplier=1, payoffs=None, seed=None
    ):
        """
        Create a new Spatial Prisoners' Dilemma Model.

        Args:
            width, height: Grid size. There will be one agent per grid cell.
            schedule_type: Can be "Sequential", "Random", or "Simultaneous".
                           Determines the agent activation regime.
            payoffs: (optional) Dictionary of (move, neighbor_move) payoffs.
        """
        self.grid = mesa.space.SingleGrid(width, height, torus=True)
        self.schedule_type = schedule_type
        self.schedule = self.schedule_types[self.schedule_type](self)
        self.payoff[('D', 'C')] = self.starting_payoff_dc * (1 + (defect_multiplier/10))
        print(defect_multiplier)
        print(self.payoff[('D', 'C')])

        # Create agents
        for x in range(width):
            for y in range(height):
                agent = PDAgent((x, y), self)
                self.grid.place_agent(agent, (x, y))
                self.schedule.add(agent)

        self.datacollector = mesa.DataCollector(
            {
                "Cooperating": lambda m: len(
                    [a for a in m.schedule.agents if a.move == "C"]
                ),
                "Defecting": lambda m: len(
                    [a for a in m.schedule.agents if a.move == "D"]
                )
            }
        )

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

    def run(self, n):
        """Run the model for n steps."""
        for _ in range(n):
            self.step()
