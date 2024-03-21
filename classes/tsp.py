from .depot import Depto


class TSP:
    def __init__(self, depot: Depto, locations: list, route: list):
        self.depot = depot
        self.locations = locations
        self.route = route
