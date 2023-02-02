from mesa import Model
from mesa.time import BaseScheduler, RandomActivation, SimultaneousActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

from .agent import PDAgent


class PdGrid(Model):
    """Model class for iterated, spatial prisoner's dilemma model."""

    schedule_types = {
        "Sequential": BaseScheduler,
        "Random": RandomActivation,
        "Simultaneous": SimultaneousActivation,
    }

    # This dictionary holds the payoff for this agent,
    # keyed on: (my_move, other_move)

    #payoff = {("C", "C"): 1, ("C", "D"): 0, ("D", "C"): 2.0, ("D", "D"): 0}

    def __init__(
        self, height=50, width=50, 
        schedule_type="Random", 
        initial_cooperation=0.5,
        defection_award=1.6
    ):
        """
        Create a new Spatial Prisoners' Dilemma Model.

        Args:
            height, width: Grid size. There will be one agent per grid cell.
            schedule_type: Can be "Sequential", "Random", or "Simultaneous".
                           Determines the agent activation regime.
            payoffs: (optional) Dictionary of (move, neighbor_move) payoffs.
        """
        self.grid = SingleGrid(width, height, torus=True)

        # Handles problem caused by batch_runner _make_model_kwargs function
        # It transforms every iterable to params, so it doesn't support strings as a single param
        # I'll check if an integer is received and map it to each scheduler type
        if type(schedule_type) == int:
            self.schedule_type = list(self.schedule_types.keys())[schedule_type]
        else:
            self.schedule_type = schedule_type

        self.schedule = self.schedule_types[self.schedule_type](self)
        self.payoff = {
            ("C", "C"): 1, 
            ("C", "D"): 0, 
            ("D", "C"): defection_award, 
            ("D", "D"): 0
        }

        # Create agents
        for x in range(width):
            for y in range(height):
                agent = PDAgent(
                    (x, y), 
                    self,
                    self.random.choices(["C", "D"], weights=[initial_cooperation, 1-initial_cooperation])[0]
                )
                self.grid.place_agent(agent, (x, y))
                self.schedule.add(agent)

        self.world_value = 0

        self.datacollector = DataCollector(
            {
                "Cooperating_Agents": lambda m: len(
                    [a for a in m.schedule.agents if a.move == "C"]
                ),
                "Defecting_Agents": lambda m: len(
                    [a for a in m.schedule.agents if a.move == "D"]
                ),
                "Total_value": lambda m: sum(
                    [agent.score for agent in m.schedule.agents]
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
