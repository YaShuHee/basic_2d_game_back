class Entity(object):
    def __init__(self, x: int, y: int) -> None:
        """
        The basic object that will be on the 2D game map.
        An entity has an "x" and a "y" coordinates.
        """
        if not(isinstance(x, int) and isinstance(y, int)):
            raise TypeError("x and y must be int")
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def move_to(self, x: int, y: int):
        if not(isinstance(x, int) and isinstance(y, int)):
            raise TypeError("x and y must be int")
        self._x = x
        self._y = y
