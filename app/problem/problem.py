from app.problem.vrp_2d import VRP_2D
from app.problem.vrp_map import VRP_MAP
from app.models.stop import Stop
from app.models.passenger import Passenger
from app.models.depot import Depot
from app.models.route import Route
from app.utils.utils import get_route_color


class Problem:

    def create_problem(
        self,
        view_mode,
        problem_type,
        problem_name,
        depot_id,
        stops,
        routes,
        passengers,
        depot_config,
        stop_config,
        routes_config,
        passenger_config,
    ):

        # Create the required objects using the factory methods
        depot = self.create_depot(
            depot_id=depot_id, stops=stops, config=depot_config, view_mode=view_mode
        )
        stops = self.create_stops(
            stop_data=stops, stop_config=stop_config, view_mode=view_mode
        )
        routes = self.create_routes(
            routes=routes, routes_config=routes_config, view_mode=view_mode
        )

        # Create the arguments for the VRP instance
        vrp_args = {
            "problem_name": problem_name,
            "depot": depot,
            "stops": stops,
            "routes": routes,
        }

        # Add passengers if the problem requires it
        if problem_type in ["bss", "sbrp"]:
            vrp_args["passengers"] = self.create_passengers(
                passengers, passenger_config, view_mode=view_mode
            )
        # Check if the problem type is supported and create the VRP instance
        if problem_type in ["vrp", "tsp", "cvrp", "bss", "sbrp"]:
            if view_mode == "2d":
                return VRP_2D(**vrp_args)
            elif view_mode == "map":
                return VRP_MAP(**vrp_args)
        else:
            print("Tipo de problema no soportado")
            return None

    def create_depot(self, depot_id, stops, config, view_mode):
        coords = stops.get(depot_id, {}).get("coords")
        if not coords:
            raise ValueError(
                f"Depot ID {depot_id} no encontrado en los datos de stops."
            )
        return Depot(
            id=depot_id, coords=coords, depot_config=config, view_mode=view_mode
        )

    def create_routes(self, routes, routes_config, view_mode):
        created_routes = []
        for i, stops in enumerate(routes):
            color = get_route_color(i, routes_config)
            route_config = {**routes_config, "default_color": color}
            route = Route(
                route_id=i + 1,
                stops=stops,
                routes_config=route_config,
                view_mode=view_mode,
            )
            created_routes.append(route)

        return created_routes

    def create_stops(self, stop_data, stop_config, view_mode):
        stops = []
        for stop_id, data in stop_data.items():
            assigned_passengers = (
                [passenger for passenger in data["passengers"]]
                if "passengers" in data
                else []
            )
            stop = Stop(
                id=str(stop_id),
                coords=data["coords"],
                stop_config=stop_config,
                assigned_passengers=assigned_passengers,
                capacity=data.get("capacity"),
                view_mode=view_mode,
            )
            stops.append(stop)
        return stops

    def create_passengers(self, passenger_list, passenger_config, view_mode):
        return [
            Passenger(pid, coords, passenger_config, view_mode)
            for pid, coords in passenger_list
        ]
