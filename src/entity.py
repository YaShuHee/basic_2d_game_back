class Entity(object):
    def __init__(self, x, y) -> None:
        """
        The basic object that will be on the 2D game map.
        An entity has an "x" and a "y" coordinates.
        """
        if not(isinstance(x, int) and isinstance(y, int)):
            raise(TypeError)
        self._x = x
        self._y = y
