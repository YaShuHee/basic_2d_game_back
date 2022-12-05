import unittest

from parameterized import parameterized

from src.entity import Entity
from src.map import Map


class TestMap(unittest.TestCase):
    def test_map_initialisation_with_int_width_and_height(self):
        expected_width = 1
        expected_height = 1
        map = Map(expected_width, expected_height)
        self.assertEqual(map._width, expected_width)
        self.assertEqual(map._height, expected_height)

    def load_map_width_and_height_from_wrong_type():
        return (
            ("2", "2"),
            ("2", 2),
            (2, "2"),
            (2.1, 2),
            (2, 2.1),
            ("2", 2.1),
            (2.1, "2"),
        )

    @parameterized.expand(load_map_width_and_height_from_wrong_type())
    def test_map_initialisation_raises_type_error_when_passed_width_or_height_are_from_wrong_type(self, width, height):
        with self.assertRaises(TypeError):
            map = Map(width, height)

    @staticmethod
    def load_map_width_and_height_lower_than_one():
        return (
            (0, 0),
            (2, 0),
            (0, 2),
            (-1, 2),
            (2, -1)
        )

    @parameterized.expand(load_map_width_and_height_lower_than_one)
    def test_map_initialisation_raises_value_error_when_passed_width_or_height_is_lower_than_one(self, width, height):
        with self.assertRaises(ValueError):
            map = Map(width, height)

    @staticmethod
    def load_width_and_height_int_values():
        return (
            (1, 1),
            (1, 100),
            (100, 1),
            (20, 20),
        )

    @parameterized.expand(load_width_and_height_int_values())
    def test_width_and_height_attributes_return_accurate_values(self, expected_width, expected_height):
        map = Map(expected_width, expected_height)
        self.assertEqual(map.width, expected_width)
        self.assertEqual(map.height, expected_height)

    @staticmethod
    def load_width_height_x_y_int_values():
        return (
            (1, 1, 1, 1),
            (10, 10, 1, 1),
            (10, 10, 4, 2),
            (10, 10, 10, 10),
        )

    @parameterized.expand(load_width_height_x_y_int_values)
    def test_add_entity_at_with_accurate_int_values(self, width, height, x, y):
        map = Map(width, height)
        entity_id = map.add_entity_at(x, y)
        self.assertEqual(map._entities[entity_id].x, x)
        self.assertEqual(map._entities[entity_id].y, y)

    @staticmethod
    def load_x_y_from_wrong_type():
        return (
            ("1", "1"),
            (1, "1"),
            ("1", 1),
            (1., 1.),
            (1., 1),
            (1, 1.),
            ("1", 1.),
            (1., "1"),
        )

    @parameterized.expand(load_x_y_from_wrong_type())
    def test_add_entity_at_when_passed_x_or_y_are_from_wrong_type(self, x, y):
        width = 1
        height = 1
        map = Map(width, height)
        with self.assertRaises(TypeError):
            map.add_entity_at(x, y)

    @staticmethod
    def load_width_height_x_y_not_on_the_map():
        return (
            (1, 1, 2, 2),
            (1, 1, -1, -1),
            (1, 99, 2, 100),
        )

    @parameterized.expand(load_width_height_x_y_not_on_the_map())
    def test_add_entity_at_when_passed_x_or_y_are_not_on_map(self, width, height, x, y):
        map = Map(width, height)
        with self.assertRaises(ValueError):
            map.add_entity_at(x, y)
