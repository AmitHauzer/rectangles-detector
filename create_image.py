from PIL import Image, ImageDraw


class ImageGenerator:
    def __init__(self, path: str, image_height: int, image_width: int, background_color) -> None:
        self.path = path
        self.image_width = image_width
        self.image_height = image_height
        self.image = Image.new(
            "RGB", (image_width, image_height), background_color)
        self.image.save(self.path)

    def get_rectangle_location(self, rectangle) -> int:
        rectangle_x = (self.image_width -
                       rectangle['w']) // 2 + rectangle['location'][0]
        rectangle_y = (self.image_height -
                       rectangle['h']) // 2 + rectangle['location'][1]
        return rectangle_x, rectangle_y

    def draw_rectangle(self, rectangles: list):
        """
        Calculate the position and draw multiple rectangles.
        """
        for rectangle in rectangles:
            if rectangle.get('location'):
                rectangle['x'], rectangle['y'] = self.get_rectangle_location(
                    rectangle=rectangle)

            draw = ImageDraw.Draw(self.image)
            draw.rectangle([(rectangle['x'], rectangle['y']), (rectangle['x'] + rectangle['w'],
                           rectangle['y'] + rectangle['h'])], outline=rectangle['color'], width=3)

        self.image.save(self.path)


if __name__ == "__main__":
    # settings:
    folder = './images/'
    image_name = 'image6.png'
    image_height = 1000
    image_width = 1000
    background_color = (128, 128, 128)
    rectangles = [
        {'w': 50, 'h': 80, 'location': (-120, 200), 'color': (255, 0, 0)},
        {'w': 90, 'h': 30, 'location': (-260, 40), 'color': (255, 0, 0)},
        {'w': 70, 'h': 150, 'location': (-20, 60), 'color': (255, 0, 0)},
    ]

    img = ImageGenerator(path=f'{folder}{image_name}',
                         image_height=image_height,
                         image_width=image_width,
                         background_color=background_color)
    img.draw_rectangle(rectangles=rectangles)
