import sys

sys.path.append("./")

from app.generate_visual.utils import create_stops_from_dict
from app.classes.vrp import VRP


def plot_problem(
    depot_id: str,
    stops: dict,
    routes: list,
    x_label: str,
    y_label: str,
    graph_title: str,
):
    vrp = VRP(depot_id=depot_id, stops=create_stops_from_dict(stops), routes=routes)
    vrp.draw_routes()
    vrp.draw_deposit()
    vrp.draw_stops()
    vrp.draw_graph(x_label, y_label, graph_title)
