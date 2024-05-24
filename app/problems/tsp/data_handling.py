import os


def process_files():
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


def process_solutions():
    tsp_solutions = {}
    folder_path = os.path.join(os.path.dirname(__file__), "solutions")
    for filename in os.listdir(folder_path):
        if filename.endswith(".tsp"):
            with open(os.path.join(folder_path, filename), "r") as file:
                lines = file.readlines()
                routes = []
                for i, line in enumerate(lines):
                    if line.startswith("Route:"):
                        route_line = lines[i + 1].strip()
                        route_nodes = route_line.split(" -> ")
                        routes.append([int(node) for node in route_nodes])
                        break

                tsp_solutions[filename] = {
                    "routes": routes,
                }
    return tsp_solutions
