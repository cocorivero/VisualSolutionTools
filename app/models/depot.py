import sys

sys.path.append("./")
from app.models.node import Node


class Depot(Node):
    def __init__(self, id, coords, depot_config=None):
        # Configuración por defecto para Depot
        default_config = {
            "depot_size": 18,
            "depot_marker_type": "o",
            "depot_marker_color": "lime",
            "depot_marker_border": 2,
            "depot_marker_border_color": "black",
            "depot_font_color": "black",
            "depot_font_size": 12,
        }
        depot_config = depot_config or {}
        config = {**default_config, **depot_config}

        # Llamada al constructor de la clase Node pasando los atributos comunes
        super().__init__(
            id,
            coords,
            size=config["depot_size"],
            marker_type=config["depot_marker_type"],
            marker_color=config["depot_marker_color"],
            marker_border=config["depot_marker_border"],
            marker_border_color=config["depot_marker_border_color"],
        )

        # Atributos específicos de Depot
        self.font_color = config["depot_font_color"]
        self.font_size = config["depot_font_size"]
