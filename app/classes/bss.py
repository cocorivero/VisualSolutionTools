from classes.depto import Depto
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


class BSS:
    def __init__(self, depot_data, bus_stop_data):
        self.depot = Depto(depot_data)
        self.bus_stop_data = bus_stop_data

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

    def draw_bus_stops_with_passengers(self):
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
