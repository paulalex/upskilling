"""Module for defining custom exceptions and classes and
functions related to exception handling.
"""
from enum import Enum
import json


class ApiBaseException(Exception):
    """Base exception class.

    Args:
        reason (str): The reason type of this exception, can be client_error or server_error.
        exception_type (str): Document describing this exception type.
        title (str): The title of the exception message. This value is passed to the parent
        Exception class as the 'message' argument.
        detail (str): Error message detail to be returned to the API consumer.
        status (str): The http response status code of this exception.
        errors: (list[str]): A list of error validation messages to be passed to the API consumer.
    """

    def __init__(self, reason, exception_type, title, detail, status, errors):
        self._reason = reason
        self._exception_type = exception_type
        self._title = title
        self._detail = detail
        self._status = status
        self._errors = errors
        super().__init__(self.exception_message_as_json())

    def exception_message_as_json(self):
        """Parse exceptions into the format required for returning back to clients calling the API.
        """
        json_error = {
            "reason": self._reason,
            "type": self._exception_type,
            "title": self._title,
            "detail": self._detail,
            "status": self._status,
            "errors": self._errors,
        }

        return json.dumps(json_error)


class RequestValidationException(ApiBaseException):
    """Exception to be triggered when request validation fails for any methods
    dealing with incoming requests.
    """

    EXCEPTION_TYPE_DESCRIPTOR = "about:blank"

    def __init__(self, detail, errors):
        """
        Args:
            detail (str): Error message detail to be returned to the API consumer.
            errors: (list[str]): A list of error validation messages to be passed
            to the API consumer.
        """
        super().__init__(
            ClientExceptionConstants.REASON.value,
            RequestValidationException.EXCEPTION_TYPE_DESCRIPTOR,
            ClientExceptionConstants.REQUEST_PARAM_VALIDATION_TITLE.value,
            detail,
            ClientExceptionConstants.HTTP_STATUS_400.value,
            errors,
        )

class MprnNotFoundException(ApiBaseException):
    """Exception to be triggered when an MPRN is not found.
    """

    EXCEPTION_TYPE_DESCRIPTOR = "about:blank"

    def __init__(self, detail, errors):
        """
        Args:
            detail (str): Error message detail to be returned to the API consumer.
            errors: (list[str]): A list of error validation messages to be passed
            to the API consumer.
        """
        super().__init__(
            ClientExceptionConstants.REASON.value,
            MprnNotFoundException.EXCEPTION_TYPE_DESCRIPTOR,
            ClientExceptionConstants.NOT_FOUND_TITLE.value,
            detail,
            ClientExceptionConstants.HTTP_STATUS_404.value,
            errors,
        )

class ServerException(ApiBaseException):
    """Custom Exception used to handle 500 internal server errors
    and any non customer exceptions that might be thrown.
    """

    EXCEPTION_TYPE_DESCRIPTOR = "about:blank"

    """Exception to be triggered when request validation fails for any methods#
    dealing with incoming requests.
    """

    def __init__(self, detail, errors):
        """
        Args:
            detail (str): Error message detail to be returned to the API consumer.
            errors: (list[str]): A list of error validation messages
            to be passed to the API consumer.
        """
        super().__init__(
            ServerExceptionConstants.REASON.value,
            self.EXCEPTION_TYPE_DESCRIPTOR,
            ServerExceptionConstants.RESPONSE_ERROR_TITLE.value,
            detail,
            ServerExceptionConstants.HTTP_STATUS_500.value,
            errors,
        )


class ClientExceptionConstants(Enum):
    """Enum based constant management when dealing with client based (4xx) errors.
    """

    REASON = "client_error"
    HTTP_STATUS_400 = 400
    HTTP_STATUS_404 = 404
    REQUEST_PARAM_VALIDATION_TITLE = "Request parameter validation error"
    NOT_FOUND_TITLE = "Requested resource was not found"

    def __str__(self):
        return str(self.value)


class ServerExceptionConstants(Enum):
    """Enum based constant management used when dealing with server based (5xx) errors.

    RESPONSE_ERROR_TITLE is handled by 500-response template to ensure
    no implementation details are leaked to clients.
    """

    REASON = "server_error"
    HTTP_STATUS_500 = 500
    RESPONSE_ERROR_TITLE = "Internal Server Error"

    def __str__(self):
        return str(self.value)
