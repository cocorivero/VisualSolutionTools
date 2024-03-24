#
# * This file contains the different instances of the problems being worked on


# * *** Simple Travelling Salesman Problem. ***
def create_data_model_tsp():
    data = {}
    locations = [
        # fmt:off
    (4, 4, "Kansas"),  # depot
    (2, 0, "Texas"), # locations to visit
    (8, 0, "California"), 
    (0, 1, "New York"), 
    (1, 1, "Florida"),
    (5, 2, "Illinois"), 
    (7, 2, "Arizona"),
    (3, 3, "Ohio"), 
    (6, 3, "Michigan"),
    (5, 5, "Washington"), 
    (8, 5, "Colorado"),
    (1, 6, "Georgia"), 
    (2, 6, "Indiana"),
    (3, 7, "Oregon"), 
    (6, 7, "Minnesota"),
    (0, 8, "Louisiana"), 
    (7, 8, "Utah")
        # fmt:on
    ]
    # Convert locations in meters using a city block dimension of 114m x 80m.
    data["locations"] = [(l[0] * 114, l[1] * 80, l[2]) for l in locations]
    data["depot"] = 0
    return data


def create_data_solution_tsp():
    solution = {}
    solution["route"] = [0, 9, 5, 8, 6, 2, 10, 16, 14, 13, 12, 11, 15, 3, 4, 1, 7, 0]
    return solution


# * *** Vehicle Routing Problem. ***
def create_data_model_vrp():
    data = {}
    data["locations"] = [
        (456, 320, "Warehouse A"),
        (228, 0, "Client A"),
        (912, 0, "Client B"),
        (0, 80, "Client C"),
        (114, 80, "Client D"),
        (570, 160, "Client E"),
        (750, 100, "Client F"),
        (342, 210, "Client G"),
        (684, 240, "Client H"),
        (570, 400, "Client I"),
        (912, 450, "Client J"),
        (114, 480, "Client K"),
        (228, 480, "Client L"),
        (342, 560, "Client M"),
        (684, 560, "Client N"),
        (0, 640, "Client O"),
        (798, 640, "Client P"),
    ]
    data["num_vehicles"] = 4
    data["depot"] = 0
    return data


def create_data_solution_vrp():
    solution = {}
    solution["vehicle_routes_mapping"] = {
        0: [0, 4, 3, 1, 7, 0],
        1: [0, 14, 16, 10, 9, 0],
        2: [0, 12, 11, 15, 13, 0],
        3: [0, 8, 2, 6, 5, 0],
    }
    return solution


# * *** Capacited Vehicle Routing Problem. ***
def create_data_model_cvrp():
    data = {}
    data["locations"] = [
        (456, 320, "Warehouse A"),
        (228, 0, "Client A"),
        (912, 0, "Client B"),
        (0, 80, "Client C"),
        (114, 80, "Client D"),
        (570, 160, "Client E"),
        (750, 100, "Client F"),
        (342, 210, "Client G"),
        (684, 240, "Client H"),
        (570, 400, "Client I"),
        (912, 450, "Client J"),
        (114, 480, "Client K"),
        (228, 480, "Client L"),
        (342, 560, "Client M"),
        (684, 560, "Client N"),
        (0, 640, "Client O"),
        (798, 640, "Client P"),
    ]
    data["num_vehicles"] = 4
    data["depot"] = 0
    data["demand"] = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]
    data["vehicle_capacity"] = [15, 15, 15, 15]
    return data


def create_data_solution_cvrp():
    solution = {}
    solution["vehicle_routes_mapping"] = {
        0: [0, 4, 3, 1, 7, 0],
        1: [0, 14, 16, 10, 9, 0],
        2: [0, 12, 11, 15, 13, 0],
        3: [0, 8, 2, 6, 5, 0],
    }
    return solution
