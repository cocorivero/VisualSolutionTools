import sys


sys.path.append("./")
from typing import List, Optional
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D

from app.models.stop import Stop
from app.models.passenger import Passenger
from app.models.depot import Depot
from app.models.route import Route


class VRP:
    def __init__(
        self,
        problem_name: str,
        depot: Depot,
        stops: List[Stop],
        routes: Optional[List[Route]] = None,
        passengers: Optional[List[Passenger]] = None,
    ):
        self.problem_name: str = problem_name
        self.depot: Depot = depot
        self.stops: List[Stop] = stops
        self.routes: List[Route] = routes if routes is not None else []
        self.passengers: List[Passenger] = passengers if passengers is not None else []

    def draw_problem_2d(self):
        """Dibuja el problema en 2D utilizando Matplotlib."""
        self.draw_routes()
        self.draw_stops()
        self.draw_depot()
        plt.xlabel("Coordenada X")
        plt.ylabel("Coordenada Y")
        plt.title(self.problem_name)
        plt.tight_layout()
        plt.show()

    def draw_depot(self):
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
                        passenger_x, passenger_y = passenger.get_coordinates()
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

    def draw_legend(self):
        if not self.routes:
            plt.text(
                1.05,
                1,
                "No hay rutas disponibles",
                transform=plt.gca().transAxes,
                fontsize=12,
                verticalalignment="top",
            )
        else:
            legend_elements = []
            for route in self.routes:
                stop_chunks = [
                    " -> ".join(route.stops[i : i + 5])
                    for i in range(0, len(route.stops), 5)
                ]
                stops_with_breaks = "\n".join(stop_chunks)

                legend_label = f"Ruta {route.route_id}:\n{stops_with_breaks}"
                legend_elements.append(
                    Line2D(
                        [0],
                        [0],
                        color=route.color,
                        lw=route.thickness,
                        label=legend_label,
                    )
                )

            plt.legend(
                handles=legend_elements,
                loc="upper left",
                bbox_to_anchor=(1.05, 1),
                borderaxespad=0.0,
                title="* Leyenda *",
            )
