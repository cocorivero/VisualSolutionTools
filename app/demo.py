import sys

sys.path.append("./")

from app.plotter.problem_plotter import ProblemPlotterFacade
from app.data_handler.load_data import (
    load_data_tsp,
    load_data_vrp,
    load_data_cvrp,
    load_data_bss,
    load_data_sbrp,
)

plotter = ProblemPlotterFacade()

# # *** Ejemplo básico ***
# plotter.plot_problem(
#     problem_type="tsp",
#     data={
#         "depot_id": "1",
#         "locations": {
#             "1": {"coordinates": (0.5, 0.5)},
#             "2": {"coordinates": (0, 1)},
#             "3": {"coordinates": (2, 2)},
#             "4": {"coordinates": (4, 1)},
#         },
#     },
#     routes=[["1", "2", "3", "4", "1"]],
#     graph_title="Ejemplo básico",
#     depot_config={"depot_size": 20, "depot_marker_color": "lime"},
#     stop_config={"stop_marker_color": "white", "stop_font_size": 10},
#     routes_config={
#         "route_line_style": "solid",
#         "custom_colors_list": ["red"],
#     },
# )

# *** TSP ***
# tsp_instance = "TSP_instance_1"
# data, routes = load_data_tsp(tsp_instance)
# plotter.plot_problem("tsp", data, routes)

# *** VRP ***
# vrp_instance = "VRP_instance_1"
# data, routes = load_data_vrp(vrp_instance)
# plotter.plot_problem("vrp", data, routes)

# *** CVRP ***
# cvrp_instance = "CVRP_instance_2"
# data, routes = load_data_cvrp(cvrp_instance)
# plotter.plot_problem("cvrp", data, routes)

# *** BSS ***
bss_instance = "BSS_solution_12"
data = load_data_bss(bss_instance)
plotter.plot_problem("bss", data)

# *** SBRP ***
# sbrp_instance = "SBRP_instance_1"
# data, routes = load_data_sbrp(sbrp_instance, multiple_routes=True)
# plotter.plot_problem("sbrp", data, routes)

# *** Parámetros configurables ***
# graph_title="TSP_Instancia_3",

# depot_config={
#     # "depot_size": 18,
#     "depot_marker_type": "o",
#     "depot_marker_color": "lime",
#     # "depot_marker_border": 2,
#     "depot_marker_border_color": "black",
#     "depot_font_color": "black",
#     # "depot_font_size": 12,
# },

# stop_config={
#     "stop_size": 15,
#     "stop_marker_type": "o",
#     "stop_marker_color": "white",
#     "stop_marker_border": 2,
#     "stop_marker_border_color": "black",
#     "stop_font_color": "black",
#     "stop_font_size": 8,
#     "stop_demand_size": 6,
#     "stop_demand_color": "grey",
#     "stop_marker_passenger_type": "o",
#     "stop_marker_passenger_size": 5,
#     "stop_marker_passenger_color": "red",
#     "stop_marker_passenger_border": 1,
#     "stop_marker_passenger_border_color": "black",
#     "passenger_route_style": "--",
#     "passenger_route_color": "grey",
# },

# routes_config={
#     "route_line_style": "solid",
#     "route_thickness": 2,
#     "random_colors": True,
#     "custom_colors_list": [
#         "blue",
#     ],
# },
