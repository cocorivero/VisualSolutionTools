import sys

sys.path.append("./")

import matplotlib.pyplot as plt

from instances_problems import create_data_model_tsp, create_data_solution_tsp
from services.draw_funtions import *
from services.draw_routes import draw_tsp_route
from classes.vehicle_routing_problem_classes import Depto, TSP


# Crear el modelo de datos
data = create_data_model_tsp()
solution = create_data_solution_tsp()

# Crear instancia de la clase TSP con la instancia de Depto, datos de lugares y la ruta
tsp_problem = TSP(
    Depto(data["locations"][data["depot"]], data["depot"]),
    data["locations"],
    solution["route"],
)


def plot_nodes_and_route(depot: Depto, locations, route):
    # Graficar las ciudades y la ruta
    plt.figure("Problema del Viajante de Comercio", figsize=(8, 6))

    # Dibujar la ruta con flechas y los índices de los lugares
    draw_tsp_route(locations, route)

    # Dibujar el depósito
    # draw_deposit(tsp_problem.depot.data, tsp_problem.depot.index)
    draw_deposit(depot.data, depot.index)

    # Dibujar los demás lugares como círculos con los índices en su interior
    draw_locations(filter_locations(locations, depot.index))

    # Crear la leyenda de la ciudad correspondiente a cada índice
    # draw_legend(locations)

    # Configurar el gráfico
    draw_graph("Coordinate X", "Coordinate Y", "Travelling Salesperson Problem")


plot_nodes_and_route(
    tsp_problem.depot,
    tsp_problem.locations,
    tsp_problem.route,
)
