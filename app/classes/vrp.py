from classes.depto import Depto


class VRP:
    def __init__(self, depot_index: int, locations: list, vehicle_routes_mapping: dict):
        self.depot = Depto(locations[depot_index], depot_index)
        self.locations = locations
        self.vehicle_routes_mapping = vehicle_routes_mapping
