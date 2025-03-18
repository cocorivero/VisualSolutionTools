import sys

sys.path.append("./")
from app.models.node import Node


class Depot(Node):
    def __init__(
        self,
        id,
        coords,
        view_mode,
        depot_config=None,
    ):
        # Configuración por defecto para Depot
        default_config = {
            "depot_size": 18,
            "depot_marker_type": ("o" if view_mode == "2d" else "home"),
            "depot_marker_color": ("lime" if view_mode == "2d" else "green"),
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

    def print_depot(self):
        print(f"ID del Depot: {self.id}")
        print(f"Coordenadas: {self.coords}")
        print(f"Tamaño: {self.size}")
        print(f"Tipo de marcador: {self.marker_type}")
        print(f"Color del marcador: {self.marker_color}")
        print(f"Ancho del borde del marcador: {self.marker_border}")
        print(f"Color del borde del marcador: {self.marker_border_color}")
        print(f"Tamaño de fuente: {self.font_size}")
        print(f"Color de fuente: {self.font_color}")
