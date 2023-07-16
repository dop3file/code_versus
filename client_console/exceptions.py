from dependencies import *


class ClientBaseException(Exception):
    ...


class ServerIsNotAvailable(ClientBaseException):
    message = "[error]Сервер в данный момент недоступен[/error]"


class Unauthorized(ClientBaseException):
    message = "[error]Неправильный логин или пароль![/error]"


def catch_exception(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as error:
            if issubclass(type(error), ClientBaseException):
                console.print(error.message)
            else:
                print(error)
    return wrapper
