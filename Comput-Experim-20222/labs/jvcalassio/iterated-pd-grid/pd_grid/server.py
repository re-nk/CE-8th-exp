from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter

from .portrayal import portrayPDAgent
from .model import PdGrid


# Make a world that is 50x50, on a 500x500 display.
canvas_element = CanvasGrid(portrayPDAgent, 50, 50, 500, 500)
chart_element = ChartModule(
    [{"Label": "Cooperating_Agents", "Color": "blue"}, {"Label": "Defecting_Agents", "Color": "red"}]
)
# chart_element = ChartModule(
#     [{"Label": "Total_value", "Color": "green"}]
# )

class TotalOutputElement(TextElement):
    def __init__(self):
        super().__init__()

    def render(self, model):
        return "Total value: " + str(sum([agent.score for agent in model.schedule.agents]))

total_coop = TotalOutputElement()

model_params = {
    "height": 50,
    "width": 50,
    "schedule_type": UserSettableParameter(
        "choice",
        "Scheduler type",
        value="Random",
        choices=list(PdGrid.schedule_types.keys()),
    ),
    "initial_cooperation": UserSettableParameter(
        "slider",
        "Initial cooperation %",
        value=0.5,
        min_value=0,
        max_value=1,
        step=0.01
    ),
    "defection_award": UserSettableParameter(
        "slider",
        "Defection award",
        value=1.6,
        min_value=0,
        max_value=10,
        step=0.1
    )
}

server = ModularServer(PdGrid, [canvas_element, total_coop, chart_element], "Prisoner's Dilemma", model_params)
