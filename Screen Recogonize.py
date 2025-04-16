import easyocr
import pyautogui
from PIL import Image, ImageOps
import numpy as np
import time
from plyer import notification
from torchgen.executorch.api.types import scalarT


def notify():
    notification.notify(
        title="Condition Met",
        message="You have a suited connector or a premium",
        timeout=5  
    )

def checkHand(i,j,k,l):
    reader = easyocr.Reader(['en'])

    region = (i,j,k,l)

    screenshot = pyautogui.screenshot(region=region)
    screenshot_gray = ImageOps.grayscale(screenshot)
    screenshot_np = np.array(screenshot_gray)

    result = reader.readtext(screenshot_np)

    extracted_text = [text for (_, text, _) in result]


    return extracted_text

COLORS = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0)
}


def capture_area_and_get_color(x, y, width, height):

    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    img_np = np.array(screenshot)

    avg_color = np.mean(img_np, axis=(0, 1))

    avg_color = tuple(map(int, avg_color))

    return avg_color


def closest_color(rgb_color):
    distances = {color: np.sqrt(sum((rgb_color[i] - COLORS[color][i]) ** 2 for i in range(3))) for color in COLORS}
    return min(distances, key=distances.get)

condition_before = ""

i = True

while i:
    condition_met = checkHand(1330, 1015, 160, 58)

    result = ''.join(condition_met).replace(" ", f"")

    color1 = closest_color(capture_area_and_get_color(1390, 1090, 10, 10))

    color2 = closest_color(capture_area_and_get_color(1460, 1100, 10, 10))

    print(f"Hand: {result}, Suits: {color1}, {color2}")

    valid_pairs = ["AA", "KK", "QQ", "JJ", "1010", "99", "88", "77", "AK", "KA", "00", "QA", "AQ", "7"
                   "A0", "0A", "KQ", "QK", "K0", "0K", "AJ", "JA", "KJ", "JK", "66", "55", "44", "33", "22",
                   "||", "A|", "|A", "A10", "10A", "0A", "A0f"]
    suited_connectors = ["QJ", "JQ", "10J", "J10", "109", "910", "89", "98",
                         "78", "87", "67", "76", "56", "65", "KQ", "QK", "A9", "9A", "A5", "5A",
                         "A3", "3A", "A2", "2A", "4A", "4A", "Q10", "10Q",
                         "KJ", "JK"]

    if result in valid_pairs:
        notify()
        print(f"Condition met with hand {result}! Exiting...")
        break
    if result in suited_connectors and color1 == color2:
        if result != condition_before:
            notify()
            print(f"Condition met with suited connecter {result}! Exiting...")
            break
        else:
            continue
    if result != condition_before:
        pyautogui.press('f')
    condition_before = result
    time.sleep(5)

