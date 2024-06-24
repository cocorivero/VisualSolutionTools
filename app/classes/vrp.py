import sys

sys.path.append("./")
from typing import List, Optional, Tuple

from matplotlib import pyplot as plt
from sympy import Line2D
from app.classes.stop import Stop


class VRP:
    def __init__(self, depot_id: str, stops: List[Stop], routes: Optional[List[str]]):
        """
        Initialize the VRP with a depot, list of stops, and list of routes.

        :param depot: Depot object
        :param stops: List of Stop objects
        :param routes: List of route IDs (each route is represented as a list of stop IDs)
        """
        self.depot_id: str = depot_id
        self.stops: List[Stop] = stops
        self.routes: List[str] = routes if routes is not None else []

    def get_depot_coordinates(self) -> Tuple[float, float]:
        """
        Obtiene las coordenadas del depósito de la lista de paradas.
        :return: Un tupla con las coordenadas (latitud, longitud) del depósito
        """
        depot_stop = next(stop for stop in self.stops if stop.id == self.depot_id)
        return depot_stop.coordinates

    def draw_graph(self, x_label, y_label, graph_title):
        """Configura y muestra el gráfico con etiquetas y título."""
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(graph_title)
        plt.tight_layout()
        plt.show(block=False)
        plt.show()

    def draw_deposit(self):
        """Dibuja el depósito en un gráfico."""
        deposit_x, deposit_y = self.get_depot_coordinates()
        # Dibujar el depósito como un círculo verde
        plt.plot(deposit_x, deposit_y, marker="o", markersize=15, color="green")
        # Dibujar el depósito como un círculo verde más pequeño dentro del círculo negro
        plt.plot(deposit_x, deposit_y, marker="o", markersize=12, color="#00FF00")
        # Agregar un texto con el índice en el centro del depósito
        plt.text(
            deposit_x,
            deposit_y,
            str(self.depot_id),
            fontsize=8,
            ha="center",
            va="center",
        )

    def draw_stops(self):
        """
        Dibuja todas las paradas excepto el depósito.

        Esta función itera sobre todas las paradas y las dibuja en el gráfico,
        mostrando sus identificadores y, si corresponde, la demanda y los pasajeros asignados.
        """
        for stop in self.stops:
            if stop.id != self.depot_id:
                stop_x, stop_y = stop.coordinates

                # Dibujar la parada
                plt.plot(stop_x, stop_y, marker="o", markersize=14, color="black")
                plt.plot(stop_x, stop_y, marker="o", markersize=12, color="white")

                # Agregar el identificador de la parada
                plt.text(
                    stop_x,
                    stop_y,
                    str(stop.id),
                    fontsize=8,
                    ha="center",
                    va="center",
                    color="blue",
                )

                # Verificar si la parada tiene una demanda
                if stop.capacity:
                    plt.text(
                        stop_x,
                        stop_y
                        - 0.1,  # Ajustar la posición vertical para mostrar la demanda debajo de la parada
                        str(stop.capacity),  # Convertir la capacidad en una cadena
                        fontsize=6,
                        ha="center",
                        va="top",
                        color="red",
                    )

                # Dibujar pasajeros asignados a la parada
                if stop.assigned_passengers:
                    for passenger_x, passenger_y in stop.assigned_passengers:
                        plt.plot(
                            passenger_x,
                            passenger_y,
                            marker="o",
                            markersize=5,
                            color="black",
                        )
                        plt.plot(
                            passenger_x,
                            passenger_y,
                            marker="o",
                            markersize=3,
                            color="red",
                        )
                        plt.plot(
                            [stop_x, passenger_x],
                            [stop_y, passenger_y],
                            linestyle="--",
                            color="gray",
                        )

    def draw_routes(self):
        """Dibuja las rutas del problema VRP utilizando matplotlib."""
        for route in self.routes:
            x_coords = []
            y_coords = []
            for stop_id in route:
                stop = next(s for s in self.stops if s.id == stop_id)
                x, y = stop.coordinates
                x_coords.append(x)
                y_coords.append(y)

            plt.plot(x_coords, y_coords, marker="o", linestyle="-", color="gray")

    def draw_stops_with_passengers(self):
        for stop_data in self.bus_stop_data:
            stop_x, stop_y = stop_data["stop_coordinates"]
            passenger_coordinates = stop_data["passenger_coordinates"]

            # Dibujar la parada de autobús

            plt.plot(stop_x, stop_y, marker="o", markersize=14, color="black")
            plt.plot(stop_x, stop_y, marker="o", markersize=12, color="white")

            # Dibujar las coordenadas de los pasajeros asignados a esa parada
            for passenger_coord in passenger_coordinates:
                passenger_x, passenger_y = passenger_coord
                plt.plot(
                    passenger_x, passenger_y, marker="o", markersize=5, color="black"
                )
                plt.plot(
                    passenger_x, passenger_y, marker="o", markersize=3, color="red"
                )

                # Dibujar una línea discontinua que conecta la parada de autobús con el pasajero asignado
                line = Line2D(
                    [stop_x, passenger_x],
                    [stop_y, passenger_y],
                    linestyle="--",
                    color="gray",
                )
                plt.gca().add_line(line)

