import sys

sys.path.append("./")

from app.models.node import Node


class Stop(Node):
    def __init__(
        self,
        id,
        coords,
        stop_config=None,
        assigned_passengers=None,
        capacity=None,
    ):
        # Definir valores predeterminados para la configuración de Stop
        default_config = {
            "stop_size": 15,
            "stop_marker_type": "o",
            "stop_marker_color": "white",
            "stop_marker_border": 2,
            "stop_marker_border_color": "black",
            "stop_font_color": "black",
            "stop_font_size": 8,
            "stop_demand_size": 8,
            "stop_demand_color": "red",
        }

        # Actualizar la configuración con cualquier valor pasado
        stop_config = stop_config or {}
        config = {**default_config, **stop_config}

        # Llamar al constructor de la clase base (Node) pasando los atributos comunes
        super().__init__(
            id,
            coords,
            size=config["stop_size"],
            marker_type=config["stop_marker_type"],
            marker_color=config["stop_marker_color"],
            marker_border=config["stop_marker_border"],
            marker_border_color=config["stop_marker_border_color"],
        )

        # Asignar los atributos específicos de Stop
        self.font_color = config["stop_font_color"]
        self.font_size = config["stop_font_size"]
        self.demand_size = config["stop_demand_size"]
        self.demand_color = config["stop_demand_color"]
        self.assigned_passengers = assigned_passengers or []
        self.capacity = capacity or False

    def print_stop(self):
        print(f"ID del Depot: {self.id}")
        print(f"Coordenadas: {self.coords}")
        print(f"Tamaño: {self.size}")
        print(f"Tipo de marcador: {self.marker_type}")
        print(f"Color del marcador: {self.marker_color}")
        print(f"Ancho del borde del marcador: {self.marker_border}")
        print(f"Color del borde del marcador: {self.marker_border_color}")
        print(f"Tamaño de fuente: {self.font_size}")
        print(f"Color de fuente: {self.font_color}")

        print(f"Tamaño de la demanda: {self.demand_size}")
        print(f"Color de la demanda: {self.demand_color}")
        print(f"Pasajeros asignados: {self.assigned_passengers}")
        print(f"Tiene capacidad: {self.capacity}")
