import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from bacteria_not_recursive import spread_breadth_first

class TestSpreadLikeBacteria(TestCase):
    def test_1_grid(self):
        surface = {(0, 0): False}
        coordinate = (0, 0)
        max_generation = 1
        spread_breadth_first(surface, coordinate, max_generation)
        expected_surface = {(0, 0): True}
        self.assertEqual(expected_surface, surface)

    def test_row(self):
        surface = {(0, 0): False, (1, 0): False, (2, 0): False}
        coordinate = (0, 0)
        max_generation = 1
        spread_breadth_first(surface, coordinate, max_generation)
        expected_surface = {(0, 0): True, (1, 0): True, (2, 0): False}
        self.assertEqual(expected_surface, surface)
        
    def test_column(self):
        surface = {(0, 0): False, (0, 1): False, (0, 2): False, (0, 3): False}
        coordinate = (0, 1)
        max_generation = 2
        spread_breadth_first(surface, coordinate, max_generation)
        expected_surface = {(0, 0): True, (0, 1): True,
                            (0, 2): True, (0, 3): True}
        self.assertEqual(expected_surface, surface)

    def test_normal_case(self):
        surface = {(0, 0): False, (1, 0): False, (2, 0): False, (3, 0): False, (4, 0): False, (0, 1): False, (1, 1): False, (2, 1): False, (3, 1): False, (4, 1): False, (0, 2): False, (1, 2): False, (2, 2): False, (3, 2): False, (4, 2): False, (0, 3): False, (1, 3): False, (2, 3): False, (3, 3): False, (4, 3): False, (0, 4): False, (1, 4): False, (2, 4): False, (3, 4): False, (4, 4): False}
        coordinate = (2, 2)
        max_generation = 2
        spread_breadth_first(surface, coordinate, max_generation)
        expected_surface = {(0, 0): False, (1, 0): False, (2, 0): True, (3, 0): False, (4, 0): False, (0, 1): False, (1, 1): True, (2, 1): True, (3, 1): True, (4, 1): False, (0, 2): True, (1, 2): True, (
            2, 2): True, (3, 2): True, (4, 2): True, (0, 3): False, (1, 3): True, (2, 3): True, (3, 3): True, (4, 3): False, (0, 4): False, (1, 4): False, (2, 4): True, (3, 4): False, (4, 4): False}
        self.assertEqual(expected_surface, surface)

if __name__ == "__main__":
    main()
