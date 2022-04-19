class AuthenticationError(Exception):
    def __init__(self, message):
        super().__init__(message)


class DataError(Exception):
    def __init__(self, message):
        super().__init__(message)


class HTTPError(Exception):
    def __init__(self, message):
        super().__init__(message)


class UndefinedWarning(Warning):
    def __init__(self, message):
        super().__init__(message)


class UndefinedError(Exception):
    def __init__(self, message):
        super().__init__(message)