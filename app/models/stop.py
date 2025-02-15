import sys

sys.path.append("./")

from app.models.point import Point


class Stop(Point):
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
        demand_size,
        demand_color,
        marker_passenger_type,
        marker_passenger_size,
        marker_passenger_color,
        marker_passenger_border,
        marker_passenger_border_color,
        passenger_route_style,
        passenger_route_color,
        assigned_passengers=None,
        capacity=None,
    ):
        super().__init__(id, coordinates)

        self.size = size
        self.marker_border = marker_border
        self.marker_type = marker_type
        self.marker_color = marker_color
        self.marker_border_color = marker_border_color
        self.font_color = font_color
        self.font_size = font_size
        self.demand_size = demand_size
        self.demand_color = demand_color
        self.marker_passenger_type = marker_passenger_type
        self.marker_passenger_size = marker_passenger_size
        self.marker_passenger_color = marker_passenger_color
        self.marker_passenger_border = marker_passenger_border
        self.marker_passenger_border_color = marker_passenger_border_color
        self.passenger_route_style = passenger_route_style
        self.passenger_route_color = passenger_route_color
        self.assigned_passengers = (
            assigned_passengers if assigned_passengers is not None else []
        )
        self.capacity = capacity
