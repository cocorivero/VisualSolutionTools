from typing import List, Optional, Tuple


class Stop:
    def __init__(
        self,
        id: str,
        coordinates: Tuple[float, float],
        assigned_passengers: Optional[List[str]] = None,
        capacity: Optional[int] = None,
    ):
        self.id: str = id
        self.coordinates: Tuple[float, float] = coordinates
        self.assigned_passengers: List[str] = (
            assigned_passengers if assigned_passengers is not None else []
        )
        self.capacity: Optional[int] = capacity
