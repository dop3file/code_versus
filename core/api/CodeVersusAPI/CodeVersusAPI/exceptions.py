from rest_framework.views import exception_handler
from rest_framework.response import Response


class CustomBaseException(Exception):
    ...


class ServiceException(CustomBaseException):
    ...


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if issubclass(type(exc), CustomBaseException):
        data = {"error": "error"}
        status_code = 400
        response = Response(data, status=status_code)

    return response