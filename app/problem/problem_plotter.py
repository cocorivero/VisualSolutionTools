import sys
from app.problem.problem import Problem

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

        # Validar que el tipo de problema sea soportado
        if problem_type not in default_problem_titles:
            print("Tipo de problema no soportado")
            return

        # Validar que view_mode sea "2d" o "map"
        if view_mode.lower() not in ("2d", "map"):
            print("Modo de vista no soportado")
            return

        # Si no se pasa un título, se asigna el predeterminado
        problem_title = problem_title or default_problem_titles[problem_type]

        vrp = Problem().create_problem(
            view_mode=view_mode.lower(),
            problem_type=problem_type,
            problem_name=problem_title,
            depot_id=data.get("depot_id", ""),
            stops=data.get("locations", {}),
            routes=routes,
            passengers=data.get("passengers", []),
            depot_config=depot_config or {},
            stop_config=stop_config or {},
            routes_config=routes_config or {},
            passenger_config=passenger_config or {},
        )

        if vrp:
            vrp.draw_problem()
