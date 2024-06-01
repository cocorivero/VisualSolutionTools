from classes.depto import Depto


class BSS:
    def __init__(self, depot_data, bus_stop_data):
        self.depot = Depto(depot_data)
        self.bus_stop_data = bus_stop_data
