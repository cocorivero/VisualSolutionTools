from abc import ABC, abstractmethod
from typing import Dict, List
from app.models.route import Route
import random


class RouteFactory(ABC):
    @abstractmethod
    def create_routes(self, routes: List, routes_config: Dict) -> List[Route]:
        pass


class ConcreteRouteFactory(RouteFactory):
    def create_routes(self, routes: List, routes_config: Dict) -> List[Route]:
        custom_colors_list = routes_config.get(
            "custom_colors_list",
            [
                "#FF0000",
                "#00FF00",
                "#0000FF",
                "#800000",
                "#FF00FF",
                "#FFFF00",
                "#00FFFF",
                "#800000",
                "#808000",
                "#008000",
                "#008080",
                "#000080",
                "#800080",
                "#FF4500",
                "#FFD700",
                "#9ACD32",
                "#00FA9A",
                "#4682B4",
                "#6A5ACD",
                "#FF69B4",
                "#FF1493",
            ],
        )

        num_colors = len(custom_colors_list)
        created_routes = []

        for i, stops in enumerate(routes):
            if routes_config.get("random_colors", False):
                color = random.choice(custom_colors_list)
            else:
                color = custom_colors_list[i % num_colors]

            route = Route(
                route_id=i + 1,
                stops=stops,
                line_style=routes_config.get("route_line_style", "solid"),
                color=color,
                thickness=routes_config.get("route_thickness", 1),
            )
            created_routes.append(route)

        return created_routes
