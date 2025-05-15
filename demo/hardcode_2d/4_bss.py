# ╔════════════════════════════════════════════════════════════════════════╗
# ║                        BSS Visualization Example                       ║
# ╠════════════════════════════════════════════════════════════════════════╣
# ║  Problem Type  : Bus Stop Selection (BSS)                              ║
# ║  Input Method  : Manual dictionary input                               ║
# ║  View Mode     : 2D                                                    ║
# ║  Total Nodes   : 10 nodes (including depot)                            ║
# ║  Passengers    : 25                                                    ║
# ╚════════════════════════════════════════════════════════════════════════╝

import sys

sys.path.append("./")

from app.problem.problem_plotter import ProblemPlotterFacade

plotter = ProblemPlotterFacade()

plotter.plot_problem(
    problem_title=" BSS - Manual Input",
    problem_type="bss",
    view_mode="2d",
    data={
        "depot_id": "0",
        "locations": {
            "0": {"coords": (50.0, 50.0)},
            "1": {
                "coords": (81.10006740957493, 41.86108100956588),
                "passengers": ["passenger_id_2", "passenger_id_8"],
                "capacity": 15,
            },
            "2": {
                "coords": (41.86108100956588, 54.75884154772805),
                "passengers": [
                    "passenger_id_17",
                    "passenger_id_7",
                    "passenger_id_15",
                    "passenger_id_20",
                ],
                "capacity": 15,
            },
            "3": {
                "coords": (39.64421282503511, 28.674732292658177),
                "passengers": ["passenger_id_14", "passenger_id_22", "passenger_id_3"],
                "capacity": 15,
            },
            "4": {
                "coords": (26.912444767284796, 54.75884154772805),
                "passengers": ["passenger_id_13", "passenger_id_23"],
                "capacity": 15,
            },
            "5": {
                "coords": (39.64421282503511, 54.75884154772805),
                "passengers": ["passenger_id_12"],
                "capacity": 15,
            },
            "6": {
                "coords": (81.10006740957493, 54.75884154772805),
                "passengers": ["passenger_id_19", "passenger_id_9", "passenger_id_4"],
                "capacity": 15,
            },
            "7": {
                "coords": (54.75884154772805, 28.674732292658177),
                "passengers": [
                    "passenger_id_16",
                    "passenger_id_5",
                    "passenger_id_10",
                    "passenger_id_24",
                ],
                "capacity": 15,
            },
            "8": {
                "coords": (26.912444767284796, 39.64421282503511),
                "passengers": ["passenger_id_11"],
                "capacity": 15,
            },
            "9": {
                "coords": (54.75884154772805, 81.10006740957493),
                "passengers": ["passenger_id_25", "passenger_id_6"],
                "capacity": 15,
            },
            "10": {
                "coords": (54.75884154772805, 54.75884154772805),
                "passengers": ["passenger_id_21", "passenger_id_1", "passenger_id_18"],
                "capacity": 15,
            },
        },
        "passengers": [
            ("passenger_id_1", (48.359, 55.86)),
            ("passenger_id_2", (66.386, 41.507)),
            ("passenger_id_3", (35.834, 29.28)),
            ("passenger_id_4", (82.836, 57.993)),
            ("passenger_id_5", (65.612, 27.586)),
            ("passenger_id_6", (57.604, 78.332)),
            ("passenger_id_7", (45.98, 51.086)),
            ("passenger_id_8", (72.342, 45.38)),
            ("passenger_id_9", (73.329, 54.915)),
            ("passenger_id_10", (60.328, 31.039)),
            ("passenger_id_11", (9.071, 35.512)),
            ("passenger_id_12", (39.486, 65.756)),
            ("passenger_id_13", (15.359, 53.768)),
            ("passenger_id_14", (33.094, 16.004)),
            ("passenger_id_15", (41.433, 49.796)),
            ("passenger_id_16", (65.941, 23.786)),
            ("passenger_id_17", (46.987, 59.167)),
            ("passenger_id_18", (58.584, 55.702)),
            ("passenger_id_19", (78.877, 67.55)),
            ("passenger_id_20", (44.443, 61.516)),
            ("passenger_id_21", (64.465, 56.926)),
            ("passenger_id_22", (43.613, 27.844)),
            ("passenger_id_23", (19.763, 49.856)),
            ("passenger_id_24", (53.807, 30.853)),
            ("passenger_id_25", (68.199, 78.151)),
        ],
    },
)
