import sys

sys.path.append("./")

from app.problem.problem_plotter import ProblemPlotterFacade
from app.data_handler.load_data import (
    load_data_sbrp,
)

plotter = ProblemPlotterFacade()
sbrp_instance = "SBRP_instance_2_map"
data, routes = load_data_sbrp(sbrp_instance, multiple_routes=True)

# *** Ejemplo básico ***
plotter.plot_problem(
    problem_title="SBRP",
    problem_type="sbrp",
    view_mode="map",
    data=data,
    routes=routes,
    depot_config={
        "depot_marker_type": "shopping-bag",
        "depot_marker_color": "orange",
    },
    stop_config={
        "stop_marker_type": "motorcycle",
        "stop_marker_color": "green",
    },
    routes_config={
        "route_line_style": "dotted",
        "route_weight": 4,
        "custom_colors_list": ["green", "blue"],
    },
    passenger_config={
        "passenger_marker_type": "flag",
        "passenger_marker_color": "red",
        "passenger_route_style": "dashed",
        "passenger_route_color": "darkblue",
        "passenger_route_weight": 3,
    },
)
