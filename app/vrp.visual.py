import sys

sys.path.append("./")

from app.problems.vrp.data_handling_vrp import (
    process_files_vrp_txt,
    process_solutions_vrp,
)
from main import plot_problem

# Seleccionar la instancia que se quiere visualizar
instance_name = "p2"
# Cargar los datos y las soluciones de las instancias de TSP
problems = process_files_vrp_txt()
data = problems[f"{instance_name}.txt"]
solutions = process_solutions_vrp()
data_solution = solutions[f"solution_{instance_name}.txt"]
routes_dict = {entry["vehicle"]: entry["route"] for entry in data_solution}

plot_problem("vrp", data["locations"], data["depot"], routes_dict)
