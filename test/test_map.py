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
