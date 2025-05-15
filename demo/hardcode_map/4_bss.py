# ╔════════════════════════════════════════════════════════════════════════╗
# ║                        BSS Visualization Example                       ║
# ╠════════════════════════════════════════════════════════════════════════╣
# ║  Problem Type  : Bus Stop Selection (BSS)                              ║
# ║  Input Method  : Manual dictionary input                               ║
# ║  View Mode     : Map                                                   ║
# ║  Total Nodes   : 5 nodes (including depot)                             ║
# ║  Passengers    : 12                                                    ║
# ╚════════════════════════════════════════════════════════════════════════╝

import sys

sys.path.append("./")

from app.problem.problem_plotter import ProblemPlotterFacade

plotter = ProblemPlotterFacade()

plotter.plot_problem(
    problem_title="BSS - Manual Input",
    problem_type="bss",
    view_mode="map",
    data={
        "depot_id": "0",
        "locations": {
            "0": {"coords": (23.1260739, -82.37243129)},
            "1": {
                "coords": (23.11939678, -82.3775335),
                "passengers": ["passenger_id_1", "passenger_id_2"],
                "capacity": 15,
            },
            "2": {
                "coords": (23.11978007, -82.39100774),
                "passengers": ["passenger_id_3", "passenger_id_4", "passenger_id_5"],
                "capacity": 15,
            },
            "3": {
                "coords": (23.12770035, -82.40008214),
                "passengers": ["passenger_id_6", "passenger_id_7", "passenger_id_8"],
                "capacity": 15,
            },
            "4": {
                "coords": (23.12880217, -82.3765467),
                "passengers": [
                    "passenger_id_9",
                    "passenger_id_10",
                    "passenger_id_11",
                    "passenger_id_12",
                ],
                "capacity": 15,
            },
        },
        "passengers": [
            ("passenger_id_1", (23.11760801, -82.37519852)),
            ("passenger_id_2", (23.11970712, -82.37658682)),
            ("passenger_id_3", (23.12168542, -82.39016326)),
            ("passenger_id_4", (23.12170782, -82.38838923)),
            ("passenger_id_5", (23.11728161, -82.38919873)),
            ("passenger_id_6", (23.1264214, -82.40242291)),
            ("passenger_id_7", (23.12889187, -82.39840001)),
            ("passenger_id_8", (23.13062993, -82.39814348)),
            ("passenger_id_9", (23.12763203, -82.37803142)),
            ("passenger_id_10", (23.13013203, -82.37743142)),
            ("passenger_id_11", (23.1313203, -82.38063142)),
            ("passenger_id_12", (23.12778152, -82.372700142)),
        ],
    },
)
