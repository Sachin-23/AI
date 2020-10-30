class InvalidMove(Exception):
    """Base class for exceptions in this module."""
    pass

try:
    raise InvalidMove("InvalidAction")
except InvalidMove as e:
    print(Action)
