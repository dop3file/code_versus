import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def back_handler(func):
    def wrapper(obj, *args, **kwargs):
        try:
            return func(obj, *args, **kwargs)
        except KeyboardInterrupt:
            return obj.back()
    return wrapper