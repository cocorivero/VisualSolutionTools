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
        "depot_marker_type": "university",
        "depot_marker_color": "green",
    },
    stop_config={
        "stop_marker_type": "bus",
        "stop_marker_color": "red",
    },
    routes_config={
        "route_line_style": "solid",
        "route_weight": 2,
        "custom_colors_list": ["black"],
    },
    passenger_config={
        "passenger_marker_type": "user",
        "passenger_marker_color": "lightgray",
        "passenger_route_style": "dotted",
        "passenger_route_color": "red",
        "passenger_route_weight": 3,
    },
)
