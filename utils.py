from colorama import Fore


def convert_location_to_coordinates(image_width: int, image_height: int, rectangle: dict) -> tuple:
    """
    Calculate the rectangle position.
    """
    rectangle_x = (
        image_width - rectangle['w']) // 2 + rectangle['location'][0]
    rectangle_y = (
        image_height - rectangle['h']) // 2 + rectangle['location'][1]

    del rectangle['location']

    return rectangle_x, rectangle_y


def message(text, result, type=''):
    if type == 'good':
        color = Fore.GREEN
    elif type == 'error':
        color = Fore.RED
    elif type == '':
        color = Fore.RESET
    print(f"{text.ljust(22)}{color}{result}{Fore.RESET}")
