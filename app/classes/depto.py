class Depto:
    def __init__(self, data: tuple, index: int = None):
        self.data = data
        self.index = index

    def get_depot_coordinates(self):
        return self.data[:2]
