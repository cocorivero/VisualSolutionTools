import os
import re

###########################
# DATA TSPLIB
###########################


def process_files_vrp():
    """
    Processes VRP instance files.

    This function iterates through all files in the 'instances' directory and reads
    those ending with '.vrp'. It extracts location coordinates from the 'NODE_COORD_SECTION'
    to construct VRP instances. Each file is assumed to represent a single vehicle route.
    Instances of Capacitated Vehicle Routing Problem (CVRP) are used, ignoring the demand
    constraints to convert them into instances of Vehicle Routing Problem (VRP).

    Returns:
        dict: A dictionary where keys are filenames and values are dictionaries
        representing VRP instances with the following keys:
            - "locations" (list of tuples): Coordinates of locations to be visited.
            - "num_vehicles" (int): The number of vehicles (assumed to be 1 per instance).
            - "depot" (int): The index of the depot location (assumed to be 0).
    """

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
    """
    Reads a CVRP instance from a text file.

    This function reads a text file containing a Capacitated Vehicle Routing Problem (CVRP) instance.
    It extracts the number of vehicles, their capacities, and the coordinates of the locations.
    The function ignores demand values and assumes the first location as the depot.

    Args:
        file (str): The path to the text file containing the CVRP instance.

    Returns:
        dict: A dictionary containing the following keys:
            - "locations" (list of tuples): A list of (x, y) coordinates for each location.
            - "num_vehicles" (int): The number of vehicles available.
            - "vehicle_capacities" (list of int): The capacities of each vehicle.
            - "depot" (int): The index of the depot, assumed to be 0.
    """
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
    """
    Processes text files containing problem instances.

    This function reads all .txt files from the 'instances' directory and processes
    them to extract problem data. It constructs the full path for the 'instances'
    directory and verifies its existence. If the directory does not exist, it raises
    a FileNotFoundError. For each .txt file found, it reads the file using the
    read_file_vrp_txt function and stores the data in a dictionary with filenames as keys.

    Returns:
        dict: A dictionary where keys are filenames and values are data extracted
        from the corresponding files.
    """

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


def process_solutions_vrp():
    """
    Processes VRP solution files and extracts routes.

    This function iterates through all files in the 'solutions' directory and reads
    those ending with '.txt'. It extracts routes from the solution files and returns
    them in the specified format.

    Returns:
        dict: A dictionary where keys are filenames and values are lists of route details.
              Each route detail is represented as a dictionary containing the following keys:
                  - "vehicle": The vehicle index.
                  - "route": A list of node indices representing the route.
                  - "distance": The distance traveled on the route.
    """
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
