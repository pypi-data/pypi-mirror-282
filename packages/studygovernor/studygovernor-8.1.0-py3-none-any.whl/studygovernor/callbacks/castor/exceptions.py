import requests


class CastorClientError(Exception):
    pass


class ConflictingDataError(CastorClientError, ValueError):
    pass


class LoginError(CastorClientError):
    pass


class ResponseError(CastorClientError):
    def __init__(self, response: requests.Response, message: str = None):
        self.response = response
        self.message = message

    @property
    def status_code(self) -> int:
        return self.response.status_code
