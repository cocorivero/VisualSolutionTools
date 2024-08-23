import random
import sys

sys.path.append("./")
from typing import List, Optional, Tuple
from matplotlib import pyplot as plt

from app.classes.stop import Stop
from app.classes.passenger import Passenger


class VRP:
    def __init__(
        self,
        depot_id: str,
        stops: List[Stop],
        routes: Optional[List[str]] = None,
        passengers: Optional[List[Passenger]] = None,
    ):
        self.depot_id: str = depot_id
        self.stops: List[Stop] = stops
        self.routes: List[str] = routes if routes is not None else []
        self.passengers: List[Passenger] = passengers if passengers is not None else []

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

        depot_size = 40
        depot_border_size = 6
        depot_id_size = 35

        deposit_x, deposit_y = self.get_depot_coordinates()
        # Dibujar el depósito como un círculo verde
        plt.plot(
            deposit_x,
            deposit_y,
            marker="o",
            markersize=depot_size + depot_border_size,
            color="black",
        )
        # Dibujar el depósito como un círculo verde más pequeño dentro del círculo negro
        plt.plot(
            deposit_x, deposit_y, marker="o", markersize=depot_size, color="#00FF00"
        )
        # Agregar un texto con el índice en el centro del depósito
        plt.text(
            deposit_x,
            deposit_y,
            str(self.depot_id),
            fontsize=depot_id_size,
            ha="center",
            va="center",
            color="black",
        )

    def draw_stops(self):
        """
        Dibuja todas las paradas excepto el depósito.

        Esta función itera sobre todas las paradas y las dibuja en el gráfico,
        mostrando sus identificadores y, si corresponde, la demanda y los pasajeros asignados.
        """
        stop_size = 35
        stop_border_size = 5
        stop_id_size = 30
        demand_size = 25

        for stop in self.stops:
            if stop.id != self.depot_id:
                stop_x, stop_y = stop.coordinates

                # Dibujar la parada
                plt.plot(
                    stop_x,
                    stop_y,
                    marker="o",
                    markersize=stop_size + stop_border_size,
                    color="black",
                )
                plt.plot(
                    stop_x, stop_y, marker="o", markersize=stop_size, color="white"
                )

                # Agregar el identificador de la parada
                plt.text(
                    stop_x,
                    stop_y,
                    str(stop.id),
                    fontsize=stop_id_size,
                    ha="center",
                    va="center",
                    color="black",
                )

                # Verificar si la parada tiene una demanda
                if stop.capacity:
                    plt.text(
                        stop_x,
                        stop_y
                        - 5,  # Ajustar la posición vertical para mostrar la demanda debajo de la parada
                        str(stop.capacity),  # Convertir la capacidad en una cadena
                        fontsize=demand_size,
                        ha="center",
                        va="top",
                        color="gray",
                    )

                # Dibujar pasajeros asignados a la parada
                if stop.assigned_passengers:
                    for passenger in stop.assigned_passengers:
                        passenger_x, passenger_y = self.get_passenger_by_id(passenger)
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
        basic_colors = [
            "#FF0000",  # Rojo
            # "#00FF00",  # Verde brillante
            # "#0000FF",  # Azul brillante
            # "#FFFF00",  # Amarillo
            # "#FF00FF",  # Magenta
            # "#00FFFF",  # Cian
            # "#800000",  # Marrón
            # "#808000",  # Verde oliva
            # "#008000",  # Verde oscuro
            # "#008080",  # Verde azulado
            # "#000080",  # Azul marino
            # "#800080",  # Púrpura
            # "#FF4500",  # Naranja rojizo
            "#FFD700",  # Oro
            # "#9ACD32",  # Verde lima
            # "#00FA9A",  # Verde medio mar
            # "#4682B4",  # Azul acero
            # "#6A5ACD",  # Azul violeta
            # "#FF69B4",  # Rosa intenso
            # "#FF1493",  # Rosa profundo
        ]
        grosor = 9
        num_colors = len(basic_colors)
        for i, route in enumerate(self.routes):
            color_route = basic_colors[i % num_colors]
            i += 1
            x_coords = []
            y_coords = []
            for stop_id in route:
                stop = next(s for s in self.stops if s.id == stop_id)
                x, y = stop.coordinates
                x_coords.append(x)
                y_coords.append(y)

            plt.plot(
                x_coords,
                y_coords,
                marker="o",
                linestyle="solid",
                color=color_route,
                linewidth=grosor,
            )

            for i in range(len(x_coords) - 1):
                start = (x_coords[i], y_coords[i])
                end = (x_coords[i + 1], y_coords[i + 1])
                midpoint = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
                plt.annotate(
                    "",
                    xy=midpoint,
                    xytext=start,
                    arrowprops=dict(
                        facecolor=color_route,
                        width=1,
                        headwidth=grosor + 10,
                        edgecolor="none",
                    ),
                    zorder=0,
                )

    def get_passenger_by_id(self, passenger_id):
        for passenger in self.passengers:
            if passenger[0] == passenger_id:
                return passenger[1]
        return None

    def random_basic_color(self):
        basic_colors = [
            "#FF0000",  # Rojo
            "#00FF00",  # Verde brillante
            # "#0000FF",  # Azul brillante
            # "#FFFF00",  # Amarillo
            # "#FF00FF",  # Magenta
            # "#00FFFF",  # Cian
            # "#800000",  # Marrón
            # "#808000",  # Verde oliva
            # "#008000",  # Verde oscuro
            # "#008080",  # Verde azulado
            # "#000080",  # Azul marino
            # "#800080",  # Púrpura
            # "#FF4500",  # Naranja rojizo
            # "#FFD700",  # Oro
            # "#9ACD32",  # Verde lima
            # "#00FA9A",  # Verde medio mar
            # "#4682B4",  # Azul acero
            # "#6A5ACD",  # Azul violeta
            # "#FF69B4",  # Rosa intenso
            # "#FF1493",  # Rosa profundo
        ]
        return random.choice(basic_colors)
