import sys
from typing import List, Dict
from app.models.vrp import VRP
from app.factories.depot_factory import ConcreteDepotFactory
from app.factories.stop_factory import ConcreteStopFactory
from app.factories.route_factory import ConcreteRouteFactory

sys.path.append("./")


class ProblemPlotterFacade:
    def __init__(self):
        # Inicializamos las fábricas necesarias
        self.depot_factory = ConcreteDepotFactory()
        self.stop_factory = ConcreteStopFactory()
        self.route_factory = ConcreteRouteFactory()
        self.default_graph_titles = {
            "tsp": "Traveling Salesman Problem (TSP)",
            "vrp": "Vehicle Routing Problem (VRP)",
            "cvrp": "Capacitated Vehicle Routing Problem (CVRP)",
            "bss": "Bus Stops Selection (BSS)",
            "sbrp": "School Bus Routing Problem (SBRP)",
        }

    def _create_problem(
        self,
        problem_type: str,
        problem_name: str,
        depot_id: str,
        stops: Dict,
        routes: List,
        passengers: List,
        depot_config: Dict,
        stop_config: Dict,
        routes_config: Dict,
    ) -> VRP:
        # Definimos argumentos adicionales para la creación de paradas
        stop_args = {
            "with_capacity": problem_type in ["cvrp", "bss", "sbrp"],
            "with_assigned_passengers": problem_type in ["bss", "sbrp"],
        }

        # Creamos los objetos necesarios usando las fábricas
        depot = self.depot_factory.create_depot(
            depot_id=depot_id, stops=stops, config=depot_config
        )
        stops = self.stop_factory.create_stops(
            stop_data=stops, stop_config=stop_config, **stop_args
        )
        routes = self.route_factory.create_routes(
            routes=routes, routes_config=routes_config
        )

        # Creamos los argumentos para la instancia de VRP
        vrp_args = {
            "problem_name": problem_name,
            "depot": depot,
            "stops": stops,
            "routes": routes,
        }

        # Agregamos pasajeros si el problema lo requiere
        if problem_type in ["bss", "sbrp"]:
            vrp_args["passengers"] = passengers

        # Verificamos si el tipo de problema es soportado y creamos la instancia de VRP
        if problem_type in ["vrp", "tsp", "cvrp", "bss", "sbrp"]:
            return VRP(**vrp_args)
        else:
            print("Tipo de problema no soportado")
            return None

    def plot_problem(
        self,
        problem_type: str,
        data,
        routes: List = [],
        depot_config: Dict = None,
        stop_config: Dict = None,
        routes_config: Dict = None,
        graph_title: str = None,
    ):
        # Asignamos un título por defecto si no se proporciona uno
        graph_title = graph_title or self.default_graph_titles.get(
            problem_type, "Tipo de problema no soportado"
        )

        if graph_title == "Tipo de problema no soportado":
            print(graph_title)
            return

        # Creamos el problema usando la configuración y los datos proporcionados
        vrp = self._create_problem(
            problem_type=problem_type,
            problem_name=graph_title,
            depot_id=data.get("depot_id", ""),
            stops=data.get("locations", {}),
            routes=routes,
            passengers=data.get("passengers", []),
            depot_config=depot_config or {},
            stop_config=stop_config or {},
            routes_config=routes_config or {},
        )

        # Graficamos el problema si fue creado correctamente
        if vrp:
            vrp.draw_problem_2d()
