import sys

sys.path.append("./")
from app.models.node import Node


class Passenger(Node):
    def __init__(self, id, coords, passenger_config=None):
        # Configuración por defecto para Passenger
        default_config = {
            "passenger_size": 5,
            "passenger_marker_type": "o",
            "passenger_marker_color": "red",
            "passenger_marker_border": 1,
            "passenger_marker_border_color": "black",
            "passenger_route_style": "--",
            "passenger_route_color": "grey",
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
