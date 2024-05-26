from classes.depto import Depto


class VRP:
    def __init__(self, depot: Depto, locations: list, vehicle_routes_mapping: dict):
        self.depot = depot
        self.locations = locations
        self.vehicle_routes_mapping = vehicle_routes_mapping
