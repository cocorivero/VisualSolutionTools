import json
import os


def process_files_tsp():
    tsp_data = {}
    folder_path = os.path.join(
        os.path.dirname(__file__), "problems_instances", "tsp", "instances"
    )
    for filename in os.listdir(folder_path):
        if filename.endswith(".tsp"):
            instance_name = filename.replace(".tsp", "")
            with open(os.path.join(folder_path, filename), "r") as file:
                lines = file.readlines()
                node_coord_section_index = lines.index("NODE_COORD_SECTION\n")
                locations = {}
                for line in lines[node_coord_section_index + 1 :]:
                    if line.strip() == "EOF":
                        break
                    parts = line.split()
                    node_id = int(parts[0])
                    x_coord = float(parts[1])
                    y_coord = float(parts[2])
                    locations[node_id] = (x_coord, y_coord)

                depot_id = next(
                    iter(locations)
                )  # Obtener el ID del primer nodo como el ID del depósito
                # Convertir el ID del depósito a cadena
                depot_id_str = str(depot_id)

                tsp_data[instance_name] = {
                    "depot_id": depot_id_str,
                    "locations": locations,
                }
    return tsp_data


def process_solutions_tsp():
    tsp_solutions = {}
    folder_path = os.path.join(
        os.path.dirname(__file__), "problems_instances", "tsp", "solutions"
    )
    for filename in os.listdir(folder_path):
        if filename.endswith(".tsp"):
            instance_name = filename.replace(".tsp", "")
            with open(os.path.join(folder_path, filename), "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Route:"):
                        route_line = lines[i + 1].strip()
                        route_nodes = route_line.split(" -> ")
                        route = [str(int(node) + 1) for node in route_nodes]
                        if instance_name not in tsp_solutions:
                            tsp_solutions[instance_name] = []
                        tsp_solutions[instance_name].append(route)
    return tsp_solutions


def load_data_tsp():
    instance_name = "ulysses22"
    tsp_data = process_files_tsp()
    data = tsp_data[instance_name]
    tsp_solutions = process_solutions_tsp()
    routes = tsp_solutions[f"solution_{instance_name}"]
    return data, routes


################################################


def process_files_vrp():
    vrp_data = {}
    folder_path = os.path.join(
        os.path.dirname(__file__), "problems_instances", "vrp", "instances"
    )
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            instance_name = filename.replace(".txt", "")
            with open(os.path.join(folder_path, filename), "r") as file:
                lines = file.readlines()
                data_lines = lines[5:]
                depot_info = data_lines[0].strip().split()
                depot_id = int(depot_info[0])
                locations = {}
                for line in data_lines:
                    parts = line.split()
                    if len(parts) < 4:
                        continue
                    node_id = int(parts[0])
                    x_coord = float(parts[1])
                    y_coord = float(parts[2])
                    locations[node_id] = (x_coord, y_coord)
                depot_id_str = str(depot_id)
                vrp_data[instance_name] = {
                    "depot_id": depot_id_str,
                    "locations": locations,
                }
    return vrp_data


def process_solutions_vrp():
    vrp_solutions = {}
    folder_path = os.path.join(
        os.path.dirname(__file__), "problems_instances", "vrp", "solutions"
    )
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            instance_name = filename.replace(".txt", "")
            with open(os.path.join(folder_path, filename), "r") as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Route for vehicle"):
                        route_line = lines[i + 1].strip()
                        route_nodes = route_line.split(" -> ")
                        if len(route_nodes) > 2:
                            route = [str(int(node)) for node in route_nodes]
                            if instance_name not in vrp_solutions:
                                vrp_solutions[instance_name] = []
                            vrp_solutions[instance_name].append(route)
    return vrp_solutions


def load_data_vrp_txt():
    instance_name = "p1"
    vrp_data = process_files_vrp()
    data = vrp_data[instance_name]
    vrp_solutions = process_solutions_vrp()
    routes = vrp_solutions[f"solution_{instance_name}"]
    return data, routes


###############################################


def process_files_cvrp():
    cvrp_data = {}
    folder_path = os.path.join(
        os.path.dirname(__file__), "problems_instances", "cvrp", "instances"
    )
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            instance_name = filename.replace(".txt", "")
            with open(os.path.join(folder_path, filename), "r") as file:
                lines = file.readlines()
                data_lines = lines[5:]
                depot_info = data_lines[0].strip().split()
                depot_id = int(depot_info[0])
                locations = {}
                for line in data_lines:
                    parts = line.split()
                    if len(parts) < 4:
                        continue
                    node_id = int(parts[0])
                    x_coord = float(parts[1])
                    y_coord = float(parts[2])
                    capacity = int(parts[3])
                    locations[node_id] = (x_coord, y_coord, capacity)
                depot_id_str = str(depot_id)
                cvrp_data[instance_name] = {
                    "depot_id": depot_id_str,
                    "locations": locations,
                }
    return cvrp_data


def process_solutions_cvrp():
    cvrp_solutions = {}
    folder_path = os.path.join(
        os.path.dirname(__file__), "problems_instances", "cvrp", "solutions"
    )
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            instance_name = filename.replace(".txt", "")
            with open(os.path.join(folder_path, filename), "r") as file:
                lines = file.readlines()
                i = 0
                while i < len(lines):
                    line = lines[i]
                    if line.startswith("Route for vehicle"):
                        i += 1
                        route_line = lines[i].strip()
                        route_nodes = [
                            node.split()[0] for node in route_line.split("->")
                        ]
                        if instance_name not in cvrp_solutions:
                            cvrp_solutions[instance_name] = []
                        cvrp_solutions[instance_name].append(route_nodes)
                    i += 1
    return cvrp_solutions


def load_data_cvrp():
    instance_name = "p15"
    cvrp_data = process_files_cvrp()
    data = cvrp_data[instance_name]
    cvrp_solutions = process_solutions_cvrp()
    routes = cvrp_solutions[f"solution_{instance_name}"]
    return data, routes


###############################################
def process_files_new_format():
    new_format_data = {}
    folder_path = os.path.join(
        os.path.dirname(__file__), "problems_instances", "bss", "solutions"
    )
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            instance_name = filename.replace(".json", "")
            with open(os.path.join(folder_path, filename), "r") as file:
                data = json.load(file)
                # Obtener el id del depósito
                depots = data.get("depots", [])
                if depots:
                    depot_id = depots[0]["id"]
                else:
                    depot_id = None
                # Obtener información de las paradas
                locations = []
                for bus_stop in data.get("bus_stops", []):
                    stop_id = bus_stop["id"]
                    coordinates = (bus_stop["coordinate_x"], bus_stop["coordinate_y"])
                    passenger_ids = [
                        passenger["passenger_id"]
                        for passenger in bus_stop.get("passenger_list", [])
                    ]
                    capacity = data.get("max_bus_stop_capacity")
                    locations.append((stop_id, coordinates, passenger_ids, capacity))
                new_format_data[instance_name] = {
                    "depot_id": depot_id,
                    "locations": locations,
                }
    return new_format_data


def load_data_bss():
    instance_name = "BSS_solution-69_B-3_P-25_D-1_MW-40.0_MBC-15_MVC-25_BSS"
    data_solution = process_files_new_format()
    data = data_solution[instance_name]
    return data
