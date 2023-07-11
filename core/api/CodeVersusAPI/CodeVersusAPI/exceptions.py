from rest_framework.views import exception_handler
from rest_framework.response import Response


class CustomBaseException(Exception):
    ...


class ServiceException(CustomBaseException):
    status_code = 500
    message = "Service Error"


class NotFoundException(CustomBaseException):
    status_code = 404
    message = "Not Found"


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if issubclass(type(exc), CustomBaseException):
        data = {"details": exc.message}
        response = Response(data, status=exc.status_code)

    return response