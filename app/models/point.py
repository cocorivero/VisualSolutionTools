from abc import ABC


class Point(ABC):
    def __init__(self, id, coordinates):
        self._id = id
        self._coordinates = coordinates

    def get_id(self):
        return self._id

    def get_coordinates(self):
        return self._coordinates
