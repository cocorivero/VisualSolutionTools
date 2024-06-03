import os
import json


def process_files_solutions():
    solution_data = {}
    folder_path = os.path.join(os.path.dirname(__file__), "solutions")
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The directory '{folder_path}' does not exist.")

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            with open(os.path.join(folder_path, filename), "r") as file:
                data = json.load(file)
                depots = data.get("depots", [])
                bus_stops = data.get("bus_stops", [])
                passengers = data.get("passenger_list", [])

                depot_coordinates = [
                    (depot["coordinate_x"], depot["coordinate_y"]) for depot in depots
                ]

                bus_stop_data = []
                for stop in bus_stops:
                    stop_coordinates = (stop["coordinate_x"], stop["coordinate_y"])
                    passenger_coordinates = [
                        (passenger["coordinate_x"], passenger["coordinate_y"])
                        for passenger in passengers
                        if passenger["id"]
                        in [p["passenger_id"] for p in stop["passenger_list"]]
                    ]
                    bus_stop_data.append(
                        {
                            "stop_coordinates": stop_coordinates,
                            "passenger_coordinates": passenger_coordinates,
                        }
                    )

                solution_data[filename] = {
                    "depot_coordinates": depot_coordinates[0],
                    "bus_stop_data": bus_stop_data,
                }

    return solution_data


def load_data_bss():
    instance_name = "BSS_solution-69_B-3_P-25_D-1_MW-40.0_MBC-15_MVC-25_BSS.json"
    data_solution = process_files_solutions()
    data = data_solution[instance_name]
    return data
