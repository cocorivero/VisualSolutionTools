from typing import Tuple


class Passenger:
    def __init__(
        self,
        id: str,
        coordinates: Tuple[float, float],
    ):
        self.id: str = id
        self.coordinates: Tuple[float, float] = coordinates
