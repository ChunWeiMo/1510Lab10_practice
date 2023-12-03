from unittest import TestCase
from unittest import main
from bacteria import colonize


class TestColonize(TestCase):
    def test_width_is_0(self):
        with self.assertRaises(ValueError):
            width = 0
            height = 2
            x_coordinate = 1
            y_coordinate = 1
            max_generation = 1
            colonize(width, height, x_coordinate, y_coordinate, max_generation)

    def test_height_is_0(self):
        with self.assertRaises(ValueError):
            width = 2
            height = 0
            x_coordinate = 1
            y_coordinate = 1
            max_generation = 1
            colonize(width, height, x_coordinate, y_coordinate, max_generation)

    def test_x_coordinate_less_than_0(self):
        with self.assertRaises(ValueError):
            width = 2
            height = 2
            x_coordinate = -1
            y_coordinate = 1
            max_generation = 1
            colonize(width, height, x_coordinate, y_coordinate, max_generation)

    def test_x_coordinate_greater_than_width(self):
        with self.assertRaises(ValueError):
            width = 2
            height = 2
            x_coordinate = 3
            y_coordinate = 0
            max_generation = 1
            colonize(width, height, x_coordinate, y_coordinate, max_generation)

    def test_y_coordinate_less_than_0(self):
        with self.assertRaises(ValueError):
            width = 2
            height = 2
            x_coordinate = 1
            y_coordinate = -1
            max_generation = 1
            colonize(width, height, x_coordinate, y_coordinate, max_generation)

    def test_y_coordinate_greater_than_height(self):
        with self.assertRaises(ValueError):
            width = 2
            height = 2
            x_coordinate = 1
            y_coordinate = 3
            max_generation = 1
            colonize(width, height, x_coordinate, y_coordinate, max_generation)

    def test_max_generation_less_than_0(self):
        with self.assertRaises(ValueError):
            width = 2
            height = 2
            x_coordinate = 1
            y_coordinate = 1
            max_generation = -1
            colonize(width, height, x_coordinate, y_coordinate, max_generation)

    def test_width_is_1(self):
        width = 1
        height = 3
        x_coordinate = 0
        y_coordinate = 1
        max_generation = 1
        colonize(width, height, x_coordinate, y_coordinate, max_generation)
        expected = {(0, 0): True, (0, 1): True, (0, 2): True}
        self.assertEqual(expected, colonize(
            width, height, x_coordinate, y_coordinate, max_generation))

    def test_height_is_1(self):
        width = 3
        height = 1
        x_coordinate = 1
        y_coordinate = 0
        max_generation = 1
        colonize(width, height, x_coordinate, y_coordinate, max_generation)
        expected = {(0, 0): True, (1, 0): True, (2, 0): True}
        self.assertEqual(expected, colonize(
            width, height, x_coordinate, y_coordinate, max_generation))

    def test_x_coordinate_on_right_boundary(self):
        width = 3
        height = 3
        x_coordinate = 2
        y_coordinate = 1
        max_generation = 1
        colonize(width, height, x_coordinate, y_coordinate, max_generation)
        expected = {(0, 0): False, (1, 0): False, (2, 0): True, (0, 1): False,
                    (1, 1): True, (2, 1): True, (0, 2): False, (1, 2): False, (2, 2): True}
        self.assertEqual(expected, colonize(
            width, height, x_coordinate, y_coordinate, max_generation))
        
    def test_y_coordinate_on_down_boundary(self):
        width = 3
        height = 3
        x_coordinate = 1
        y_coordinate = 2
        max_generation = 1
        colonize(width, height, x_coordinate, y_coordinate, max_generation)
        expected = {(0, 0): False, (1, 0): False, (2, 0): False, (0, 1): False,
                    (1, 1): True, (2, 1): False, (0, 2): True, (1, 2): True, (2, 2): True}
        self.assertEqual(expected, colonize(
            width, height, x_coordinate, y_coordinate, max_generation))
    
    def test_zero_generation(self):
        width = 3
        height = 3
        x_coordinate = 1
        y_coordinate = 1
        max_generation = 0
        colonize(width, height, x_coordinate, y_coordinate, max_generation)
        expected = {(0, 0): False, (1, 0): False, (2, 0): False, (0, 1): False,
                    (1, 1): True, (2, 1): False, (0, 2): False, (1, 2): False, (2, 2): False}
        self.assertEqual(expected, colonize(
            width, height, x_coordinate, y_coordinate, max_generation))
        
    def test_normal_case(self):
        width = 4
        height = 5
        x_coordinate = 2
        y_coordinate = 3
        max_generation = 1
        colonize(width, height, x_coordinate, y_coordinate, max_generation)
        expected = {(0, 0): False, (1, 0): False, (2, 0): False, (3, 0): False, (0, 1): False, (1, 1): False, (2, 1): False, (3, 1): False, (0, 2): False, (1, 2): False, (2, 2): True, (3, 2): False, (0, 3): False, (1, 3): True, (2, 3): True, (3, 3): True, (0, 4): False, (1, 4): False, (2, 4): True, (3, 4): False}
        self.assertEqual(expected, colonize(
            width, height, x_coordinate, y_coordinate, max_generation))
        
        
if __name__ == "__main__":
    main()
