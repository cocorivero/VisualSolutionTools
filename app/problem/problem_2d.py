from app.problem.problem import Problem
from app.models.vrp import VRP
from app.models.stop import Stop
from app.models.passenger import Passenger
from app.models.depot import Depot
from app.models.route import Route
import random


class Problem2D(Problem):

    def create_problem(
        self,
        problem_type,
        problem_name,
        depot_id,
        stops,
        routes,
        passengers,
        depot_config,
        stop_config,
        routes_config,
    ):
        # Definimos argumentos adicionales para la creación de paradas
        stop_args = {
            "with_capacity": problem_type in ["cvrp", "bss", "sbrp"],
            "with_assigned_passengers": problem_type in ["bss", "sbrp"],
        }

        # Creamos los objetos necesarios usando las fábricas
        depot = self.create_depot(depot_id=depot_id, stops=stops, config=depot_config)
        stops = self.create_stops(stop_data=stops, stop_config=stop_config, **stop_args)
        routes = self.create_routes(routes=routes, routes_config=routes_config)

        # Creamos los argumentos para la instancia de VRP
        vrp_args = {
            "problem_name": problem_name,
            "depot": depot,
            "stops": stops,
            "routes": routes,
        }

        # Agregamos pasajeros si el problema lo requiere
        if problem_type in ["bss", "sbrp"]:
            vrp_args["passengers"] = passengers

        # Verificamos si el tipo de problema es soportado y creamos la instancia de VRP
        if problem_type in ["vrp", "tsp", "cvrp", "bss", "sbrp"]:
            return VRP(**vrp_args)
        else:
            print("Tipo de problema no soportado")
            return None

    def create_depot(self, depot_id, stops, config):
        coordinates = stops.get(depot_id, {}).get("coordinates")
        if not coordinates:
            raise ValueError(
                f"Depot ID {depot_id} no encontrado en los datos de stops."
            )
        return Depot(
            id=depot_id,
            coordinates=coordinates,
            size=config.get("depot_size", 18),
            marker_type=config.get("depot_marker_type", "o"),
            marker_color=config.get("depot_marker_color", "lime"),
            marker_border=config.get("depot_marker_border", 2),
            marker_border_color=config.get("depot_marker_border_color", "black"),
            font_color=config.get("depot_font_color", "black"),
            font_size=config.get("depot_font_size", 12),
        )

    def create_routes(self, routes, routes_config):
        custom_colors_list = routes_config.get(
            "custom_colors_list",
            [
                "#FF0000",
                "#00FF00",
                "#0000FF",
                "#800000",
                "#FF00FF",
                "#FFFF00",
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
                thickness=routes_config.get("route_thickness", 1),
            )
            created_routes.append(route)

        return created_routes

    def create_stops(
        self,
        stop_data,
        stop_config,
        with_capacity=False,
        with_assigned_passengers=False,
    ):
        def create_passengers(passenger_data):
            return [
                Passenger(id=passenger_id, coordinates=coordinates)
                for passenger_id, coordinates in passenger_data
            ]

        stops = []
        for stop_id, data in stop_data.items():
            assigned_passengers = (
                create_passengers(data["passengers"])
                if with_assigned_passengers
                else []
            )
            stop = Stop(
                id=str(stop_id),
                coordinates=data["coordinates"],
                size=stop_config.get("stop_size", 15),
                marker_type=stop_config.get("stop_marker_type", "o"),
                marker_color=stop_config.get("stop_marker_color", "white"),
                marker_border=stop_config.get("stop_marker_border", 2),
                marker_border_color=stop_config.get(
                    "stop_marker_border_color", "black"
                ),
                font_color=stop_config.get("stop_font_color", "black"),
                font_size=stop_config.get("stop_font_size", 8),
                demand_size=stop_config.get("stop_demand_size", 8),
                demand_color=stop_config.get("stop_demand_color", "red"),
                marker_passenger_type=stop_config.get(
                    "stop_marker_passenger_type", "o"
                ),
                marker_passenger_size=stop_config.get("stop_marker_passenger_size", 5),
                marker_passenger_color=stop_config.get(
                    "stop_marker_passenger_color", "red"
                ),
                marker_passenger_border=stop_config.get(
                    "stop_marker_passenger_border", 1
                ),
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
