from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
from app.classes.stop.stop import Stop
from app.classes.passenger import Passenger


class StopFactory(ABC):
    @abstractmethod
    def create_stops(
        self,
        stop_data: Dict[str, Dict[str, Tuple[float, float]]],
        stop_config: Dict,
        with_capacity: bool = False,
        with_assigned_passengers: bool = False,
    ) -> List[Stop]:
        pass


class ConcreteStopFactory(StopFactory):
    def create_stops(
        self,
        stop_data: Dict[str, Dict[str, Tuple[float, float]]],
        stop_config: Dict,
        with_capacity: bool = False,
        with_assigned_passengers: bool = False,
    ) -> List[Stop]:
        def create_passengers(
            passenger_data: List[Tuple[str, Tuple[float, float]]]
        ) -> List[Passenger]:
            return [
                Passenger(id=passenger_id, coordinates=coordinates)
                for passenger_id, coordinates in passenger_data
            ]

        stops = []
        for stop_id, data in stop_data.items():
            assigned_passengers = (
                create_passengers(data["passengers"])
                if with_assigned_passengers
                else []
            )
            stop = Stop(
                id=str(stop_id),
                coordinates=data["coordinates"],
                size=stop_config.get("stop_size", 15),
                marker_type=stop_config.get("stop_marker_type", "o"),
                marker_color=stop_config.get("stop_marker_color", "white"),
                marker_border=stop_config.get("stop_marker_border", 2),
                marker_border_color=stop_config.get(
                    "stop_marker_border_color", "black"
                ),
                font_color=stop_config.get("stop_font_color", "black"),
                font_size=stop_config.get("stop_font_size", 8),
                demand_size=stop_config.get("stop_demand_size", 8),
                demand_color=stop_config.get("stop_demand_color", "black"),
                marker_passenger_type=stop_config.get(
                    "stop_marker_passenger_type", "o"
                ),
                marker_passenger_size=stop_config.get("stop_marker_passenger_size", 5),
                marker_passenger_color=stop_config.get(
                    "stop_marker_passenger_color", "red"
                ),
                marker_passenger_border=stop_config.get(
                    "stop_marker_passenger_border", 1
                ),
                marker_passenger_border_color=stop_config.get(
                    "passenger_route_color", "black"
                ),
                passenger_route_style=stop_config.get("passenger_route_style", "--"),
                passenger_route_color=stop_config.get("passenger_route_color", "grey"),
                capacity=data.get("capacity") if with_capacity else None,
                assigned_passengers=assigned_passengers,
            )
            stops.append(stop)
        return stops
