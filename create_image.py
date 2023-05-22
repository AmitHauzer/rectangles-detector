from PIL import Image, ImageDraw
from data.data import save_to_csv


class ImageGenerator:
    def __init__(self, path: str, image_height: int, image_width: int, image_background: tuple, rectangles: list):
        self.path = path
        self.image_width = image_width
        self.image_height = image_height
        self.image_background = image_background
        self.rectangles = rectangles

    def convert_location_to_coordinates(self, rectangle: dict) -> tuple:
        """
        Calculate the rectangle position.
        """
        rectangle_x = (self.image_width -
                       rectangle['w']) // 2 + rectangle['location'][0]
        rectangle_y = (self.image_height -
                       rectangle['h']) // 2 + rectangle['location'][1]
        del rectangle['location']

        return rectangle_x, rectangle_y

    def draw_rectangle(self, image) -> None:
        """
        Draw multiple rectangles.
        """
        for rectangle in self.rectangles:
            if rectangle.get('location'):
                rectangle['x'], rectangle['y'] = self.convert_location_to_coordinates(
                    rectangle=rectangle)
            draw = ImageDraw.Draw(image)
            draw.rectangle([(rectangle['x'], rectangle['y']), (rectangle['x'] + rectangle['w'],
                           rectangle['y'] + rectangle['h'])], outline=rectangle['color'], width=3)

    def create_image(self) -> None:
        img = Image.new(
            "RGB", (self.image_width, self.image_height), self.image_background)
        self.draw_rectangle(image=img)
        img.save(self.path)


if __name__ == "__main__":
    # settings:
    folder = './images/'
    image_name = 'image4.png'
    image_height = 1000
    image_width = 1000
    image_background = (148, 148, 148)
    rectangles = [
        {'w': 50, 'h': 80, 'location': (180, 200), 'color': (200, 0, 0)},
        {'w': 190, 'h': 230, 'location': (-260, 140), 'color': (180, 140, 1)},
        {'w': 70, 'h': 150, 'location': (-20, 60), 'color': (255, 0, 100)},
    ]

    img = ImageGenerator(path=f'{folder}{image_name}',
                         image_height=image_height,
                         image_width=image_width,
                         image_background=image_background,
                         rectangles=rectangles)
    img.create_image()
    save_to_csv(details=img)
