import sys

sys.path.append("./")

from app.problems.cvrp.data_handling_cvrp import (
    process_files_cvrp_txt,
    process_solutions_cvrp,
)
from services.draw_funtions import *
from services.draw_routes import draw_cvrp_route
from classes.cvrp import CVRP
from classes.depto import Depto

# Cargar los datos y las soluciones de las instancias de TSP
problems = process_files_cvrp_txt()
solutions = process_solutions_cvrp()

# Seleccionar la instancia que se quiere visualizar
instance_name = "p31"

# Extraer los datos de la instancia y la solución
data = problems[f"{instance_name}.txt"]
data_solution = solutions[f"solution_{instance_name}.txt"]

routes_dict = {entry["vehicle"]: entry["route"] for entry in data_solution}

# Crear instancia de la clase TSP con la instancia de Depto, datos de lugares y la ruta
cvrp_problem = CVRP(
    Depto(data["locations"][data["depot"]], data["depot"]),
    data["locations"],
    data["demands"],
    routes_dict,
)

draw_locations(
    filter_locations(cvrp_problem.locations, cvrp_problem.depot.index),
    cvrp_problem.demands,
)
draw_deposit(cvrp_problem.depot.data, cvrp_problem.depot.index)
draw_cvrp_route(cvrp_problem.locations, cvrp_problem.vehicle_routes_mapping)
draw_graph("Coordinate X", "Coordinate Y", "Capacitated Vehicle Routing Problem")
