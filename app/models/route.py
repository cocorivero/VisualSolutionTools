class Route:
    def __init__(self, route_id, stops, routes_config=None, view_mode=None):
        # Configuración por defecto para Route
        default_config = {
            "route_line_style": "solid",
            "route_weight": (1 if view_mode == "2d" else 2),
            "default_color": "#000000",
        }
        routes_config = routes_config or {}
        config = {**default_config, **routes_config}

        self.route_id = route_id
        self.stops = stops
        self.line_style = config["route_line_style"]
        self.weight = config["route_weight"]
        self.color = config["default_color"]

    def print_route(self):
        print(f"ID de la Ruta: {self.route_id}")
        print(f"Paradas: {self.stops}")
        print(f"Estilo de la linea: {self.line_style}")
        print(f"Ancho de la linea: {self.weight}")
        print(f"Color de la linea: {self.color}")
