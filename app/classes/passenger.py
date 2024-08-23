import sys

sys.path.append("./")
from app.classes.point import Point
from typing import Tuple


class Passenger(Point):
    def __init__(
        self,
        id: str,
        coordinates: Tuple[float, float],
    ):
        super().__init__(id, coordinates)
