# ╔════════════════════════════════════════════════════════════════════════╗
# ║                        SBRP Visualization Example                      ║
# ╠════════════════════════════════════════════════════════════════════════╣
# ║  Problem Type  : School BusRouting Problem (SBRP)                      ║
# ║  Input Method  : Manual dictionary input                               ║
# ║  View Mode     : 2D                                                    ║
# ║  Total Nodes   : 4 nodes (including depot)                             ║
# ║  Passengers    : 25                                                    ║
# ║  Route         : 1                                                     ║
# ╚════════════════════════════════════════════════════════════════════════╝

import sys

sys.path.append("./")

from app.problem.problem_plotter import ProblemPlotterFacade

plotter = ProblemPlotterFacade()

plotter.plot_problem(
    problem_title="SBRP - Manual Input",
    problem_type="sbrp",
    view_mode="2d",
    data={
        "depot_id": "0",
        "locations": {
            "0": {"coords": (50.0, 50.0)},
            "1": {
                "coords": (41.22666666666667, 51.766999999999996),
                "passengers": [
                    "passenger_id_2",
                    "passenger_id_13",
                    "passenger_id_25",
                    "passenger_id_3",
                    "passenger_id_17",
                    "passenger_id_15",
                    "passenger_id_18",
                ],
                "capacity": 15,
            },
            "2": {
                "coords": (69.1885, 47.2435),
                "passengers": [
                    "passenger_id_5",
                    "passenger_id_7",
                    "passenger_id_21",
                    "passenger_id_8",
                ],
                "capacity": 15,
            },
            "3": {
                "coords": (47.88094444444445, 71.19444444444446),
                "passengers": [
                    "passenger_id_19",
                    "passenger_id_9",
                    "passenger_id_11",
                    "passenger_id_22",
                    "passenger_id_4",
                    "passenger_id_6",
                    "passenger_id_10",
                    "passenger_id_1",
                    "passenger_id_23",
                    "passenger_id_14",
                    "passenger_id_12",
                    "passenger_id_24",
                    "passenger_id_16",
                    "passenger_id_20",
                ],
                "capacity": 15,
            },
        },
        "passengers": [
            ("passenger_id_1", (45.658, 84.734)),
            ("passenger_id_2", (22.96, 58.777)),
            ("passenger_id_3", (45.205, 42.495)),
            ("passenger_id_4", (26.013, 72.453)),
            ("passenger_id_5", (75.771, 57.152)),
            ("passenger_id_6", (63.216, 76.771)),
            ("passenger_id_7", (61.891, 42.563)),
            ("passenger_id_8", (72.369, 49.029)),
            ("passenger_id_9", (68.527, 80.802)),
            ("passenger_id_10", (63.545, 73.386)),
            ("passenger_id_11", (36.396, 86.937)),
            ("passenger_id_12", (52.678, 63.497)),
            ("passenger_id_13", (35.801, 63.173)),
            ("passenger_id_14", (40.512, 78.207)),
            ("passenger_id_15", (41.441, 59.143)),
            ("passenger_id_16", (55.007, 70.914)),
            ("passenger_id_17", (37.02, 56.429)),
            ("passenger_id_18", (43.54, 55.439)),
            ("passenger_id_19", (71.214, 76.69)),
            ("passenger_id_20", (46.363, 67.611)),
            ("passenger_id_21", (66.723, 40.23)),
            ("passenger_id_22", (40.59, 88.571)),
            ("passenger_id_23", (50.643, 59.045)),
            ("passenger_id_24", (43.693, 67.698)),
            ("passenger_id_25", (55.515, 54.029)),
        ],
    },
    routes=[["0", "1", "3", "2", "0"]],
)
