import pyautogui
from PIL import Image
import numpy as np

# Define reference colors
COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0)
}


def capture_area_and_get_color(x, y, width, height):
    # Capture the screenshot of the specific area
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # Convert screenshot to a numpy array
    img_np = np.array(screenshot)

    # Calculate the average color of the region (mean along the x and y axes)
    avg_color = np.mean(img_np, axis=(0, 1))

    # Convert average color to standard Python int
    avg_color = tuple(map(int, avg_color))

    return avg_color


def closest_color(rgb_color):
    # Calculate the Euclidean distance to find the closest color
    distances = {color: np.sqrt(sum((rgb_color[i] - COLORS[color][i]) ** 2 for i in range(3))) for color in COLORS}
    return min(distances, key=distances.get)


avg_color = capture_area_and_get_color(1390, 1090, 10, 10)
closest = closest_color(avg_color)
closest1 = closest_color(capture_area_and_get_color(1460, 1100, 10, 10))

print(f"The closest color of card 1 is: {closest}")
print(f"The closest color of card 2 is: {closest1}")
