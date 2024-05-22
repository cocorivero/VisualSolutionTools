from classes.depto import Depto


class TSP:
    def __init__(self, depot: Depto, locations: list, route: dict):
        self.depot = depot
        self.locations = locations
        self.route = route
