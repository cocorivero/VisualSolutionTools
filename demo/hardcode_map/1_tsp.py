# ╔════════════════════════════════════════════════════════════════════════╗
# ║                        TSP Visualization Example                       ║
# ╠════════════════════════════════════════════════════════════════════════╣
# ║  Problem Type  : Travelling Salesman Problem (TSP)                     ║
# ║  Input Method  : Manual dictionary input                               ║
# ║  View Mode     : Map                                                   ║
# ║  Total Nodes   : 16 nodes (including depot)                            ║
# ║  Route         : 1                                                     ║
# ╚════════════════════════════════════════════════════════════════════════╝

import sys

sys.path.append("./")

from app.problem.problem_plotter import ProblemPlotterFacade

plotter = ProblemPlotterFacade()

plotter.plot_problem(
    problem_title="TSP - Manual Input",
    problem_type="tsp",
    view_mode="map",
    data={
        "depot_id": "0",
        "locations": {
            "0": {"coords": (23.13366377, -82.37866321)},
            "1": {"coords": (23.11779549, -82.37530662)},
            "2": {"coords": (23.12616853, -82.40682857)},
            "3": {"coords": (23.13424049, -82.36762437)},
            "4": {"coords": (23.08805186, -82.37964925)},
            "5": {"coords": (23.04797093, -82.36181186)},
            "6": {"coords": (23.09642123, -82.35004654)},
            "7": {"coords": (23.12146334, -82.37953162)},
            "8": {"coords": (23.09808869, -82.35806208)},
            "9": {"coords": (23.10730613, -82.36562921)},
            "10": {"coords": (23.07200338, -82.39101364)},
            "11": {"coords": (23.06233965, -82.39352418)},
            "12": {"coords": (23.06124195, -82.44990091)},
            "13": {"coords": (23.04719695, -82.46413116)},
            "14": {"coords": (23.09403291, -82.45969428)},
            "15": {"coords": (23.10922716, -82.35838221)},
        },
    },
    routes=[
        [
            "0",
            "3",
            "7",
            "1",
            "9",
            "15",
            "8",
            "6",
            "4",
            "10",
            "11",
            "5",
            "12",
            "13",
            "14",
            "2",
            "0",
        ]
    ],
)
