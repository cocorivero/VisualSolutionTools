import sys

sys.path.append("./")

from app.problems.tsp.data_handling_tsp import process_files_tsp, process_solutions_tsp
from services.draw_funtions import *
from services.draw_routes import draw_tsp_route
from classes.tsp import TSP
from classes.depto import Depto

# Cargar los datos y las soluciones de las instancias de TSP
problems = process_files_tsp()
solutions = process_solutions_tsp()

# Seleccionar la instancia que se quiere visualizar
instance_name = "ulysses22"

# Extraer los datos de la instancia y la solución
data = problems[f"{instance_name}.tsp"]
data_solution = solutions[f"solution_{instance_name}.tsp"]

# Crear instancia de la clase TSP con la instancia de Depto, datos de lugares y la ruta
tsp_problem = TSP(
    Depto(data["locations"][data["depot"]], data["depot"]),
    data["locations"],
    data_solution["route"],
)

draw_locations(filter_locations(tsp_problem.locations, tsp_problem.depot.index))
draw_deposit(tsp_problem.depot.data, tsp_problem.depot.index)
draw_tsp_route(tsp_problem.locations, tsp_problem.route)
draw_graph("Coordinate X", "Coordinate Y", "Travelling Salesperson Problem")
