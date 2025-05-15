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
        "depot_size": 30,
        "depot_marker_type": "*",
        "depot_marker_color": "#FF4500",  # naranja fuerte
        "depot_marker_border": 5,
        "depot_marker_border_color": "darkblue",
        "depot_font_color": "white",
        "depot_font_size": 10,
    },
    stop_config={
        "stop_size": 18,
        "stop_marker_type": "s",
        "stop_marker_color": "gold",
        "stop_marker_border": 2,
        "stop_marker_border_color": "#228B22",  # forest green
        "stop_font_color": "#000000",
        "stop_font_size": 9,
        "stop_demand_size": 9,
        "stop_demand_color": "darkred",
    },
    passenger_config={
        "passenger_size": 12,
        "passenger_marker_type": "^",
        "passenger_marker_color": "deepskyblue",
        "passenger_marker_border": 1,
        "passenger_marker_border_color": "navy",
        "passenger_route_style": "--",
        "passenger_route_color": "#888888",
        "passenger_route_weight": 1.5,
    },
    routes_config={
        "route_line_style": "-.",
        "route_weight": 2.5,
        "custom_colors_list": ["#FF1493", "#00CED1"],
        "random_colors": False,
    },
)
