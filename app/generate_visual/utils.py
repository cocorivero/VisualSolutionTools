from typing import List

from sympy import Dict
from app.classes.stop import Stop


def create_simple_stops(stop_data) -> List[Stop]:
    stops = []
    for stop_id, data in stop_data.items():
        coordinates = data["coordinates"]
        stop = Stop(id=str(stop_id), coordinates=coordinates)
        stops.append(stop)
    return stops


def create_stops_with_capacity(stop_data) -> List[Stop]:
    stops = []
    for stop_id, data in stop_data.items():
        coordinates = data["coordinates"]
        capacity = data["capacity"]
        stop = Stop(id=str(stop_id), coordinates=coordinates, capacity=capacity)
        stops.append(stop)
    return stops


def create_stops_with_assigned_passengers(stop_data: dict) -> List[Stop]:
    stops = []
    for stop_id, data in stop_data.items():
        coordinates = data["coordinates"]
        capacity = data["capacity"]
        passengers = data["passenger_ids"]
        stop = Stop(
            id=str(stop_id),
            coordinates=coordinates,
            capacity=capacity,
            assigned_passengers=passengers,
        )
        stops.append(stop)
    return stops
