class UserException(Exception):
    pass


class PathErrorException(UserException):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return f'Path: <{self.path}> not exists'
    

class InputErrorException(UserException):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return f'Parameter {self.param} should be string, bytes, os.PathLike or integer, not builtin_function_or_method! \
            May be you must add "()"'
    

class ZeroSideException(UserException):
    def __str__(self):
        return f'The side must be not ZERO!'
    

class NegativeValueSideException(UserException):
    def __init__(self, side, value):
        self.side = side
        self.val = value

    def __str__(self):
        return f'Incorrect value {self.val} for {self.side}. Value must be positive!'