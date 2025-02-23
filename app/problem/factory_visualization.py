from app.problem.problem_2d import Problem2D
from app.problem.problem_map import ProblemMap


class FactoryVisualizacion:
    @staticmethod
    def crear_visualizacion(view_mode):
        if view_mode == "2D":
            return Problem2D()
        elif view_mode == "Mapa":
            return ProblemMap()
        else:
            raise ValueError("Tipo de visualización no soportado")
