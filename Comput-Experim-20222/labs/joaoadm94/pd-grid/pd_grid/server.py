import mesa

from .portrayal import portrayPDAgent
from .model import PdGrid


# Make a world that is 50x50, on a 500x500 display.
canvas_element = mesa.visualization.CanvasGrid(portrayPDAgent, 50, 50, 500, 500)

model_params = {
    "height": 50,
    "width": 50,
    "schedule_type": mesa.visualization.Choice(
        "Scheduler type",
        value="Random",
        choices=list(PdGrid.schedule_types.keys()),
    ),
    "defect_multiplier": mesa.visualization.Slider(
        "Defect multiplier",
        0,
        -5,
        5,
        description="Multiplier of the defection payoff"
    ),
    #"cooperation_start": mesa.visualization.Slider(
    #    "Cooperating at start",
    #    50,
    #    0,
    #    100,
    #    description="Percent of agents cooperating at start"),
}

# map data to chart in the ChartModule
chart_element = mesa.visualization.ChartModule(
    [
        {"Label": "Cooperating", "Color": "blue"},
        {"Label": "Defecting", "Color": "red"},
    ]
)

server = mesa.visualization.ModularServer(
    PdGrid, [canvas_element, chart_element], "Prisoner's Dilemma", model_params
)
