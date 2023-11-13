

def frequency_to_rgb(frequency: int) -> tuple[int, int, int]:
    # Define the range of frequencies for visible colors
    visible_color_frequencies = [620, 530, 480, 450, 420, 380]
    
    # Corresponding RGB values for visible colors
    visible_colors_rgb = [
        (255, 0, 0),   # Red
        (255, 165, 0),  # Orange
        (255, 255, 0),  # Yellow
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (138, 43, 226)  # Violet
    ]

    # Perform linear interpolation to find the corresponding RGB value
    for i in range(len(visible_color_frequencies) - 1):
        if frequency >= visible_color_frequencies[i] and frequency <= visible_color_frequencies[i + 1]:
            # Linear interpolation
            t = (frequency - visible_color_frequencies[i + 1]) / (visible_color_frequencies[i] - visible_color_frequencies[i + 1])
            rgb_value = (
                int((1 - t) * visible_colors_rgb[i][0] + t * visible_colors_rgb[i + 1][0]),
                int((1 - t) * visible_colors_rgb[i][1] + t * visible_colors_rgb[i + 1][1]),
                int((1 - t) * visible_colors_rgb[i][2] + t * visible_colors_rgb[i + 1][2])
            )
            return rgb_value

def find_nearest_visible_color(rgb_value: tuple[int, int, int]):
    # Visible colors and their RGB values
    visible_colors_rgb = {
        "Violet": (138, 43, 226),
        "Indigo": (75, 0, 130),
        "Blue": (0, 0, 255),
        "Cyan": (0, 255, 255),
        "Green": (0, 128, 0),
        "Yellow-Green": (154, 205, 50),
        "Yellow": (255, 255, 0),
        "Orange": (255, 165, 0),
        "Red": (255, 0, 0)
    }

    # Calculate the Euclidean distance between the input RGB and each visible color
    distances = {color: sum((a - b) ** 2 for a, b in zip(rgb_value, rgb)) for color, rgb in visible_colors_rgb.items()}

    # Find the color with the minimum distance
    nearest_color = min(distances, key=distances.get)

    return visible_colors_rgb[nearest_color]

def rgb_to_frequency(rgb_value):
    # Example lookup table (replace with accurate values)
    visible_colors_rgb = {
        "Violet": (138, 43, 226),
        "Indigo": (75, 0, 130),
        "Blue": (0, 0, 255),
        "Cyan": (0, 255, 255),
        "Green": (0, 128, 0),
        "Yellow-Green": (154, 205, 50),
        "Yellow": (255, 255, 0),
        "Orange": (255, 165, 0),
        "Red": (255, 0, 0)
    }

    # Find the nearest color based on Euclidean distance
    nearest_color = min(visible_colors_rgb, key=lambda x: sum((a - b) ** 2 for a, b in zip(rgb_value, visible_colors_rgb[x])))

    # Example mapping from color to frequency (replace with accurate values)
    frequency_mapping = {
        "Violet": 700,
        "Indigo": 650,
        "Blue": 600,
        "Cyan": 550,
        "Green": 500,
        "Yellow-Green": 470,
        "Yellow": 525,
        "Orange": 580,
        "Red": 640
    }

    return frequency_mapping.get(nearest_color, None)

