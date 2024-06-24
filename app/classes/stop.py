from typing import List, Optional, Tuple


class Stop:
    def __init__(
        self,
        id: str,
        coordinates: Tuple[float, float],
        assigned_passengers: Optional[List[Tuple[float, float]]] = None,
        capacity: Optional[int] = None,
    ):
        """
        Initialize the Stop with coordinates, an optional list of assigned passengers (each with coordinates), and an optional capacity.

        :param id: Unique identifier for the stop
        :param coordinates: Coordinates of the stop (latitude, longitude)
        :param assigned_passengers: Optional list of coordinates for passengers assigned to this stop
        :param capacity: Optional capacity of the stop
        """
        self.id: str = id
        self.coordinates: Tuple[float, float] = coordinates
        self.assigned_passengers: List[Tuple[float, float]] = (
            assigned_passengers if assigned_passengers is not None else []
        )
        self.capacity: Optional[int] = capacity
