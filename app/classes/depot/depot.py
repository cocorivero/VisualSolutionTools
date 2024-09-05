import sys

sys.path.append("./")

from app.classes.point import Point
import matplotlib.pyplot as plt
from typing import Tuple


class Depot(Point):
    def __init__(
        self,
        id: str,
        coordinates: Tuple[float, float],
        size: int,
        marker_type: str,
        marker_color: str,
        marker_border: int,
        marker_border_color: str,
        font_color: str,
        font_size: int,
    ):
        super().__init__(id, coordinates)

        self.size: int = size
        self.marker_border: int = marker_border
        self.marker_type: str = marker_type
        self.marker_color: str = marker_color
        self.marker_border_color: str = marker_border_color
        self.font_color: str = font_color
        self.font_size: int = font_size
