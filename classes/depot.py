class Depto:
    def __init__(self, data: tuple, index: int):
        self.data = data
        self.index = index

    def get_depot_name(self):
        return self.data[2]

    def get_depot_coordinates(self):
        return self.data[:2]
