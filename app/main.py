# from services.draw_routes import draw_tsp_route, draw_vrp_route, draw_cvrp_route
from classes.vrp import VRP
from classes.cvrp import CVRP
from classes.bss import BSS


def plot_problem(
    problem_type: str,
    locations: list = None,
    depot_data: tuple = None,
    depot_index: int = None,
    vehicle_routes_mapping: dict = None,
    demands: list = None,
    bus_stop_data: list = None,
):
    match problem_type:
        case "vrp":
            vrp = VRP(
                depot_index,
                locations,
                vehicle_routes_mapping,
            )
            vrp.draw_locations()
            vrp.draw_deposit()
            vrp.draw_vrp_route()
            vrp.draw_graph("Coordinate X", "Coordinate Y", "Vehicle Routing Problem")
        case "cvrp":
            cvrp = CVRP(depot_index, locations, vehicle_routes_mapping, demands)
            cvrp.draw_locations()
            cvrp.draw_deposit()
            cvrp.draw_cvrp_route()
            cvrp.draw_graph(
                "Coordinate X", "Coordinate Y", "Capacitated Vehicle Routing Problem"
            )
        case "bss":
            bss = BSS(depot_data, bus_stop_data)
            bss.draw_deposit()
            bss.draw_bus_stops_with_passengers()
            bss.draw_graph("Coordinate X", "Coordinate Y", "Bus Stop Selection")
        case _:
            print("Tipo de problema no soportado")
