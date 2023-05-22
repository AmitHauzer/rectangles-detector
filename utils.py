from colorama import Fore


def message(text, result, type=''):
    if type == 'good':
        color = Fore.GREEN
    elif type == 'error':
        color = Fore.RED
    elif type == '':
        color = Fore.RESET
    print(f"{text.ljust(22)}{color}{result}{Fore.RESET}")


def compare(value1, value2, label):
    if value1 == value2:
        message(text=f'\t{label}:', result='Pass.', type='good')
    else:
        message(text=f'\t{label}:', result='Failed.', type='error')


def check_diff(value1, value2, diff_set, label):
    if abs(value1 - value2) <= diff_set:
        message(text=f'\t{label}:', result='Pass.', type='good')
    else:
        message(text=f'\t{label}:', result='Failed.', type='error')
