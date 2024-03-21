import matplotlib.pyplot as plt


# Dibujar el depósito
def draw_deposit(deposit_data, index):
    # Obtener las coordenadas x e y del depósito
    deposit_x = deposit_data[0]
    deposit_y = deposit_data[1]
    # Dibujar el depósito como un círculo negro grande
    plt.plot(deposit_x, deposit_y, marker="o", markersize=15, color="black")
    # Dibujar el depósito como un círculo verde más pequeño dentro del círculo negro
    plt.plot(deposit_x, deposit_y, marker="o", markersize=13, color="green")
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
    for i, location in enumerate(locations, start=1):
        # Obtener las coordenadas x e y del lugar
        x = location[0]
        y = location[1]
        # Dibujar el lugar como un círculo negro grande
        plt.plot(x, y, marker="o", markersize=15, color="black")
        # Dibujar un círculo blanco más pequeño dentro del círculo negro
        plt.plot(x, y, marker="o", markersize=12, color="white")
        # Agregar un texto con el número del lugar en el centro
        plt.text(x, y, str(i), fontsize=8, ha="center", va="center")
        if demands is not None:
            plt.text(
                x,
                y - 30,
                str(demands[i]),
                fontsize=8,
                ha="center",
                va="center",
                color="blue",
            )


# def draw_locations(locations, demands=None):
#     for i, (location) in enumerate(zip(locations), start=1):
# x = location[0]
# y = location[1]
# plt.plot(x, y, marker="o", markersize=15, color="black")
# plt.plot(x, y, marker="o", markersize=12, color="white")
# plt.text(x, y, str(i), fontsize=8, ha="center", va="center")

# if demands is not None:
#     plt.text(
#         x,
#         y - 0.5,
#         str(demands[i]),
#         fontsize=8,
#         ha="center",
#         va="center",
#         color="blue",
#     )


# Crear una leyenda de ciudades con sus índices y nombres
def draw_legend(locations):
    city_legend = [f"{index}: {city}" for index, (_, _, city) in enumerate(locations)]
    # Agregar la leyenda al gráfico con la posición en la esquina superior izquierda
    plt.legend(
        city_legend,
        loc="upper left",
        bbox_to_anchor=(1, 1),
        handlelength=1,
    )


def draw_graph(x_label, y_label, graph_title):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(graph_title)
    plt.gca().set_aspect("equal", adjustable="box")
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()
