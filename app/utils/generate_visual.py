import sys

sys.path.append("./")

from app.classes.vrp import VRP
from app.classes.stop import Stop
from typing import List


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
                stops=create_stops(stops),
                routes=routes,
            )
        case "cvrp":
            vrp = VRP(
                depot_id=depot_id,
                stops=create_stops(stops, with_capacity=True),
                routes=routes,
            )
        case "bss":
            vrp = VRP(
                depot_id=depot_id,
                stops=create_stops(
                    stops, with_capacity=True, with_assigned_passengers=True
                ),
                passengers=passengers,
            )
        case _:
            print("Tipo de problema no soportado")

    vrp.draw_routes()
    vrp.draw_deposit()
    vrp.draw_stops()
    vrp.draw_graph(x_label, y_label, graph_title)


def create_stops(
    stop_data,
    with_capacity: bool = False,
    with_assigned_passengers: bool = False,
) -> List[Stop]:
    stops = []
    for stop_id, data in stop_data.items():
        stop = Stop(
            id=str(stop_id),
            coordinates=data["coordinates"],
            capacity=data["capacity"] if with_capacity else None,
            assigned_passengers=(
                data["passenger_ids"] if with_assigned_passengers else None
            ),
        )
        stops.append(stop)
    return stops
