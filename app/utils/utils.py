import random


def get_route_color(index, routes_config):
    custom_colors_list = routes_config.get(
        "custom_colors_list",
        [
            "#FF0000",
            "#00FF00",
            "#0000FF",
            "#800000",
            "#FF00FF",
            "#FFFF00",
            "#00FFFF",
            "#800000",
            "#808000",
            "#008000",
            "#008080",
            "#000080",
            "#800080",
            "#FF4500",
            "#FFD700",
            "#9ACD32",
            "#00FA9A",
            "#4682B4",
            "#6A5ACD",
            "#FF69B4",
            "#FF1493",
        ],
    )

    if routes_config.get("random_colors", False):
        return random.choice(custom_colors_list)
    else:
        num_colors = len(custom_colors_list)
        return custom_colors_list[index % num_colors]
