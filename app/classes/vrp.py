import sys

sys.path.append("./")

import random

# from app.services.draw_routes import draw_route
from app.classes.vehicle_routing_problem import VehicleRoutingProblem


class VRP(VehicleRoutingProblem):

    # Dibuja la ruta del VRP
    def draw_vrp_route(self):
        for route in self.vehicle_routes_mapping.items():
            if route[1] == [0, 0]:
                continue
            color = "#" + "".join([random.choice("0123456789ABCDEF") for _ in range(6)])
            self.draw_route(route[1], color)
