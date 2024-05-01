class Depto:
    def __init__(self, data: tuple, index: int):
        self.data = data
        self.index = index

    def get_depot_name(self):
        return self.data[2]

    def get_depot_coordinates(self):
        return self.data[:2]


class VehicleRoutingProblem:
    def __init__(self, depot: Depto, locations: list, **kwargs):
        self.depot = depot
        self.locations = locations
        for key, value in kwargs.items():
            setattr(self, key, value)


class TSP(VehicleRoutingProblem):
    def __init__(self, depot: Depto, locations: list, route: dict):
        super().__init__(depot, locations, route=route)


class VRP(VehicleRoutingProblem):
    def __init__(self, depot: Depto, locations: list, vehicle_routes_mapping: dict):
        super().__init__(
            depot, locations, vehicle_routes_mapping=vehicle_routes_mapping
        )


class CVRP(VehicleRoutingProblem):
    def __init__(
        self, depot: Depto, locations: list, demands: list, vehicle_routes_mapping: dict
    ):
        super().__init__(
            depot,
            locations,
            demands=demands,
            vehicle_routes_mapping=vehicle_routes_mapping,
        )
