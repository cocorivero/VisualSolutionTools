import sys

sys.path.append("./")
from app.data_handler.load_data import (
    load_data_bss,
    load_data_cvrp,
    load_data_tsp,
    load_data_vrp_txt,
)
from app.generate_visual.main import plot_problem


def plot_tsp():
    data, routes = load_data_tsp()
    plot_problem(
        problem_type="tsp",
        depot_id=data["depot_id"],
        stops=data["locations"],
        routes=routes,
        x_label="Coordinate X",
        y_label="Coordinate Y",
        graph_title="Travelling Salesman Problem",
    )


def plot_vrp():
    data, routes = load_data_vrp_txt()
    plot_problem(
        problem_type="vrp",
        depot_id=data["depot_id"],
        stops=data["locations"],
        routes=routes,
        x_label="Coordinate X",
        y_label="Coordinate Y",
        graph_title="Vehicle Routing Problem",
    )


def plot_cvrp():
    data, routes = load_data_cvrp()
    plot_problem(
        problem_type="cvrp",
        depot_id=data["depot_id"],
        stops=data["locations"],
        routes=routes,
        x_label="Coordinate X",
        y_label="Coordinate Y",
        graph_title="Capacitated Vehicle Routing Problem",
    )


def plot_bss():
    data = load_data_bss()
    # print(data)
    plot_problem(
        problem_type="bss",
        depot_id=data["depot_id"],
        stops=data["locations"],
        passengers=data["passengers"],
        x_label="Coordinate X",
        y_label="Coordinate Y",
        graph_title="Bus Stops Selector",
    )
