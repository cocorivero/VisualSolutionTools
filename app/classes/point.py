from abc import ABC
from typing import Tuple


class Point(ABC):
    def __init__(
        self,
        id: str,
        coordinates: Tuple[float, float],
    ):
        self._id: str = id
        self._coordinates: Tuple[float, float] = coordinates

    def get_id(self) -> str:
        return self._id

    def get_coordinates(self) -> Tuple[float, float]:
        return self._coordinates
