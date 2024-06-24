from typing import List
from app.classes.stop import Stop


def create_stops_from_dict(stop_data: dict) -> List[Stop]:
    stops = []
    for stop_id, data in stop_data.items():
        if len(data) == 2:  # Solo coordenadas proporcionadas
            stop = Stop(id=str(stop_id), coordinates=data)
        elif len(data) == 3:  # Coordenadas y capacidad proporcionadas
            stop = Stop(id=str(stop_id),
                        coordinates=data[:2], capacity=data[2])
        stops.append(stop)
    return stops
