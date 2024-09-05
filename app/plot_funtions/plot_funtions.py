import sys
from app.classes.vrp import VRP
from app.classes.depot.depot_factory import ConcreteDepotFactory
from app.classes.stop.stop_factory import ConcreteStopFactory
from app.classes.route.route_factory import ConcreteRouteFactory
from matplotlib import pyplot as plt
from typing import List, Dict

sys.path.append("./")


def plot_problem(
    problem_type: str,
    data,
    routes: List = [],
    depot_config: Dict = None,
    stop_config: Dict = None,
    routes_config: Dict = None,
    graph_title: str = None,
):
    default_graph_titles = {
        "tsp": "Traveling Salesman Problem (TSP)",
        "vrp": "Vehicle Routing Problem (VRP)",
        "cvrp": "Capacitated Vehicle Routing Problem (CVRP)",
        "bss": "Bus Stops Selector (BSS)",
        "sbrp": "School Bus Routing Problem (SBRP)",
    }

    graph_title = graph_title or default_graph_titles.get(
        problem_type, "Tipo de problema no soportado"
    )

    if graph_title == "Tipo de problema no soportado":
        print(graph_title)
        return

    create_problem(
        problem_type=problem_type,
        depot_id=data.get("depot_id", ""),
        stops=data.get("locations", {}),
        routes=routes,
        passengers=data.get("passengers", []),
        graph_title=graph_title,
        depot_config=depot_config or {},
        stop_config=stop_config or {},
        routes_config=routes_config or {},
    )


def create_problem(
    problem_type: str,
    depot_id: str,
    stops: Dict,
    graph_title: str,
    depot_config: Dict,
    stop_config: Dict,
    routes_config: Dict,
    routes: List = [],
    passengers: List = [],
):
    stop_args = {
        "with_capacity": problem_type in ["cvrp", "bss", "sbrp"],
        "with_assigned_passengers": problem_type in ["bss", "sbrp"],
    }

    depot_factory = ConcreteDepotFactory()
    stop_factory = ConcreteStopFactory()
    route_factory = ConcreteRouteFactory()

    vrp_args = {
        "depot": depot_factory.create_depot(
            depot_id=depot_id, stops=stops, config=depot_config
        ),
        "stops": stop_factory.create_stops(
            stop_data=stops, stop_config=stop_config, **stop_args
        ),
        "routes": route_factory.create_routes(
            routes=routes, routes_config=routes_config
        ),
    }

    if problem_type in ["bss", "sbrp"]:
        vrp_args["passengers"] = passengers

    if problem_type in ["vrp", "tsp", "cvrp", "bss", "sbrp"]:
        vrp = VRP.get_instance(**vrp_args)
        create_graph(vrp, graph_title)
    else:
        print("Tipo de problema no soportado")


def create_graph(vrp: VRP, graph_title):
    vrp.draw_routes()
    vrp.draw_stops()
    vrp.draw_depot()
    vrp.draw_legend()
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.title(graph_title)
    plt.tight_layout()
    plt.show()
