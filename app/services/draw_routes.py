import random
import matplotlib.pyplot as plt


def draw_route(locations, route, color_line="blue", displacement=0.05):
    for i in range(len(route) - 1):
        # Obtener las coordenadas del punto de inicio y punto final
        start_point = locations[route[i]]
        end_point = locations[route[i + 1]]

        # Calcular el vector de dirección
        dx = end_point[0] - start_point[0]
        dy = end_point[1] - start_point[1]
        distance = (dx**2 + dy**2) ** 0.1

        # Calcular el factor de desplazamiento
        dx_displacement = displacement * (dx / distance)
        dy_displacement = displacement * (dy / distance)

        # Calcular nuevas coordenadas con desplazamiento
        start_point_displaced = (
            start_point[0] + dx_displacement,
            start_point[1] + dy_displacement,
        )
        end_point_displaced = (
            end_point[0] - dx_displacement,
            end_point[1] - dy_displacement,
        )

        # Dibujar la flecha entre los puntos desplazados
        plt.annotate(
            "",
            xy=end_point_displaced,
            xytext=start_point_displaced,
            arrowprops=dict(arrowstyle="->", color=color_line),
        )
        # Añadir los números a cada nodo
    for idx, point in enumerate(route[1:-1], start=1):
        x, y = locations[point]
        plt.text(x, y, str(idx), fontsize=8, ha="center", va="center", color="black")


# Dibuja la ruta del TSP
def draw_tsp_route(locations, route):
    draw_route(locations, route, "#87CEEB")


# Dibuja la ruta del VRP
def draw_vrp_route(locations, vehicle_routes_mapping):
    for route in vehicle_routes_mapping.items():
        if route[1] == [0, 0]:
            continue
        color = "#" + "".join([random.choice("0123456789ABCDEF") for _ in range(6)])
        draw_route(locations, route[1], color)


# Dibuja la ruta del CVRP
def draw_cvrp_route(locations, vehicle_routes_mapping):
    for route in vehicle_routes_mapping.items():
        if route[1] == [0, 0]:
            continue
        color = "#" + "".join([random.choice("0123456789ABCDEF") for _ in range(6)])
        draw_route(locations, route[1], color)
