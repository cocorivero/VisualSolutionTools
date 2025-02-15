import sys

sys.path.append("./")
from app.models.point import Point


class Passenger(Point):
    def __init__(self, id, coordinates):
        super().__init__(id, coordinates)
