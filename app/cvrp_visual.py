import sys

sys.path.append("./")

from app.problems.cvrp.data_handling_cvrp import (
    process_files_cvrp_txt,
    process_solutions_cvrp,
)
from app.services.main import plot_problem

# Seleccionar la instancia que se quiere visualizar
instance_name = "p31"
# Cargar los datos y las soluciones de las instancias de TSP
problems = process_files_cvrp_txt()
data = problems[f"{instance_name}.txt"]
solutions = process_solutions_cvrp()
data_solution = solutions[f"solution_{instance_name}.txt"]
routes_dict = {entry["vehicle"]: entry["route"] for entry in data_solution}

plot_problem("cvrp", data["locations"], data["depot"], routes_dict, data["demands"])
