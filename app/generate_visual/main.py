import sys

sys.path.append("./")

from app.generate_visual.utils import (
    create_simple_stops,
    create_stops_with_assigned_passengers,
    create_stops_with_capacity,
)
from app.classes.vrp import VRP


def plot_problem(
    problem_type: str,
    depot_id: str,
    stops: dict,
    routes: list = [],
    passengers: list = [],
    x_label: str = "X-Axis",
    y_label: str = "Y-Axis",
    graph_title: str = "Graph Title",
):

    match problem_type:
        case "vrp" | "tsp":
            vrp = VRP(
                depot_id=depot_id,
                stops=create_simple_stops(stops),
                routes=routes,
            )
        case "cvrp":
            vrp = VRP(
                depot_id=depot_id,
                stops=create_stops_with_capacity(stops),
                routes=routes,
            )
        case "bss":
            vrp = VRP(
                depot_id=depot_id,
                stops=create_stops_with_assigned_passengers(stops),
                passengers=passengers,
            )
        case _:
            print("Tipo de problema no soportado")

    vrp.draw_routes()
    vrp.draw_deposit()
    vrp.draw_stops()
    vrp.draw_graph(x_label, y_label, graph_title)
