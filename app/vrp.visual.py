import sys

sys.path.append("./")

import matplotlib.pyplot as plt

from instances_problems import create_data_model_vrp, create_data_solution_vrp
from services.draw_funtions import *
from services.draw_routes import draw_vrp_route
from classes.vehicle_routing_problem_classes import Depto, VRP


# Crear el modelo de datos
data = create_data_model_vrp()
solution = create_data_solution_vrp()

# Crear instancia de la clase TSP con la instancia de Depto, datos de lugares y la ruta
vrp_problem = VRP(
    Depto(data["locations"][data["depot"]], data["depot"]),
    data["locations"],
    solution["vehicle_routes_mapping"],
)


def plot_nodes_and_route(depot: Depto, locations, vehicle_routes_mapping):
    # Graficar las ciudades y la ruta
    plt.figure("Problema del Viajante de Comercio", figsize=(8, 6))

    # Dibujar la ruta con flechas y los índices de los lugares
    draw_vrp_route(locations, vehicle_routes_mapping)

    # Dibujar el depósito
    # draw_deposit(tsp_problem.depot.data, tsp_problem.depot.index)
    draw_deposit(depot.data, depot.index)

    # Dibujar los demás lugares como círculos con los índices en su interior
    draw_locations(filter_locations(locations, depot.index))

    # Crear la leyenda de la ciudad correspondiente a cada índice
    # draw_legend(locations)

    # Configurar el gráfico
    draw_graph("Coordinate X", "Coordinate Y", "Vehicle Routing Problem")


plot_nodes_and_route(
    vrp_problem.depot, vrp_problem.locations, vrp_problem.vehicle_routes_mapping
)
