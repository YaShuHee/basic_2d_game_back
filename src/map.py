from src.entity import Entity


class Map(object):
    entities_counter = 0
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
        self._entities = {}

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def add_entity_at(self, x: int, y: int):
        # if x and y are not int, the Entity class will raise errors and messages
        entity = Entity(x, y)
        if not(1 <= x <= self._width):
            raise ValueError(f"x must be an int included in [1-{self._width}]")
        if not(1 <= y <= self.height):
            raise ValueError(f"y must be an int included in [1-{self._height}]")
        Map.entities_counter += 1
        entity_id = Map.entities_counter
        self._entities[entity_id] = entity
        return entity_id

