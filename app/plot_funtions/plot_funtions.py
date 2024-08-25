import sys
from app.classes.vrp import VRP
from app.classes.stop import Stop
from app.classes.depot import Depot
from app.classes.route import Route
from app.classes.passenger import Passenger
from matplotlib import pyplot as plt
import random
from typing import List, Tuple, Dict

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
    vrp_args = {
        "depot": create_depot(
            depot_id=depot_id, stops=stops, depot_config=depot_config
        ),
        "stops": create_stops(stop_data=stops, stop_config=stop_config, **stop_args),
        "routes": create_routes(routes=routes, routes_config=routes_config),
    }
    if problem_type in ["bss", "sbrp"]:
        vrp_args["passengers"] = passengers

    if problem_type in ["vrp", "tsp", "cvrp", "bss", "sbrp"]:
        vrp = VRP(**vrp_args)
        create_graph(vrp, graph_title)
    else:
        print("Tipo de problema no soportado")


def create_depot(
    depot_id: str,
    stops: Dict[str, Dict[str, Tuple[float, float]]],
    depot_config: Dict,
) -> Depot:
    coordinates = stops.get(depot_id, {}).get("coordinates")
    if not coordinates:
        raise ValueError(f"Depot ID {depot_id} no encontrado en los datos de stops.")
    return Depot(
        id=depot_id,
        coordinates=coordinates,
        size=depot_config.get("depot_size", 18),
        marker_type=depot_config.get("depot_marker_type", "o"),
        marker_color=depot_config.get("depot_marker_color", "lime"),
        marker_border=depot_config.get("depot_marker_border", 2),
        marker_border_color=depot_config.get("depot_marker_border_color", "black"),
        font_color=depot_config.get("depot_font_color", "black"),
        font_size=depot_config.get("depot_font_size", 12),
    )


def create_stops(
    stop_data: Dict[str, Dict[str, Tuple[float, float]]],
    stop_config: Dict,
    with_capacity: bool = False,
    with_assigned_passengers: bool = False,
) -> List[Stop]:
    stops = []
    for stop_id, data in stop_data.items():
        assigned_passengers = (
            create_passengers(data["passengers"]) if with_assigned_passengers else []
        )
        stop = Stop(
            id=str(stop_id),
            coordinates=data["coordinates"],
            size=stop_config.get("stop_size", 15),
            marker_type=stop_config.get("stop_marker_type", "o"),
            marker_color=stop_config.get("stop_marker_color", "white"),
            marker_border=stop_config.get("stop_marker_border", 2),
            marker_border_color=stop_config.get("stop_marker_border_color", "black"),
            font_color=stop_config.get("stop_font_color", "black"),
            font_size=stop_config.get("stop_font_size", 8),
            demand_size=stop_config.get("stop_demand_size", 8),
            demand_color=stop_config.get("stop_demand_color", "black"),
            marker_passenger_type=stop_config.get("stop_marker_passenger_type", "o"),
            marker_passenger_size=stop_config.get("stop_marker_passenger_size", 5),
            marker_passenger_color=stop_config.get(
                "stop_marker_passenger_color", "red"
            ),
            marker_passenger_border=stop_config.get("stop_marker_passenger_border", 1),
            marker_passenger_border_color=stop_config.get(
                "passenger_route_color", "black"
            ),
            passenger_route_style=stop_config.get("passenger_route_style", "--"),
            passenger_route_color=stop_config.get("passenger_route_color", "grey"),
            capacity=data.get("capacity") if with_capacity else None,
            assigned_passengers=assigned_passengers,
        )
        stops.append(stop)
    return stops


def create_passengers(
    passenger_data: List[Tuple[str, Tuple[float, float]]]
) -> List[Passenger]:
    return [
        Passenger(id=passenger_id, coordinates=coordinates)
        for passenger_id, coordinates in passenger_data
    ]


def create_routes(routes: List, routes_config: Dict) -> List[Route]:
    custom_colors_list = routes_config.get(
        "custom_colors_list",
        [
            "#FF0000",
            "#00FF00",
            "#0000FF",
            "#FFFF00",
            "#FF00FF",
            "#00FFFF",
            "#800000",
            "#808000",
            "#008000",
            "#008080",
            "#000080",
            "#800080",
            "#FF4500",
            "#FFD700",
            "#9ACD32",
            "#00FA9A",
            "#4682B4",
            "#6A5ACD",
            "#FF69B4",
            "#FF1493",
        ],
    )

    num_colors = len(custom_colors_list)
    created_routes = []

    for i, stops in enumerate(routes):
        if routes_config.get("random_colors", False):
            color = random.choice(custom_colors_list)
        else:
            color = custom_colors_list[i % num_colors]

        route = Route(
            route_id=i + 1,
            stops=stops,
            line_style=routes_config.get("route_line_style", "solid"),
            color=color,
            thickness=routes_config.get("route_thickness", 2),
        )
        created_routes.append(route)

    return created_routes


def create_graph(vrp: VRP, graph_title):
    vrp.draw_routes()
    vrp.draw_stops()
    vrp.draw_deposit()
    vrp.draw_legend()
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.title(graph_title)
    plt.tight_layout()
    plt.show()
