import cv2
from colorama import Fore
from utils import check_diff, compare


class ImageAnalyzer:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image_height = None
        self.image_width = None
        self.rectangles = None
        self.image_background = None
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise ValueError("Error reading image or image file not found.")
        self.get_image_details()
        self.detect_rectangles()

    def detect_rectangles(self) -> None:
        # Convert the image to grayscale
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # Apply edge detection to find contours
        edges = cv2.Canny(gray, 50, 150)
        contours, _ = cv2.findContours(
            edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        rectangles_list = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            # Get the color at the top-left corner of the rectangle.
            color = tuple(self.image[y+1, x+1][::-1])
            rectangles_list.append({
                'x': x,
                'y': y,
                'w': w,
                'h': h,
                'color': color,
            })
        self.rectangles = rectangles_list

    def get_image_details(self) -> None:
        self.image_height, self.image_width, _ = self.image.shape
        self.image_background = tuple(self.image[0, 0][::-1])

    def image_tests(self, csv_image: dict):
        print(f"Image file: '{self.image_path}'")
        self_dict = vars(self)
        for key in csv_image.keys():
            if key == "image_path":
                continue
            compare(value1=self_dict[key], value2=csv_image[key], label=key)

    def rectangle_tests(self, csv_rectangle: dict):
        diff_set = 2
        detected = False
        for i, rectangle in enumerate(self.rectangles, 1):

            if (abs(rectangle['x'] - csv_rectangle['x']) <= diff_set) and (abs(rectangle['y'] - csv_rectangle['y']) <= diff_set):
                print(f"\tRectangle: ({rectangle['x']},{rectangle['y']})")
                for key in rectangle:
                    if key == 'color':
                        compare(
                            value1=rectangle[key], value2=csv_rectangle[key], label=key)
                        continue
                    check_diff(
                        value1=rectangle[key], value2=csv_rectangle[key], diff_set=diff_set, label=key)
                break

            elif detected == False and i == len(self.rectangles):
                print(
                    f"{Fore.RED}Error: Rectangle ({rectangle['x']},{rectangle['y']}) not recognized{Fore.RESET}")
