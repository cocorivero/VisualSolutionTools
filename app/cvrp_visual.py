import sys

sys.path.append("./")

from app.problems.cvrp.data_handling_cvrp import load_data_cvrp_txt
from app.main import plot_problem

data, rotes = load_data_cvrp_txt()

plot_problem(
    "cvrp",
    locations=data["locations"],
    depot_index=data["depot"],
    vehicle_routes_mapping=rotes,
    demands=data["demands"],
)
