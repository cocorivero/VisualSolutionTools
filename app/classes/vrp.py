import random
import sys

sys.path.append("./")
from typing import List, Optional
from matplotlib import pyplot as plt

from app.classes.stop import Stop
from app.classes.passenger import Passenger
from app.classes.depot import Depot
from app.classes.route import Route


class VRP:
    def __init__(
        self,
        depot: Depot,
        stops: List[Stop],
        routes: Optional[List[Route]] = None,
        passengers: Optional[List[Passenger]] = None,
    ):
        self.depot: Depot = depot
        self.stops: List[Stop] = stops
        self.routes: List[Route] = routes if routes is not None else []
        self.passengers: List[Passenger] = passengers if passengers is not None else []

    def draw_deposit(self):
        deposit_x, deposit_y = self.depot.get_coordinates()
        plt.plot(
            deposit_x,
            deposit_y,
            marker=self.depot.marker_type,
            markersize=self.depot.size + self.depot.marker_border,
            color=self.depot.marker_border_color,
        )
        plt.plot(
            deposit_x,
            deposit_y,
            marker=self.depot.marker_type,
            markersize=self.depot.size,
            color=self.depot.marker_color,
        )
        plt.text(
            deposit_x,
            deposit_y,
            str(self.depot.get_id()),
            fontsize=self.depot.font_size,
            ha="center",
            va="center",
            color=self.depot.font_color,
        )

    def draw_stops(self):
        for stop in self.stops:
            if stop._id != self.depot._id:
                stop_x, stop_y = stop._coordinates

                if stop.assigned_passengers:
                    for passenger in stop.assigned_passengers:
                        passenger_x, passenger_y = self.get_coordinates_by_passenger_id(
                            passenger
                        )
                        plt.plot(
                            passenger_x,
                            passenger_y,
                            marker=stop.marker_passenger_type,
                            markersize=stop.marker_passenger_size
                            + stop.marker_passenger_border,
                            color=stop.marker_passenger_border_color,
                        )
                        plt.plot(
                            passenger_x,
                            passenger_y,
                            marker=stop.marker_passenger_type,
                            markersize=stop.marker_passenger_size,
                            color=stop.marker_passenger_color,
                        )
                        plt.plot(
                            [stop_x, passenger_x],
                            [stop_y, passenger_y],
                            linestyle=stop.passenger_route_style,
                            color=stop.passenger_route_color,
                        )

                plt.plot(
                    stop_x,
                    stop_y,
                    marker=stop.marker_type,
                    markersize=stop.size + stop.marker_border,
                    color=stop.marker_border_color,
                )
                plt.plot(
                    stop_x,
                    stop_y,
                    marker=stop.marker_type,
                    markersize=stop.size,
                    color=stop.marker_color,
                )
                plt.text(
                    stop_x,
                    stop_y,
                    str(stop._id),
                    fontsize=stop.font_size,
                    ha="center",
                    va="center",
                    color=stop.font_color,
                )

                if stop.capacity:
                    plt.text(
                        stop_x,
                        stop_y - 5,
                        str(stop.capacity),
                        fontsize=stop.demand_size,
                        ha="center",
                        va="top",
                        color=stop.demand_color,
                    )

    def draw_routes(self):
        for i, route in enumerate(self.routes):
            i += 1
            x_coords = []
            y_coords = []
            for stop_id in route.stops:
                stop = next(s for s in self.stops if s._id == stop_id)
                x, y = stop._coordinates
                x_coords.append(x)
                y_coords.append(y)

            plt.plot(
                x_coords,
                y_coords,
                linestyle=route.line_style,
                color=route.color,
                linewidth=route.thickness,
            )

            for i in range(len(x_coords) - 1):
                start = (x_coords[i], y_coords[i])
                end = (x_coords[i + 1], y_coords[i + 1])
                midpoint = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
                plt.annotate(
                    "",
                    xy=midpoint,
                    xytext=start,
                    arrowprops=dict(
                        facecolor=route.color,
                        width=1,
                        headwidth=route.thickness + 10,
                        edgecolor="none",
                    ),
                    zorder=0,
                )

    def get_coordinates_by_passenger_id(self, passenger_id):
        for passenger in self.passengers:
            if passenger[0] == passenger_id:
                return passenger[1]
        return None
