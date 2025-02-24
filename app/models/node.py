from abc import ABC


class Node(ABC):
    def __init__(
        self,
        id,
        # name=None,
        coords,
        size=None,
        marker_type=None,
        marker_color=None,
        marker_border=None,
        marker_border_color=None,
    ):
        self.id = id
        self.coords = coords
        self.size = size
        self.marker_type = marker_type
        self.marker_color = marker_color
        self.marker_border = marker_border
        self.marker_border_color = marker_border_color
