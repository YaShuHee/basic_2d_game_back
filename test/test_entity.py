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
            ("0", "0"), # str str
            ("0", 0),   # str int
            (0, "0"),   # int str
            (.0, .0),   # flt flt
            (0, .0),    # int flt
            (.0, 0),    # flt int
            ("0", .0),  # str flt
            (.0, "0"),  # flt str
        )

    @parameterized.expand(load_x_y_initialisation_values_raising_type_error())
    def test_entity_initialisation_raises_type_error_when_passed_x_or_y_are_from_wrong_type(self, x, y):
        with self.assertRaises(TypeError):
            entity = Entity(x, y)

    @staticmethod
    def load_x_and_y_int_values():
        return (
            (0, 0),     # 0 0
            (42, 0),    # + 0
            (0, 42),    # 0 +
            (442, 123), # + +
            (500, 500), # +=+
            (-999, 0),  # - 0
            (0, -30),   # 0 -
            (4, -12),   # + -
            (-54, 2),   # - +
            (-3, -7),   # - -
            (-77, -77), # -=-
        )
    
    @parameterized.expand(load_x_and_y_int_values())
    def test_x_and_y_attributes_return_accurate_values(self, expected_x, expected_y):
        entity = Entity(expected_x, expected_y)
        self.assertEqual(entity.x, expected_x)
        self.assertEqual(entity.y, expected_y)

    @staticmethod
    def load_start_and_end_x_and_y_int_values():
        return (
            (0, 0, 0, 0),       # 0 0 0 0
            (1, 0, 0, 0),       # + 0 0 0
            (0, 1, 0, 0),       # 0 + 0 0
            (0, 0, 1, 0),       # 0 0 + 0
            (0, 0, 0, 1),       # 0 0 0 +
            (1, 2, 0, 0),       # + + 0 0
            (3, 0, 4, 0),       # + 0 + 0
            (1, 0, 0, 1),       # + 0 0 +
            (0, 3, 4, 0),       # 0 + + 0
            (0, 5, 0, 7),       # 0 + 0 +
            (0, 0, 1, 2),       # 0 0 + +
            (1, 2, 3, 0),       # + + + 0
            (2, 2, 0, 4),       # + + 0 +
            (2, 0, 1, 4),       # + 0 + +
            (0, 3, 1, 4),       # 0 + + +
            (5, 2, 4, 3),       # + + + +
            (-1, 0, 0, 0),      # - 0 0 0
            (0, -1, 0, 0),      # 0 - 0 0
            (0, 0, -1, 0),      # 0 0 - 0
            (0, 0, 0, -1),      # 0 0 0 -
            (-1, -1, 0, 0),     # - - 0 0
            (-1, 0, -1, 0),     # - 0 - 0
            (-1, 0, 0, -1),     # - 0 0 -
            (0, -1, -1, 0),     # 0 - - 0
            (0, -1, 0, -1),     # 0 - 0 -
            (0, 0, -1, -1),     # 0 0 - -
            (-2, -5, -3, 0),    # - - - 0
            (-2, -2, 0, -4),    # - - 0 -
            (-2, 0, -7, -4),    # - 0 - -
            (0, -6, -1, -4),    # 0 - - -
            (-7, -2, -8, -3),   # - - - -
            (-5, 3, 2, 4),      # - + + +
            (8, -7, 1, 9),      # + - + +
            (2, 4, -4, 5),      # + + - +
            (3, 6, 7, -2),      # + + + -
            (-6, -1, 5, 8),     # - - + +
            (-3, 2, -4, 5),     # - + - +
            (-8, 1, 9, -7),     # - + + -
            (4, -3, -2, 5),     # + - - +
            (1, 2, -3, -4),     # + - + -
            (2, 5, -1, -7),     # + + - -
            (-3, -4, -4, 2),    # - - - +
            (-5, -7, 8, -2),    # - - + -
            (-1, 2, -1, -6),    # - + - -
            (8, -9, -1, -2),    # + - - -
        )

    @parameterized.expand(load_start_and_end_x_and_y_int_values())
    def test_move_to_method(self, start_x, start_y, end_x, end_y):
        entity = Entity(start_x, start_y)
        entity.move_to(end_x, end_y)
        self.assertEqual(entity.x, end_x)
        self.assertEqual(entity.y, end_y)

    @staticmethod
    def load_start_and_end_x_and_y_values_raising_type_error():
        return (
            (0, 0, "0", "0"),   # str str
            (0, 0, "0", 0),     # str int
            (0, 0, 0, "0"),     # int str
            (0, 0, .0, .0),     # flt flt
            (0, 0, 0, .0),      # int flt
            (0, 0, .0, 0),      # flt int
            (0, 0, "0", .0),    # str flt
            (0, 0, .0, "0"),    # flt str
        )

    @parameterized.expand(load_start_and_end_x_and_y_values_raising_type_error())
    def test_move_to_method_raises_type_error_when_passed_x_or_y_are_from_wrong_type(self, start_x, start_y, end_x, end_y):
        entity = Entity(start_x, start_y)
        with self.assertRaises(TypeError):
            entity.move_to(end_x, end_y)
