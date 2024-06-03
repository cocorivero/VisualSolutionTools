import sys

sys.path.append("./")

from app.problems.bss.data_handling_bss import load_data_bss
from app.main import plot_problem

data = load_data_bss()

plot_problem(
    "bss",
    depot_data=data["depot_coordinates"],
    bus_stop_data=data["bus_stop_data"],
)
