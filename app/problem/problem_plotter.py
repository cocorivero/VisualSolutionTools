import sys
from app.problem.factory_visualization import FactoryVisualizacion
from app.problem.problem_2d import Problem2D
from app.problem.problem_map import ProblemMap

sys.path.append("./")


class ProblemPlotterFacade:

    def plot_problem(
        self,
        problem_type,
        view_mode,
        data,
        routes=[],
        depot_config=None,
        stop_config=None,
        routes_config=None,
        passenger_config=None,
        problem_title=None,
    ):
        default_problem_titles = {
            "tsp": "Traveling Salesman Problem (TSP)",
            "vrp": "Vehicle Routing Problem (VRP)",
            "cvrp": "Capacitated Vehicle Routing Problem (CVRP)",
            "bss": "Bus Stops Selection (BSS)",
            "sbrp": "School Bus Routing Problem (SBRP)",
        }

        problem_title = problem_title or default_problem_titles.get(
            problem_type, "Tipo de problema no soportado"
        )

        if problem_title == "Tipo de problema no soportado":
            print(problem_title)
            return

        visualization = FactoryVisualizacion.crear_visualizacion(view_mode)

        common_params = {
            "problem_type": problem_type,
            "problem_name": problem_title,
            "depot_id": data.get("depot_id", ""),
            "stops": data.get("locations", {}),
            "routes": routes,
            "passengers": data.get("passengers", []),
            "depot_config": depot_config or {},
            "stop_config": stop_config or {},
            "routes_config": routes_config or {},
            "passenger_config": passenger_config or {},
        }
        if isinstance(visualization, Problem2D):
            vrp = visualization.create_problem(**common_params)
            if vrp:
                vrp.draw_problem_2d()

        elif isinstance(visualization, ProblemMap):
            vrp = visualization.create_problem(**common_params)
            if vrp:
                vrp.draw_problem_map()
