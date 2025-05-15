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
        "depot_size": 35,
        "depot_marker_type": "p",
        "depot_marker_color": "magenta",
        "depot_marker_border": 4,
        "depot_marker_border_color": "black",
        "depot_font_color": "#000000",
        "depot_font_size": 14,
    },
    stop_config={
        "stop_size": 20,
        "stop_marker_type": "o",
        "stop_marker_color": "#00FA9A",  # medium spring green
        "stop_marker_border": 3,
        "stop_marker_border_color": "blue",
        "stop_font_color": "black",
        "stop_font_size": 10,
        "stop_demand_size": 10,
        "stop_demand_color": "#FF6347",  # tomato red
    },
    passenger_config={
        "passenger_size": 11,
        "passenger_marker_type": "*",
        "passenger_marker_color": "#9400D3",  # dark violet
        "passenger_marker_border": 2,
        "passenger_marker_border_color": "black",  # gold
        "passenger_route_style": "-",
        "passenger_route_color": "blue",
        "passenger_route_weight": 2,
    },
    routes_config={
        "route_line_style": "solid",
        "route_weight": 3,
        "custom_colors_list": ["red", "orange", "lime"],
        "random_colors": False,
    },
)
