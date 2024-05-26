from services.draw_funtions import *
from services.draw_routes import draw_tsp_route, draw_vrp_route, draw_cvrp_route
from classes.tsp import TSP
from classes.vrp import VRP
from classes.cvrp import CVRP


def plot_problem(
    problem_type: str,
    locations: list,
    depot_index: int,
    vehicle_routes_mapping: dict = None,
    demands: list = None,
):
    match problem_type:
        case "tsp":
            tsp = TSP(
                depot_index,
                locations,
                vehicle_routes_mapping,
            )
            draw_locations(filter_locations(tsp.locations, tsp.depot.index))
            draw_deposit(tsp.depot.data, tsp.depot.index)
            draw_tsp_route(tsp.locations, tsp.route)
            draw_graph("Coordinate X", "Coordinate Y", "Travelling Salesperson Problem")
        case "vrp":
            vrp = VRP(
                depot_index,
                locations,
                vehicle_routes_mapping,
            )
            draw_locations(filter_locations(vrp.locations, vrp.depot.index))
            draw_deposit(vrp.depot.data, vrp.depot.index)
            draw_vrp_route(vrp.locations, vrp.vehicle_routes_mapping)
            draw_graph("Coordinate X", "Coordinate Y", "Vehicle Routing Problem")
        case "cvrp":
            cvrp = CVRP(
                depot_index,
                locations,
                demands,
                vehicle_routes_mapping,
            )
            draw_locations(
                filter_locations(cvrp.locations, cvrp.depot.index),
                cvrp.demands,
            )
            draw_deposit(cvrp.depot.data, cvrp.depot.index)
            draw_cvrp_route(cvrp.locations, cvrp.vehicle_routes_mapping)
            draw_graph(
                "Coordinate X", "Coordinate Y", "Capacitated Vehicle Routing Problem"
            )
        case _:
            print("Tipo de problema no soportado")
