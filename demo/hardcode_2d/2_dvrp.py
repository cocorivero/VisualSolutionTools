# ╔════════════════════════════════════════════════════════════════════════╗
# ║                        DVRP Visualization Example                      ║
# ╠════════════════════════════════════════════════════════════════════════╣
# ║  Problem Type  : Distance Vehicle Routing Problem (DVRP)               ║
# ║  Input Method  : Manual dictionary input                               ║
# ║  View Mode     : 2D                                                    ║
# ║  Total Nodes   : 17 nodes (including depot)                            ║
# ║  Route         : 2                                                     ║
# ╚════════════════════════════════════════════════════════════════════════╝

import sys

sys.path.append("./")

from app.problem.problem_plotter import ProblemPlotterFacade

plotter = ProblemPlotterFacade()

plotter.plot_problem(
    problem_title="VRP - Manual Input",
    problem_type="vrp",
    view_mode="2d",
    data={
        "depot_id": "0",
        "locations": {
            "0": {"coords": (23.07658329, -82.31711341)},
            "1": {"coords": (23.08809165, -82.38046935)},
            "2": {"coords": (23.12624164, -82.39115311)},
            "3": {"coords": (23.10078975, -82.36673786)},
            "4": {"coords": (23.12920515, -82.37688084)},
            "5": {"coords": (23.09920493, -82.37715249)},
            "6": {"coords": (23.0960326, -82.36918036)},
            "7": {"coords": (23.12968988, -82.38966018)},
            "8": {"coords": (23.1010951, -82.38805238)},
            "9": {"coords": (23.09993958, -82.33650503)},
            "10": {"coords": (23.07363773, -82.3613428)},
            "11": {"coords": (23.12828544, -82.32453085)},
            "12": {"coords": (23.12564268, -82.32464419)},
            "13": {"coords": (23.1267473, -82.36498816)},
            "14": {"coords": (23.09663832, -82.32552482)},
            "15": {"coords": (23.10733252, -82.36946415)},
            "16": {"coords": (23.1097303, -82.38149651)},
        },
    },
    routes=[
        ["0", "10", "6", "3", "16", "15", "8", "2", "7", "4", "13", "1", "0"],
        ["0", "14", "9", "12", "11", "0"],
    ],
)
