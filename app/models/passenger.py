import sys

sys.path.append("./")
from app.models.node import Node


class Passenger(Node):
    def __init__(self, id, coords, passenger_config=None, view_mode=None):
        # Configuración por defecto para Passenger
        default_config = {
            "passenger_size": 5,
            "passenger_marker_type": ("o" if view_mode == "2d" else "user"),
            "passenger_marker_color": ("red" if view_mode == "2d" else "blue"),
            "passenger_marker_border": 1,
            "passenger_marker_border_color": "black",
            "passenger_route_style": ("--" if view_mode == "2d" else "solid"),
            "passenger_route_color": "#808080",
            "passenger_route_weight": (1 if view_mode == "2d" else 2),
        }
        passenger_config = passenger_config or {}
        config = {**default_config, **passenger_config}

        # Inicializamos la parte común utilizando la clase base (Node)
        super().__init__(
            id,
            coords,
            size=config["passenger_size"],
            marker_type=config["passenger_marker_type"],
            marker_color=config["passenger_marker_color"],
            marker_border=config["passenger_marker_border"],
            marker_border_color=config["passenger_marker_border_color"],
        )

        # Atributos específicos de Passenger
        self.passenger_route_style = config["passenger_route_style"]
        self.passenger_route_color = config["passenger_route_color"]
        self.passenger_route_weight = config["passenger_route_weight"]

    def print_passenger(self):
        print(f"ID del Depot: {self.id}")
        print(f"Coordenadas: {self.coords}")
        print(f"Tamaño: {self.size}")
        print(f"Tipo de marcador: {self.marker_type}")
        print(f"Color del marcador: {self.marker_color}")
        print(f"Ancho del borde del marcador: {self.marker_border}")
        print(f"Color del borde del marcador: {self.marker_border_color}")
        print(f"Tamaño de a ruta del pasajero: {self.passenger_route_style}")
        print(f"Color de a ruta del pasajero: {self.passenger_route_color}")
        print(f"Ancho de la ruta del pasajero: {self.passenger_route_weight}")
