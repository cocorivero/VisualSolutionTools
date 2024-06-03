import os
import re


#######################
# DATA CVRPMD
#######################


def read_file_cvrp_txt(file):
    locations = []
    demands = []
    num_locations = 0

    with open(file, "r") as f:
        lines = f.readlines()
        num_vehicles = int(lines[0].split()[2])
        capacities = []
        for i in range(1, num_vehicles + 1):
            capacities.extend(map(int, lines[i].split()))

        for line in lines[1:]:
            if len(line.strip()) == 0:
                break
            data = line.split()
            if len(data) == 4:
                x_coord = float(data[1])
                y_coord = float(data[2])
                locations.append((x_coord, y_coord))
                demand = int(data[3]) if data[3] else 0
                demands.append(demand)
                num_locations += 1

    return {
        "locations": locations,
        "num_vehicles": num_vehicles,
        "vehicle_capacities": capacities,
        "demands": demands,
        "depot": 0,
    }


def process_files_cvrp_txt():
    total_data = {}
    instances_path = os.path.join(
        os.path.dirname(__file__), "instances"
    )  # Constructs the full path for 'instances'

    if not os.path.exists(instances_path):
        raise FileNotFoundError(f"The directory '{instances_path}' does not exist.")

    files = os.listdir(instances_path)
    for file in files:
        if file.endswith(".txt"):
            route = os.path.join(instances_path, file)
            data = read_file_cvrp_txt(route)
            total_data[file] = data
    return total_data


def process_solutions_cvrp_txt():
    solution_routes = {}
    folder_path = os.path.join(os.path.dirname(__file__), "solutions")

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r") as file:
                lines = file.readlines()
                route_details = []
                current_route = None

                for line in lines:
                    if line.startswith("Route for vehicle"):
                        # Extract vehicle index from the line
                        vehicle_index = int(re.findall(r"\d+", line)[0])
                        current_route = {
                            "vehicle": vehicle_index,
                            "route": [],
                            "distance": 0,
                        }
                    elif line.strip().startswith("Distance of the route:"):
                        # Extract distance from the line
                        distance = int(re.findall(r"\d+", line)[0])
                        current_route["distance"] = distance
                        route_details.append(current_route)
                        current_route = None
                    elif current_route is not None:
                        # Extract node indices from the line, only before 'Load()'
                        nodes = [int(node.split()[0]) for node in line.split("->")]
                        current_route["route"].extend(nodes)

                solution_routes[filename] = route_details

    return solution_routes


def load_data_cvrp_txt():
    instance_name = "p31"
    cvrp_txt_data = process_files_cvrp_txt()
    data = cvrp_txt_data[f"{instance_name}.txt"]
    cvrp_solutions_txt = process_solutions_cvrp_txt()
    data_solution = cvrp_solutions_txt[f"solution_{instance_name}.txt"]
    routes = {entry["vehicle"]: entry["route"] for entry in data_solution}
    return data, routes
