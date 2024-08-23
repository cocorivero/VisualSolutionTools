import sys

sys.path.append("./")
from app.data_handler.load_data import (
    load_data_bss,
    load_data_cvrp,
    load_data_tsp,
    load_data_vrp_txt,
)
from app.utils.generate_visual import plot_problem


def plot_tsp(instance: str):
    data, routes = load_data_tsp(instance)
    plot_problem(
        problem_type="tsp",
        depot_id=data["depot_id"],
        stops=data["locations"],
        routes=routes,
        x_label="Coordinate X",
        y_label="Coordinate Y",
        graph_title=instance,
    )


def plot_vrp(instance: str):
    data, routes = load_data_vrp_txt(instance)
    plot_problem(
        problem_type="vrp",
        depot_id=data["depot_id"],
        stops=data["locations"],
        routes=routes,
        x_label="Coordinate X",
        y_label="Coordinate Y",
        graph_title="Vehicle Routing Problem",
    )


def plot_cvrp(instance: str):
    data, routes = load_data_cvrp(instance)
    plot_problem(
        problem_type="cvrp",
        depot_id=data["depot_id"],
        stops=data["locations"],
        routes=routes,
        x_label="Coordinate X",
        y_label="Coordinate Y",
        graph_title="Capacitated Vehicle Routing Problem",
    )


def plot_bss(instance: str):
    data = load_data_bss(instance)
    plot_problem(
        problem_type="bss",
        depot_id=data["depot_id"],
        stops=data["locations"],
        passengers=data["passengers"],
        x_label="Coordinate X",
        y_label="Coordinate Y",
        graph_title="Bus Stops Selector",
    )


instance1 = "p31"
plot_cvrp(instance1)
