import matplotlib.pyplot as plt
from app.problem.problem import Problem


class ProblemMap(Problem):
    def create_problem(self, route_data):
        plt.figure()
        for route in route_data:
            plt.plot(route[0], route[1], "bo-")
        plt.title("2D Route Visualization")
        plt.show()
