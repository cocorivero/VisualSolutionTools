class Route:
    def __init__(
        self, route_id, stops, line_style="solid", color="#000000", thickness=2
    ):

        self.route_id = route_id
        self.stops = stops
        self.line_style = line_style
        self.color = color
        self.thickness = thickness
