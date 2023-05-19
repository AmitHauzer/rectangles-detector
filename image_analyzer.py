import cv2


class ImageAnalyzer:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)

        if self.image is None:
            raise ValueError("Error reading image or image file not found.")

    def detect_rectangles(self) -> list:
        """
        :return: rectangles_details.
        """
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

        return rectangles_list

    def get_image_details(self) -> dict:
        height, width, _ = self.image.shape
        background = tuple(self.image[0, 0][::-1])
        return {
            'h': height,
            'w': width,
            'background': background,
        }
