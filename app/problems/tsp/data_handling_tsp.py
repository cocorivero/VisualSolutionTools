import os
import re


def process_files_tsp():
    """
    Processes TSP instance files.

    This function iterates through all files in the 'instances' directory and reads
    those ending with '.tsp'. It extracts location coordinates from the 'NODE_COORD_SECTION'
    to construct Traveling Salesman Problem (TSP) instances. Each file is assumed to represent
    a single TSP instance with a single vehicle route.

    Returns:
        dict: A dictionary where keys are filenames and values are dictionaries
        representing TSP instances with the following keys:
            - "locations" (list of tuples): Coordinates of locations to be visited.
            - "num_vehicles" (int): The number of vehicles (assumed to be 1 per instance).
            - "depot" (int): The index of the depot location (assumed to be 0).
    """
    tsp_data = {}
    folder_path = os.path.join(os.path.dirname(__file__), "instances")
    for filename in os.listdir(folder_path):
        if filename.endswith(".tsp"):
            with open(os.path.join(folder_path, filename), "r") as file:
                lines = file.readlines()
                node_coord_section_index = lines.index("NODE_COORD_SECTION\n")
                locations = []
                for line in lines[node_coord_section_index + 1 :]:
                    if line.strip() == "EOF":
                        break
                    parts = line.split()
                    x_coord = float(parts[1])
                    y_coord = float(parts[2])
                    locations.append((x_coord, y_coord))

                tsp_data[filename] = {
                    "locations": locations,
                    "num_vehicles": 1,
                    "depot": 0,
                }
    return tsp_data


def process_solutions_tsp():
    """
    Processes TSP solution files and extracts routes.

    This function iterates through all files in the 'solutions' directory and reads
    those ending with '.txt'. It extracts routes from the solution files and returns
    them in the specified format.

    Returns:
        dict: A dictionary where keys are filenames and values are lists of route details.
              Each route detail is represented as a dictionary containing the following keys:
                  - "vehicle": The vehicle index (always 0 if only one vehicle).
                  - "route": A list of node indices representing the route.
                  - "distance": The distance traveled on the route.
    """
    tsp_solutions = {}
    folder_path = os.path.join(os.path.dirname(__file__), "solutions")
    for filename in os.listdir(folder_path):
        if filename.endswith(".tsp"):
            with open(os.path.join(folder_path, filename), "r") as file:
                lines = file.readlines()
                route = []
                for i, line in enumerate(lines):
                    if line.startswith("Route:"):
                        route_line = lines[i + 1].strip()
                        route_nodes = route_line.split(" -> ")
                        route.extend([int(node) for node in route_nodes])
                    elif line.strip().startswith("Objective:"):
                        distance = int(re.findall(r"\d+", line)[0])
                        tsp_solutions[filename] = {
                            "vehicle": 0,
                            "route": route,
                            "distance": distance,
                        }

    return tsp_solutions
