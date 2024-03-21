from .depot import Depto


class CVRP:
    def __init__(
        self, depot: Depto, locations: list, demands: list, vehicle_routes_mapping: dict
    ):
        self.depot = depot
        self.locations = locations
        self.demands = demands
        self.vehicle_routes_mapping = vehicle_routes_mapping
