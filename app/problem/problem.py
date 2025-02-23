from abc import ABC, abstractmethod


class Problem(ABC):
    @abstractmethod
    def create_problem(
        self,
        problem_type,
        problem_name,
        data,
        routes=[],
        depot_config=None,
        stop_config=None,
        routes_config=None,
        graph_title=None,
    ):
        pass
