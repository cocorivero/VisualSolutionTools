from abc import ABC, abstractmethod
from app.models.depot import Depot
from app.models.passenger import Passenger
from app.models.stop import Stop
from app.models.route import Route


class VRP(ABC):
    def __init__(
        self,
        problem_name,
        depot: Depot,
        stops: list[Stop],
        routes: list[Route] = None,
        passengers: list[Passenger] = None,
    ):
        self.problem_name = problem_name
        self.depot = depot
        self.stops = stops
        self.routes = routes if routes is not None else []
        self.passengers = passengers if passengers is not None else []

    @abstractmethod
    def draw_problem(self):
        pass

    def find_passenger(self, passenger_id):
        for p in self.passengers:
            if p.id == passenger_id:
                return p
        return None
