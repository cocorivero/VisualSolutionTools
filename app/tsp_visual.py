import sys

sys.path.append("./")

import matplotlib.pyplot as plt

from problems.tsp.data_handling import process_files
from instances_problems import create_data_model_tsp, create_data_solution_tsp
from services.draw_funtions import *
from services.draw_routes import draw_tsp_route
from classes.tsp import TSP
from classes.depto import Depto

# Guardar en variables individuales los datos de cada instancia
for filename, data in process_files().items():
    locations = data["locations"]
    num_vehicles = data["num_vehicles"]
    depot_index = data["depot"]

depot = Depto(locations[depot_index], depot_index)

solution = create_data_solution_tsp()

# Crear instancia de la clase TSP con la instancia de Depto, datos de lugares y la ruta
tsp_problem = TSP(
    depot,
    locations,
    solution["route"],
)


import sys

sys.path.append("./")

import matplotlib.pyplot as plt

from problems.tsp.data_handling import process_files
from instances_problems import create_data_model_tsp, create_data_solution_tsp
from services.draw_funtions import *
from services.draw_routes import draw_tsp_route
from classes.tsp import TSP
from classes.depto import Depto


# Guardar en variables individuales los datos de cada instancia
for filename, data in process_files().items():
    locations = data["locations"]
    num_vehicles = data["num_vehicles"]
    depot_index = data["depot"]

depot = Depto(locations[depot_index], depot_index)

# Cadena inicial
sequence = "0 -> 7 -> 3 -> 17 -> 21 -> 16 -> 1 -> 2 -> 15 -> 13 -> 12 -> 11 -> 20 -> 19 -> 18 -> 9 -> 6 -> 5 -> 8 -> 10 -> 4 -> 14 -> 0"
# Dividir la cadena en elementos individuales y convertirlos a enteros
array = [int(num) for num in sequence.split(" -> ")]


# Crear instancia de la clase TSP con la instancia de Depto, datos de lugares y la ruta
tsp_problem = TSP(depot, locations, array)


draw_locations(filter_locations(tsp_problem.locations, tsp_problem.depot.index))
draw_deposit(tsp_problem.depot.data, tsp_problem.depot.index)
draw_tsp_route(tsp_problem.locations, tsp_problem.route)
draw_graph("Coordinate X", "Coordinate Y", "Travelling Salesperson Problem")
