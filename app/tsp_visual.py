import sys

sys.path.append("./")

from app.problems.tsp.data_handling_tsp import process_files_tsp, process_solutions_tsp
from app.services.main import plot_problem

# Seleccionar la instancia que se quiere visualizar
instance_name = "ulysses22"
# Cargar los datos y las soluciones de las instancias de TSP
problems = process_files_tsp()
data = problems[f"{instance_name}.tsp"]
solutions = process_solutions_tsp()
data_solution = solutions[f"solution_{instance_name}.tsp"]

plot_problem(
    "tsp",
    locations=data["locations"],
    depot_index=data["depot"],
    vehicle_routes_mapping=data_solution["route"],
)
