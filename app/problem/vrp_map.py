from app.problem.vrp import VRP


class VRP_MAP(VRP):
    def draw_problem(self):
        # self.draw_depot()
        # self.draw_routes()
        # self.draw_stops()
        self.draw_passengers()

    def draw_depot(self):
        self.depot.print_depot()

    def draw_stops(self):
        for index, stop in enumerate(self.stops, start=1):
            print(f"Stop {index}:")
            stop.print_stop()  # Asumiendo que cada objeto Stop tiene este método
            print("-" * 40)

    def draw_routes(self):
        for index, route in enumerate(self.routes, start=1):
            print(f"Ruta {index}:")
            route.print_route()
            print("-" * 40)

    def draw_passengers(self):
        for index, passenger in enumerate(self.passengers, start=1):
            print(f"Passenger {index}:")
            passenger.print_passenger()  # Asumiendo que cada objeto Passenger tiene este método
            print("-" * 40)
