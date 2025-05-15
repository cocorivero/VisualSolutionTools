# ╔════════════════════════════════════════════════════════════════════════╗
# ║                        CVRP Visualization Example                      ║
# ╠════════════════════════════════════════════════════════════════════════╣
# ║  Problem Type  : Capacitated Vehicle Routing Problem (CVRP)            ║
# ║  Input Method  : Manual dictionary input                               ║
# ║  View Mode     : 2D                                                    ║
# ║  Total Nodes   : 9 nodes (including depot)                             ║
# ║  Route         : 2                                                     ║
# ╚════════════════════════════════════════════════════════════════════════╝

import sys

sys.path.append("./")

from app.problem.problem_plotter import ProblemPlotterFacade

plotter = ProblemPlotterFacade()

plotter.plot_problem(
    problem_title="CVRP - Manual Input",
    problem_type="cvrp",
    view_mode="2d",
    data={
        "depot_id": "0",
        "locations": {
            "0": {"coords": (-3.799, 44.290)},
            "1": {"coords": (-40.289, -42.303), "capacity": 20},
            "2": {"coords": (-64.709, -17.389), "capacity": 10},
            "3": {"coords": (5.060, -14.349), "capacity": 8},
            "4": {"coords": (72.095, 20.233), "capacity": 6},
            "5": {"coords": (2.594, -15.002), "capacity": 1},
            "6": {"coords": (-24.176, -72.894), "capacity": 19},
            "7": {"coords": (-13.190, 66.498), "capacity": 13},
            "8": {"coords": (33.191, 13.690), "capacity": 24},
            "9": {"coords": (66.827, -30.554), "capacity": 15},
            "10": {"coords": (19.934, 35.883), "capacity": 13},
        },
    },
    routes=[
        ["0", "10", "4", "9", "8", "0"],
        ["0", "7", "2", "1", "6", "5", "3", "0"],
    ],
)
