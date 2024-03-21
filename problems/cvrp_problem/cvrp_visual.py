import sys

sys.path.append("./")

import matplotlib.pyplot as plt

from cvrp_data import main_cvrp, create_data_model
from services.draw_funtions import *
from services.draw_routes import draw_cvrp_route
from classes.depot import Depto
from classes.vehicle_routing_problem_classes import CVRP


# # Crear el modelo de datos
data = create_data_model()

# Crear instancia de la clase TSP con la instancia de Depto, datos de lugares y la ruta
cvrp_problem = CVRP(
    Depto(data["locations"][data["deposito"]], data["deposito"]),
    data["locations"],
    data["demanda"],
    main_cvrp(),
)


def plot_nodes_and_route(depot: Depto, locations, demands, vehicle_routes_mapping):
    # Graficar las ciudades y la ruta
    plt.figure("Problema del Viajante de Comercio", figsize=(8, 6))

    # Dibujar la ruta con flechas y los índices de los lugares
    draw_cvrp_route(locations, vehicle_routes_mapping)

    # Dibujar el depósito
    # draw_deposit(tsp_problem.depot.data, tsp_problem.depot.index)
    draw_deposit(depot.data, depot.index)

    # Dibujar los demás lugares como círculos con los índices en su interior
    draw_locations(filter_locations(locations, depot.index), demands)

    # Crear la leyenda de la ciudad correspondiente a cada índice
    # draw_legend(locations)

    # Configurar el gráfico
    draw_graph("Coordinate X", "Coordinate Y", "Capacited Vehicle Routing Problem")


plot_nodes_and_route(
    cvrp_problem.depot,
    cvrp_problem.locations,
    cvrp_problem.demands,
    cvrp_problem.vehicle_routes_mapping,
)
