import sys

sys.path.append("./")

from app.problems.bss.data_handling_bss import process_files_solutions
from app.services.main import plot_problem


solution_data = process_files_solutions()
data = solution_data["BSS_solution-69_B-3_P-25_D-1_MW-40.0_MBC-15_MVC-25_BSS.json"]

plot_problem(
    "bss",
    depot_data=data["depot_coordinates"],
    bus_stop_data=data["bus_stop_data"],
)
