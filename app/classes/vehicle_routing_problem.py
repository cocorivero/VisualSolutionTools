import sys

sys.path.append("./")

from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import random

from classes.depto import Depto

# from app.services.draw_routes import draw_route


class VehicleRoutingProblem(ABC):
    def __init__(self, depot_index: int, locations: list, vehicle_routes_mapping: dict):
        self.depot = Depto(locations[depot_index], depot_index)
        self.locations = locations
        self.vehicle_routes_mapping = vehicle_routes_mapping

    def draw_deposit(self):
        """Dibuja el depósito en un gráfico."""
        deposit_x = self.depot.data[0]
        deposit_y = self.depot.data[1]
        # Dibujar el depósito como un círculo verde
        plt.plot(deposit_x, deposit_y, marker="o", markersize=15, color="green")
        # Dibujar el depósito como un círculo verde más pequeño dentro del círculo negro
        plt.plot(deposit_x, deposit_y, marker="o", markersize=12, color="#00FF00")
        # Agregar un texto con el índice en el centro del depósito
        plt.text(
            deposit_x,
            deposit_y,
            str(self.depot.index),
            fontsize=8,
            ha="center",
            va="center",
        )

    def draw_locations(self):
        """Dibuja todos los lugares que no son el depósito."""
        filtered_locations = [
            location
            for index, location in enumerate(self.locations)
            if index != self.depot.index
        ]

        for location in filtered_locations:
            x = location[0]
            y = location[1]
            # Dibujar el lugar como un círculo negro grande
            plt.plot(x, y, marker="o", markersize=14, color="black")
            # Dibujar un círculo blanco más pequeño dentro del círculo negro
            plt.plot(x, y, marker="o", markersize=12, color="white")

    def draw_graph(self, x_label, y_label, graph_title):
        """Configura y muestra el gráfico con etiquetas y título."""
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(graph_title)
        plt.tight_layout()
        plt.show(block=False)
        plt.show()

    def draw_route(self, route, color_line="blue", displacement=0.05):
        """Dibuja una ruta en el gráfico."""
        for i in range(len(route) - 1):
            # Obtener las coordenadas del punto de inicio y punto final
            start_point = self.locations[route[i]]
            end_point = self.locations[route[i + 1]]

            # Calcular el vector de dirección
            dx = end_point[0] - start_point[0]
            dy = end_point[1] - start_point[1]
            distance = (dx**2 + dy**2) ** 0.5

            # Calcular el factor de desplazamiento
            dx_displacement = displacement * (dx / distance)
            dy_displacement = displacement * (dy / distance)

            # Calcular nuevas coordenadas con desplazamiento
            start_point_displaced = (
                start_point[0] + dx_displacement,
                start_point[1] + dy_displacement,
            )
            end_point_displaced = (
                end_point[0] - dx_displacement,
                end_point[1] - dy_displacement,
            )

            # Dibujar la flecha entre los puntos desplazados
            plt.annotate(
                "",
                xy=end_point_displaced,
                xytext=start_point_displaced,
                arrowprops=dict(arrowstyle="->", color=color_line),
            )

        # Añadir los números a cada nodo
        for idx, point in enumerate(route[1:-1], start=1):
            x, y = self.locations[point]
            plt.text(
                x, y, str(idx), fontsize=8, ha="center", va="center", color="black"
            )
