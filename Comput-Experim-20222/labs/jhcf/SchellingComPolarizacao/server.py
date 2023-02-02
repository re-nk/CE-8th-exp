import mesa

from model import SchellingPolarized

def get_info(model):
    """
    Display a text count of how many happy agents there are.
    """
    return f"Happy agents: {model.happy}, happy-1: {model.happy_1}, happy-2: {model.happy_2}, qty_agents: {model.qty_agents}"

def get_stable(model):
    """
    Is model stable?
    """
    return f"Is the model stable? {model.stable}"

def schelling_draw(agent):
    """
    Portrayal Method for canvas
    """
    if agent is None:
        return
    portrayal = {"Shape": "circle", "r": 0.5, "Filled": "true", "Layer": 0}

    if agent.type == 0:
        portrayal["Color"] = ["#FF0000", "#FF9999"]
        portrayal["stroke_color"] = "#00FF00"
    else:
        portrayal["Color"] = ["#0000FF", "#9999FF"]
        portrayal["stroke_color"] = "#000000"
    return portrayal


canvas_element = mesa.visualization.CanvasGrid(schelling_draw, 20, 20, 500, 500)
happy_chart = mesa.visualization.ChartModule([{"Label": "happy", "Color": "Black"}])
happy_chart2 = mesa.visualization.ChartModule([{"Label": "qty_evictions", "Color": "Red"}])

model_params = {
    "height": 20,
    "width": 20,
    "density": mesa.visualization.Slider("Density of Agents", 0.3, 0.05, 1.0, 0.05),
    "minority_pc": mesa.visualization.Slider("Minority Fraction", 0.2, 0.00, 1.0, 0.05),
    "homophily": mesa.visualization.Slider("Homophily", 3, 0, 8, 1),
    "polarization": mesa.visualization.Slider("Polarization", 2, 0, 1, 0.1)
}

server = mesa.visualization.ModularServer(
    SchellingPolarized,
    [canvas_element, get_stable, get_info, happy_chart,happy_chart2],
    "Schelling Segregation Polarized",
    model_params,
)
