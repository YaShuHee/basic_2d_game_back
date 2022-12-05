import unittest

from parameterized import parameterized

from src.entity import Entity


class TestEntity(unittest.TestCase):
    def test_entity_initialisation_works_with_int_x_and_y(self):
        expected_x = 0
        expected_y = 0
        entity = Entity(expected_x, expected_y)
        self.assertEqual(entity._x, expected_x)
        self.assertEqual(entity._y, expected_y)

    @staticmethod
    def load_x_y_initialisation_values_raising_type_error():
        return (
            ("0", "0"),
            ("0", 0),
            (0, "0"),
            (.0, .0),
            (0, .0),
            (.0, 0),
            ("0", .0),
            (.0, "0")
        )

    @parameterized.expand(load_x_y_initialisation_values_raising_type_error())
    def test_entity_initialisation_raises_type_error_with_bad_type_x_or_y(self, x, y):
        with self.assertRaises(TypeError):
            entity = Entity(x, y)

    @staticmethod
    def load_x_and_y_int_values():
        return (
            (0, 0),
            (42, 0),
            (0, 42),
            (442, 123),
            (500, 500),
            (-999, 0),
            (0, -30),
            (4, -12),
            (-54, 2),
            (-3, -7),
            (-77, -77)
        )
    
    @parameterized.expand(load_x_and_y_int_values())
    def test_if_x_and_y_attributes_return_accurate_values(self, expected_x, expected_y):
        entity = Entity(expected_x, expected_y)
        self.assertEqual(entity.x, expected_x)
        self.assertEqual(entity.y, expected_y)
