# ╔════════════════════════════════════════════════════════════════════════╗
# ║                        CVRP Visualization Example                      ║
# ╠════════════════════════════════════════════════════════════════════════╣
# ║  Problem Type  : Capacitated Vehicle Routing Problem (CVRP)            ║
# ║  Input Method  : Manual dictionary input                               ║
# ║  View Mode     : Map                                                   ║
# ║  Total Nodes   : 8 nodes (including depot)                             ║
# ║  Route         : 2                                                     ║
# ╚════════════════════════════════════════════════════════════════════════╝

import sys

sys.path.append("./")

from app.problem.problem_plotter import ProblemPlotterFacade

plotter = ProblemPlotterFacade()

plotter.plot_problem(
    problem_title="CVRP - Manual Input",
    problem_type="cvrp",
    view_mode="map",
    data={
        "depot_id": "0",
        "locations": {
            "0": {"coords": (23.12281593, -82.31865032)},
            "1": {"coords": (23.10550779, -82.39007169), "capacity": 20},
            "2": {"coords": (23.08777992, -82.37669715), "capacity": 10},
            "3": {"coords": (23.12811315, -82.37004818), "capacity": 8},
            "4": {"coords": (23.08319999, -82.32625959), "capacity": 6},
            "5": {"coords": (23.12320551, -82.38125607), "capacity": 1},
            "6": {"coords": (23.07040675, -82.42995379), "capacity": 19},
            "7": {"coords": (23.10361576, -82.36380077), "capacity": 13},
        },
    },
    routes=[
        ["0", "3", "1", "4", "2", "0"],
        ["0", "6", "5", "7", "0"],
    ],
)
