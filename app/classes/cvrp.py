import sys

sys.path.append("./")

import random
import matplotlib.pyplot as plt

# from app.services.draw_routes import draw_route
from app.classes.vehicle_routing_problem import VehicleRoutingProblem


class CVRP(VehicleRoutingProblem):
    def __init__(
        self,
        depot_index: int,
        locations: list,
        vehicle_routes_mapping: dict,
        demands: list,
    ):
        super().__init__(depot_index, locations, vehicle_routes_mapping)
        self.demands = demands

    def draw_locations(self):
        """Dibuja todos los lugares que no son el depósito."""
        filtered_locations = [
            location
            for index, location in enumerate(self.locations)
            if index != self.depot.index
        ]

        for i, location in enumerate(filtered_locations):
            x = location[0]
            y = location[1]
            # Dibujar el lugar como un círculo negro grande
            plt.plot(x, y, marker="o", markersize=14, color="black")
            # Dibujar un círculo blanco más pequeño dentro del círculo negro
            plt.plot(x, y, marker="o", markersize=12, color="white")
            # Agregar texto con la demanda en el centro del lugar
            plt.text(
                x,
                y - 5,
                str(self.demands[i]),
                fontsize=8,
                ha="center",
                va="center",
                color="blue",
            )

    # Dibuja la ruta del VRP
    def draw_cvrp_route(self):
        for route in self.vehicle_routes_mapping.items():
            if route[1] == [0, 0]:
                continue
            color = "#" + "".join([random.choice("0123456789ABCDEF") for _ in range(6)])
            self.draw_route(route[1], color)
