from classes.depto import Depto


class TSP:
    def __init__(self, depot_index: int, locations: list, route: dict):
        self.depot = Depto(locations[depot_index], depot_index)
        self.locations = locations
        self.route = route
