""" Describe the module ...
"""


def _private_placeholder_function():
    return 0


def placeholder_function(arg1, arg2):
    """Describe what the function does ...

    Args:
        arg1: Describe the meaning ...
        arg2: Describe the meaning ...

    Describe the side effects of the function ...

    Describe the preconditions, postconditions and invariants ...

    Provide additional information interesting to callers ...
    """
    return _private_placeholder_function()


class PlaceholderIF:
    """Describe what the interface defines ...
    """

    def method(self):
        """Like function ...
        """
        raise NotImplementedError


class _PrivatePlaceholderClass(PlaceholderIF):
    def __init__(self, arg):
        self.arg = arg

    def method(self):
        return self.arg


class PlaceholderClass(PlaceholderIF):
    """Like function ...
    """

    def __init__(self, arg):
        self.arg = arg

    def method(self):
        return self.arg
