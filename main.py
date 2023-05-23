from data.data import get_from_csv, csv_rectangle_name, csv_image_name
from image_analyzer import ImageAnalyzer
from colorama import init

# Settings:
init()  # colorama init


# Get data:
csv_image_data_list = get_from_csv(csv_name=csv_image_name)
csv_rectangle_data_list = get_from_csv(csv_name=csv_rectangle_name)

# Analyze the image.
print('#####################')
for csv_image in csv_image_data_list:

    analyzer = ImageAnalyzer(image_path=csv_image['image_path'])
    analyzer.image_tests(csv_image=csv_image)
    rect_counter = 0
    for csv_rectangle in csv_rectangle_data_list:

        if csv_rectangle['image_path'] == analyzer.image_path:
            rect_counter += 1
            analyzer.rectangle_tests(csv_rectangle=csv_rectangle)

    print('#####################')
