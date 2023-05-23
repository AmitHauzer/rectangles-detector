import ast
import csv

# Settings:
csv_image_name = './data/image_data.csv'
csv_rectangle_name = './data/rectangle_data.csv'


def save_image_to_csv(details, csv_name=csv_image_name) -> None:
    fieldnames = ['image_path', 'image_width',
                  'image_height', 'image_background']

    with open(csv_name, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # Write header if file is empty
        if f.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'image_path': details.path,
            'image_width': details.image_width,
            'image_height': details.image_height,
            'image_background': details.image_background,
        })


def save_rectangles_to_csv(details, csv_name=csv_rectangle_name) -> None:
    fieldnames = ['image_path', 'x', 'y', 'w', 'h', 'color']

    with open(csv_name, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # Write header if file is empty
        if f.tell() == 0:
            writer.writeheader()
        for rectangle in details.rectangles:
            writer.writerow({
                'image_path': details.path,
                'x': rectangle['x'],
                'y': rectangle['y'],
                'w': rectangle['w'],
                'h': rectangle['h'],
                'color': rectangle['color'],
            })


def save_to_csv(details):
    save_image_to_csv(details=details)
    save_rectangles_to_csv(details=details)


def get_from_csv(csv_name) -> list:
    data = []
    with open(csv_name, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # for image
            if row.get('image_width'):
                row['image_width'] = int(row['image_width'])
                row['image_height'] = int(row['image_height'])
                row['image_background'] = ast.literal_eval(
                    row['image_background'])
            # for rectangel
            if row.get('x'):
                row['x'] = int(row['x'])
                row['y'] = int(row['y'])
                row['w'] = int(row['w'])
                row['h'] = int(row['h'])
                row['color'] = ast.literal_eval(row['color'])
            data.append(row)
    return data
