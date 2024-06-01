import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# Dibujar el depósito
def draw_deposit(deposit_data, index=0):
    # Obtener las coordenadas x e y del depósito
    deposit_x = deposit_data[0]
    deposit_y = deposit_data[1]
    # Dibujar el depósito como un círculo negro grande
    plt.plot(deposit_x, deposit_y, marker="o", markersize=15, color="green")
    # Dibujar el depósito como un círculo verde más pequeño dentro del círculo negro
    plt.plot(deposit_x, deposit_y, marker="o", markersize=12, color="#00FF00")
    # Agregar un texto con el índice en el centro del depósito
    plt.text(
        deposit_x,
        deposit_y,
        index,
        fontsize=8,
        ha="center",
        va="center",
    )


# Filtra los lugares excluyendo el depósito basado en su índice
def filter_locations(locations, depot_index):
    return [
        location for index, location in enumerate(locations) if index != depot_index
    ]


# Dibujar todos los lugares que no son el depósito
def draw_locations(locations, demands=None):
    # x = [point[0] for point in locations]
    # y = [point[1] for point in locations]
    # # Crear la gráfica de dispersión
    # plt.scatter(x, y, color="blue", marker="o")

    for i, location in enumerate(locations, start=1):
        # Obtener las coordenadas x e y del lugar
        x = location[0]
        y = location[1]
        # Dibujar el lugar como un círculo negro grande
        plt.plot(x, y, marker="o", markersize=14, color="black")
        # Dibujar un círculo blanco más pequeño dentro del círculo negro
        plt.plot(x, y, marker="o", markersize=12, color="white")
        # Agregar un texto con el número del lugar en el centro
        # plt.text(x, y, str(i), fontsize=8, ha="center", va="center")
        if demands is not None:
            plt.text(
                x,
                y - 5,
                str(demands[i]),
                fontsize=8,
                ha="center",
                va="center",
                color="blue",
            )


def draw_graph(x_label, y_label, graph_title):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(graph_title)
    plt.tight_layout()
    plt.show(block=False)
    plt.show()


def draw_bus_stops_with_passengers(bus_stop_data):
    for stop_data in bus_stop_data:
        stop_x, stop_y = stop_data["stop_coordinates"]
        passenger_coordinates = stop_data["passenger_coordinates"]

        # Dibujar la parada de autobús

        plt.plot(stop_x, stop_y, marker="o", markersize=14, color="black")
        plt.plot(stop_x, stop_y, marker="o", markersize=12, color="white")

        # Dibujar las coordenadas de los pasajeros asignados a esa parada
        for passenger_coord in passenger_coordinates:
            passenger_x, passenger_y = passenger_coord
            plt.plot(passenger_x, passenger_y, marker="o", markersize=5, color="black")
            plt.plot(passenger_x, passenger_y, marker="o", markersize=3, color="red")

            # Dibujar una línea discontinua que conecta la parada de autobús con el pasajero asignado
            line = Line2D(
                [stop_x, passenger_x],
                [stop_y, passenger_y],
                linestyle="--",
                color="gray",
            )
            plt.gca().add_line(line)
