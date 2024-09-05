from abc import ABC, abstractmethod
from typing import Dict, Tuple
from app.classes.depot.depot import Depot


class DepotFactory(ABC):
    @abstractmethod
    def create_depot(
        self,
        depot_id: str,
        stops: Dict[str, Dict[str, Tuple[float, float]]],
        config: Dict,
    ) -> Depot:
        pass


class ConcreteDepotFactory(DepotFactory):
    def create_depot(
        self,
        depot_id: str,
        stops: Dict[str, Dict[str, Tuple[float, float]]],
        config: Dict,
    ) -> Depot:
        coordinates = stops.get(depot_id, {}).get("coordinates")
        if not coordinates:
            raise ValueError(
                f"Depot ID {depot_id} no encontrado en los datos de stops."
            )
        return Depot(
            id=depot_id,
            coordinates=coordinates,
            size=config.get("depot_size", 18),
            marker_type=config.get("depot_marker_type", "o"),
            marker_color=config.get("depot_marker_color", "lime"),
            marker_border=config.get("depot_marker_border", 2),
            marker_border_color=config.get("depot_marker_border_color", "black"),
            font_color=config.get("depot_font_color", "black"),
            font_size=config.get("depot_font_size", 12),
        )
