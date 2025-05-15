import sys

sys.path.append("./")

from app.problem.problem_plotter import ProblemPlotterFacade
from app.data_handler.load_data import (
    load_data_sbrp,
)

plotter = ProblemPlotterFacade()
sbrp_instance = "SBRP_instance_1_2d"
data, routes = load_data_sbrp(sbrp_instance, multiple_routes=True)

# *** Ejemplo básico ***
plotter.plot_problem(
    problem_title="SBRP",
    problem_type="sbrp",
    view_mode="2d",
    data=data,
    routes=routes,
    depot_config={
        "depot_size": 20,
        "depot_marker_type": "D",
        "depot_marker_color": "#000000",
        "depot_marker_border": 3,
        "depot_marker_border_color": "#444444",
        "depot_font_color": "#EEEEEE",
        "depot_font_size": 11,
    },
    stop_config={
        "stop_size": 20,
        "stop_marker_type": "h",
        "stop_marker_color": "#EEEEEE",
        "stop_marker_border": 2,
        "stop_marker_border_color": "gray",
        "stop_font_color": "#222222",
        "stop_font_size": 10,
        "stop_demand_size": 7,
        "stop_demand_color": "#111111",
    },
    passenger_config={
        "passenger_size": 9,
        "passenger_marker_type": "X",
        "passenger_marker_color": "#555555",
        "passenger_marker_border": 1,
        "passenger_marker_border_color": "black",
        "passenger_route_style": ":",
        "passenger_route_color": "black",
        "passenger_route_weight": 1,
    },
    routes_config={
        "route_line_style": "--",
        "route_weight": 1.8,
        "custom_colors_list": ["gray", "#222222"],
        "random_colors": False,
    },
)
