from create_image import ImageGenerator
from image_analyzer import ImageAnalyzer

# settings:
folder = './images/'
image_name = 'image5.png'

# Analyze the image.
image_path = f'{folder}{image_name}'
analyzer = ImageAnalyzer(image_path=image_path)
image_details = analyzer.get_image_details()
rectangles_list = analyzer.detect_rectangles()

# Create a copy with the image details.
copy_img = ImageGenerator(path=f'{folder}/copy_{image_name}',
                          image_height=image_details['h'],
                          image_width=image_details['w'],
                          background_color=image_details['background'])
copy_img.draw_rectangle(rectangles=rectangles_list)
