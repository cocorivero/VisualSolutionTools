from app.problem.vrp import VRP
import veroviz as vrv
import pandas as pd
import webbrowser
import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)


class VRP_MAP(VRP):
    def draw_problem(self):
        nodes_data = self.create_nodes(self.get_nodes_data())
        arcs_data = self.create_arcs(self.get_routes_data(), nodes_data)
        if isinstance(nodes_data, pd.DataFrame) and isinstance(arcs_data, pd.DataFrame):
            map_object = vrv.createLeaflet(nodes=nodes_data, arcs=arcs_data)
            map_object.save("mapa_interactivo.html")
            webbrowser.open("mapa_interactivo.html")

    def get_nodes_data(self):
        nodes_data = []
        depot_data = {
            "coords": list(self.depot.coords),
            "name": self.depot.id,
            "iconType": self.depot.marker_type,
            "iconColor": self.depot.marker_color,
        }
        nodes_data.append(depot_data)

        if self.stops:
            for stop in self.stops:
                if stop.id != self.depot.id:
                    stop_data = {
                        "coords": list(stop.coords),
                        "name": stop.id,
                        "iconType": stop.marker_type,
                        "iconColor": stop.marker_color,
                    }
                    nodes_data.append(stop_data)

        if self.passengers:
            for passenger in self.passengers:
                passenger_data = {
                    "coords": list(passenger.coords),
                    "name": passenger.id,
                    "iconType": passenger.marker_type,
                    "iconColor": passenger.marker_color,
                }
                nodes_data.append(passenger_data)

        return nodes_data

    def get_routes_data(self):
        routes_data = []
        for route in self.routes:
            route_data = {
                "route": [int(stop) for stop in route.stops],
                "color": route.color,
                "weight": route.weight,
                "style": route.line_style,
            }
            routes_data.append(route_data)
        return routes_data

    def get_passenger_routes_data(self):
        arcs = []
        for stop in self.stops:
            # Check if the stop has assigned passengers
            if stop.assigned_passengers:
                for passenger_id in stop.assigned_passengers:
                    # Find the passenger object with the corresponding id
                    passenger = next(
                        (p for p in self.passengers if p.id == passenger_id), None
                    )
                    if passenger:
                        arc = {
                            "coords": [list(passenger.coords), list(stop.coords)],
                            "color": passenger.passenger_route_color,
                            "weight": passenger.passenger_route_weight,
                            "style": passenger.passenger_route_style,
                        }
                        arcs.append(arc)
        return arcs

    def create_nodes(self, nodes_data):
        nodes = pd.concat(
            [
                vrv.createNodesFromLocs(
                    locs=[node["coords"]],
                    popupText=node["name"],
                    leafletIconPrefix="fa",
                    leafletIconType=node["iconType"],
                    leafletColor=node["iconColor"],
                )
                for node in nodes_data
            ],
            ignore_index=True,
        )
        nodes["id"] = nodes.index
        return nodes

    def create_arcs(self, routes_data, nodes_data):
        routes = None
        if self.routes:
            routes = pd.concat(
                [
                    vrv.createArcsFromNodeSeq(
                        nodeSeq=route["route"],
                        nodes=nodes_data,
                        leafletColor=route["color"],
                        leafletWeight=route["weight"],
                        leafletStyle=route["style"],
                    )
                    for route in routes_data
                ],
                ignore_index=True,
            )

        passenger_arcs = None
        if self.passengers:
            passenger_arcs = pd.concat(
                [
                    vrv.createArcsFromLocSeq(
                        locSeq=arc["coords"],
                        leafletColor=arc["color"],
                        leafletWeight=arc["weight"],
                        leafletStyle=arc["style"],
                    )
                    for arc in self.get_passenger_routes_data()
                ],
                ignore_index=True,
            )

        routes_has_value = routes is not None and not routes.empty
        passenger_has_value = passenger_arcs is not None and not passenger_arcs.empty

        if routes_has_value and passenger_has_value:
            return pd.concat([routes, passenger_arcs], ignore_index=True)
        elif routes_has_value:
            return routes
        elif passenger_has_value:
            return passenger_arcs
        else:
            return pd.DataFrame()
