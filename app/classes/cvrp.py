from classes.depto import Depto


class CVRP:
    def __init__(
        self,
        depot_index: int,
        locations: list,
        demands: list,
        vehicle_routes_mapping: dict,
    ):
        self.depot = Depto(locations[depot_index], depot_index)
        self.locations = locations
        self.demands = demands
        self.vehicle_routes_mapping = vehicle_routes_mapping
