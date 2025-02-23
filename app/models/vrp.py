import sys

sys.path.append("./")

from matplotlib import pyplot as plt
from app.models.depot import Depot
from app.models.stop import Stop
from app.models.route import Route
from app.models.passenger import Passenger


class VRP:
    def __init__(
        self,
        problem_name,
        depot: Depot,
        stops: list[Stop],
        routes: list[Route] = None,
        passengers: list[Passenger] = None,
    ):
        self.problem_name = problem_name
        self.depot = depot
        self.stops = stops
        self.routes = routes if routes is not None else []
        self.passengers = passengers if passengers is not None else []

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
        deposit_x, deposit_y = self.depot.coords
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
            str(self.depot.id),
            fontsize=self.depot.font_size,
            ha="center",
            va="center",
            color=self.depot.font_color,
        )

    def draw_stops(self):
        for stop in self.stops:
            if stop.id != self.depot.id:
                stop_x, stop_y = stop.coords

                if stop.assigned_passengers:
                    for passenger in stop.assigned_passengers:
                        passenger_obj = self.find_passenger(passenger.id)
                        x, y = passenger_obj.coords
                        plt.plot(
                            [stop_x, x],
                            [stop_y, y],
                            linestyle=passenger_obj.passenger_route_style,
                            color=passenger_obj.passenger_route_color,
                        )
                        plt.plot(
                            x,
                            y,
                            marker=passenger_obj.marker_type,
                            markersize=passenger_obj.size + passenger_obj.marker_border,
                            color=passenger_obj.marker_border_color,
                        )
                        plt.plot(
                            x,
                            y,
                            marker=passenger_obj.marker_type,
                            markersize=passenger_obj.size,
                            color=passenger_obj.marker_color,
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
                    str(stop.id),
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
                stop = next(s for s in self.stops if s.id == stop_id)
                x, y = stop.coords
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

    def find_passenger(self, passengers_id) -> Passenger:
        for p in self.passengers:
            if p.id == passengers_id:
                return p
        return None
