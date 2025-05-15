from matplotlib import pyplot as plt
from app.problem.vrp import VRP
from app.models.stop import Stop


class VRP_2D(VRP):
    def draw_problem(self):
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
                    self.draw_passenger(stop)

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
            x_coords = []
            y_coords = []
            for stop_id in route.stops:
                stop = next((s for s in self.stops if s.id == stop_id), None)
                if stop is None:
                    raise ValueError(
                        f"El nodo con ID '{stop_id}' en la ruta '{i+1}' no se encuentra en la lista de paradas."
                    )
                x, y = stop.coords
                x_coords.append(x)
                y_coords.append(y)

            plt.plot(
                x_coords,
                y_coords,
                linestyle=route.line_style,
                color=route.color,
                linewidth=route.weight,
            )

            for j in range(len(x_coords) - 1):
                start = (x_coords[j], y_coords[j])
                end = (x_coords[j + 1], y_coords[j + 1])
                midpoint = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
                plt.annotate(
                    "",
                    xy=midpoint,
                    xytext=start,
                    arrowprops=dict(
                        facecolor=route.color,
                        width=1,
                        headwidth=route.weight + 10,
                        edgecolor="none",
                    ),
                    zorder=0,
                )

    def draw_passenger(self, stop: Stop):
        stop_x, stop_y = stop.coords
        for passenger in stop.assigned_passengers:
            passenger_obj = self.find_passenger(passenger)
            x, y = passenger_obj.coords
            plt.plot(
                [stop_x, x],
                [stop_y, y],
                linestyle=passenger_obj.passenger_route_style,
                color=passenger_obj.passenger_route_color,
                linewidth=passenger_obj.passenger_route_weight,
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
