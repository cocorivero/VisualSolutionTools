import sys

sys.path.append("./")

from app.classes.point import Point
from typing import List, Optional, Tuple


class Stop(Point):
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
        demand_size: int,
        demand_color: str,
        marker_passenger_type: str,
        marker_passenger_size: int,
        marker_passenger_color: str,
        marker_passenger_border: int,
        marker_passenger_border_color: str,
        passenger_route_style: str,
        passenger_route_color: str,
        assigned_passengers: Optional[List[str]] = None,
        capacity: Optional[int] = None,
    ):
        super().__init__(id, coordinates)

        self.size: int = size
        self.marker_border: int = marker_border
        self.marker_type: str = marker_type
        self.marker_color: str = marker_color
        self.marker_border_color: str = marker_border_color
        self.font_color: str = font_color
        self.font_size: int = font_size
        self.demand_size: int = demand_size
        self.demand_color: str = demand_color
        self.marker_passenger_type: str = marker_passenger_type
        self.marker_passenger_size: int = marker_passenger_size
        self.marker_passenger_color: str = marker_passenger_color
        self.marker_passenger_border: int = marker_passenger_border
        self.marker_passenger_border_color: str = marker_passenger_border_color
        self.passenger_route_style: str = passenger_route_style
        self.passenger_route_color: str = passenger_route_color
        self.assigned_passengers: List[str] = (
            assigned_passengers if assigned_passengers is not None else []
        )
        self.capacity: Optional[int] = capacity
