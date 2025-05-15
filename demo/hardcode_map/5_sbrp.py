# ╔════════════════════════════════════════════════════════════════════════╗
# ║                        SBRP Visualization Example                      ║
# ╠════════════════════════════════════════════════════════════════════════╣
# ║  Problem Type  : School BusRouting Problem (SBRP)                      ║
# ║  Input Method  : Manual dictionary input                               ║
# ║  View Mode     : Map                                                   ║
# ║  Total Nodes   : 5 nodes (including depot)                             ║
# ║  Passengers    : 21                                                    ║
# ║  Route         : 2                                                     ║
# ╚════════════════════════════════════════════════════════════════════════╝

import sys

sys.path.append("./")

from app.problem.problem_plotter import ProblemPlotterFacade

plotter = ProblemPlotterFacade()

plotter.plot_problem(
    problem_title="SBRP - Manual Input",
    problem_type="sbrp",
    view_mode="map",
    data={
        "depot_id": "0",
        "locations": {
            "0": {"coords": (23.09920493, -82.37715249)},
            "1": {
                "coords": (23.1010951, -82.38805238),
                "passengers": [
                    "passenger_id_1",
                    "passenger_id_2",
                    "passenger_id_3",
                    "passenger_id_12",
                    "passenger_id_13",
                ],
                "capacity": 15,
            },
            "2": {
                "coords": (23.1097303, -82.38149651),
                "passengers": [
                    "passenger_id_4",
                    "passenger_id_5",
                    "passenger_id_14",
                    "passenger_id_15",
                    "passenger_id_16",
                ],
                "capacity": 15,
            },
            "3": {
                "coords": (23.10733252, -82.36946415),
                "passengers": [
                    "passenger_id_6",
                    "passenger_id_7",
                    "passenger_id_17",
                    "passenger_id_19",
                ],
                "capacity": 15,
            },
            "4": {
                "coords": (23.10078975, -82.36673786),
                "passengers": [
                    "passenger_id_10",
                    "passenger_id_11",
                    "passenger_id_20",
                    "passenger_id_21",
                ],
                "capacity": 15,
            },
        },
        "passengers": [
            ("passenger_id_1", (23.097571175601896, -82.3850370166508)),
            ("passenger_id_2", (23.100411761303654, -82.39106770576396)),
            ("passenger_id_3", (23.100347272294816, -82.3857292819285)),
            ("passenger_id_4", (23.11176925348477, -82.38535470723254)),
            ("passenger_id_5", (23.10761444966701, -82.38525252919841)),
            ("passenger_id_6", (23.108360539073365, -82.37160257503693)),
            ("passenger_id_7", (23.108013018354504, -82.36557045264058)),
            ("passenger_id_10", (23.096990521830715, -82.36464083228278)),
            ("passenger_id_11", (23.099661698207348, -82.36477992852001)),
            ("passenger_id_12", (23.09895311382798, -82.39131458591454)),
            ("passenger_id_13", (23.097284259973986, -82.39177165080051)),
            ("passenger_id_14", (23.106392344443407, -82.37906803638526)),
            ("passenger_id_15", (23.11221629448479, -82.38444245588589)),
            ("passenger_id_16", (23.111918951592983, -82.37817854450097)),
            ("passenger_id_17", (23.104398470663927, -82.37292230169892)),
            ("passenger_id_19", (23.105549339855718, -82.36639157849218)),
            ("passenger_id_20", (23.098232659710668, -82.36423824710424)),
            ("passenger_id_21", (23.09717370551054, -82.37044979378494)),
        ],
    },
    routes=[["0", "1", "2", "0"], ["0", "3", "4", "0"]],
)
