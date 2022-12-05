class Map(object):
    def __init__(self, width: int, height: int):
        """
        The class used to control the map and the moving entities.
        """
        if not(isinstance(width, int) and isinstance(height, int)):
            raise TypeError("width and height must be int")
        if not(width > 0 and height > 0):
            raise ValueError("width and height must be greater than or equal to 1")
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
