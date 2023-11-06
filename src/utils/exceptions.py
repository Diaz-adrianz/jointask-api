from typing import Union


class BadRequest400(Exception):
    def __init__(self, message: str = "Bad Request"):
        self.name = message


class ServerError500(Exception):
    def __init__(self, message: str = "Internal Server Error"):
        self.name = message


class Forbidden403(Exception):
    def __init__(self, message: str = "Forbidden"):
        self.name = message


class NotFound404(Exception):
    def __init__(self, message: str = None, id: Union[str, int, None] = None):
        if message:
            self.name = message
        elif id:
            self.name = f"Data with id {id} not found"
        else:
            self.name = "Data Not Found"
