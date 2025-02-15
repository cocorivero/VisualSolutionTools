import sys

sys.path.append("./")

from app.models.point import Point


class Depot(Point):
    def __init__(
        self,
        id,
        coordinates,
        size,
        marker_type,
        marker_color,
        marker_border,
        marker_border_color,
        font_color,
        font_size,
    ):
        super().__init__(id, coordinates)

        self.size = size
        self.marker_border = marker_border
        self.marker_type = marker_type
        self.marker_color = marker_color
        self.marker_border_color = marker_border_color
        self.font_color = font_color
        self.font_size = font_size
