import os
import re

###########################
# DATA TSPLIB
###########################


def process_files_vrp():
    vrp_data = {}
    folder_path = os.path.join(os.path.dirname(__file__), "instances")
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The directory '{folder_path}' does not exist.")
    for filename in os.listdir(folder_path):
        if filename.endswith(".vrp"):
            with open(os.path.join(folder_path, filename), "r") as file:
                lines = file.readlines()
                locations = []
                node_coord_section_index = lines.index("NODE_COORD_SECTION\n")
                demand_section_index = lines.index("DEMAND_SECTION\n")

                for line in lines[node_coord_section_index + 1 : demand_section_index]:
                    if line.strip() == "-1":
                        break
                    parts = line.split()
                    x_coord = float(parts[1])
                    y_coord = float(parts[2])
                    locations.append((x_coord, y_coord))

                vrp_data[filename] = {
                    "locations": locations,
                    "num_vehicles": 1,
                    "depot": 0,
                }

    return vrp_data


#######################
# DATA CVRPMD
#######################


def read_file_vrp_txt(file):
    locations = []
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
                num_locations += 1

    return {
        "locations": locations,
        "num_vehicles": num_vehicles,
        "vehicle_capacities": capacities,
        "depot": 0,
    }


def process_files_vrp_txt():
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
            data = read_file_vrp_txt(route)
            total_data[file] = data
    return total_data


def process_solutions_vrp_txt():
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
                        # Extract node indices from the line
                        nodes = [int(node) for node in re.findall(r"\d+", line)]
                        current_route["route"].extend(nodes)

                solution_routes[filename] = route_details

    return solution_routes


def load_data_vrp_txt():
    instance_name = "p2"
    vrp_txt_data = process_files_vrp_txt()
    data = vrp_txt_data[f"{instance_name}.txt"]
    vrp_solutions_txt = process_solutions_vrp_txt()
    data_solution = vrp_solutions_txt[f"solution_{instance_name}.txt"]
    routes = {entry["vehicle"]: entry["route"] for entry in data_solution}
    return data, routes
