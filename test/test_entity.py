import unittest

from parameterized import parameterized

from src.entity import Entity


class TestEntity(unittest.TestCase):
    def test_entity_initiatisation_works_with_int_x_and_y(self):
        entity = Entity(0, 0)
        self.assertEqual(entity._x, 0)
        self.assertEqual(entity._y, 0)

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
