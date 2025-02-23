class Route:
    def __init__(self, route_id, stops, routes_config=None):
        # Configuración por defecto para Route
        default_config = {
            "route_line_style": "solid",
            "route_thickness": 1,
            "default_color": "#000000",
        }
        routes_config = routes_config or {}
        config = {**default_config, **routes_config}

        self.route_id = route_id
        self.stops = stops
        self.line_style = config["route_line_style"]
        self.thickness = config["route_thickness"]
        self.color = config["default_color"]
