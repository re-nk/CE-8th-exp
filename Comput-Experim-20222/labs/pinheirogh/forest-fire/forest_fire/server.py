import mesa

from .model import ForestFire

COLORS = {"Fine": "#00AA00", "On Fire": "#880000", "Burned Out": "#000000"}
COLORS2 = {"arvores_recuperaveis": "#00AA00", "arvores_irrecuperaveis": "#660000"}


def forest_fire_portrayal(tree):
    if tree is None:
        return
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
    (x, y) = tree.pos
    portrayal["x"] = x
    portrayal["y"] = y
    portrayal["Color"] = COLORS[tree.condition] if tree.health != "Healthy" else "#007d00"
    return portrayal


canvas_element = mesa.visualization.CanvasGrid(
    forest_fire_portrayal, 100, 100, 500, 500
)
tree_chart = mesa.visualization.ChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)
pie_chart = mesa.visualization.PieChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS.items()]
)
pie_chart2 = mesa.visualization.PieChartModule(
    [{"Label": label, "Color": color} for (label, color) in COLORS2.items()]
)
model_params = {
    "height": 100,
    "width": 100,
    "density": mesa.visualization.Slider("Tree density", 0.65, 0.01, 1.0, 0.01),
    "health_percentage": mesa.visualization.Slider("Healthy Tree Percentage", 0.3, 0.01, 1.0, 0.01),
}
server = mesa.visualization.ModularServer(
    ForestFire, [canvas_element, tree_chart, pie_chart, pie_chart2], "Forest Fire", model_params
)
