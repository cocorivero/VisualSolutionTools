import random
import matplotlib.pyplot as plt


def draw_route(locations, route, color_line):
    for i in range(len(route) - 1):
        # Obtener las coordenadas del punto de inicio y punto final
        start_point = locations[route[i]]
        end_point = locations[route[i + 1]]
        # Calcular la diferencia en las coordenadas x e y
        dx = end_point[0] - start_point[0]
        dy = end_point[1] - start_point[1]
        # Calcular la distancia entre los puntos
        distance = (dx**2 + dy**2) ** 0.5
        # Definir el desplazamiento para que la flecha no comience en el punto exacto
        displacement = 25
        dx -= displacement * (dx / distance)
        dy -= displacement * (dy / distance)
        # Dibujar la flecha entre los puntos con color rojo
        plt.arrow(
            start_point[0],
            start_point[1],
            dx,
            dy,
            color=color_line,
            width=1,
            head_width=10,
            length_includes_head=True,
            zorder=2,
        )


# Dibuja la ruta del TSP
def draw_tsp_route(locations, route):
    draw_route(locations, route, "#00FF00")


# Dibuja la ruta del VRP
def draw_vrp_route(locations, vehicle_routes_mapping):
    for vehicle_id, route in vehicle_routes_mapping.items():
        color = "#" + "".join([random.choice("0123456789ABCDEF") for _ in range(6)])
        draw_route(locations, route, color)


# Dibuja la ruta del CVRP
def draw_cvrp_route(locations, vehicle_routes_mapping):
    for vehicle_id, route in vehicle_routes_mapping.items():
        color = "#" + "".join([random.choice("0123456789ABCDEF") for _ in range(6)])
        draw_route(locations, route, color)
