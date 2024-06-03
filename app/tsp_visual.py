import sys

sys.path.append("./")

from app.problems.tsp.data_handling_tsp import load_data_tsp
from app.main import plot_problem

data, route = load_data_tsp()

plot_problem(
    "vrp",
    locations=data["locations"],
    depot_index=data["depot"],
    vehicle_routes_mapping=route,
)
