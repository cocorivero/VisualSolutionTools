import sys

sys.path.append("./")

from app.problems.vrp.data_handling_vrp import load_data_vrp_txt
from app.main import plot_problem

data, route = load_data_vrp_txt()


plot_problem(
    "vrp",
    locations=data["locations"],
    depot_index=data["depot"],
    vehicle_routes_mapping=route,
)
