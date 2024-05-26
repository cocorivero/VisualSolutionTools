import sys

sys.path.append("./")

from app.problems.cvrp.data_handling_vrp import (
    process_files_vrp_txt,
    process_files_vrp,
    process_solutions_vrp,
)
from services.draw_funtions import *
from services.draw_routes import draw_vrp_route
from classes.vrp import VRP
from classes.depto import Depto

# Cargar los datos y las soluciones de las instancias de TSP
problems = process_files_vrp_txt()
solutions = process_solutions_vrp()

# Seleccionar la instancia que se quiere visualizar
instance_name = "p2"

# Extraer los datos de la instancia y la solución
data = problems[f"{instance_name}.txt"]
data_solution = solutions[f"solution_{instance_name}.txt"]

routes_dict = {entry["vehicle"]: entry["route"] for entry in data_solution}

# Crear instancia de la clase TSP con la instancia de Depto, datos de lugares y la ruta
vrp_problem = VRP(
    Depto(data["locations"][data["depot"]], data["depot"]),
    data["locations"],
    routes_dict,
)

draw_locations(filter_locations(vrp_problem.locations, vrp_problem.depot.index))
draw_deposit(vrp_problem.depot.data, vrp_problem.depot.index)
draw_vrp_route(vrp_problem.locations, vrp_problem.vehicle_routes_mapping)
draw_graph("Coordinate X", "Coordinate Y", "Vehicle Routing Problem")
