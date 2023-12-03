import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from bacteria import spread_like_bacteria


class TestSpreadLikeBacteria(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_surface_not_dictionary(self, mock_output):
        surface = "surface"
        coordinate = (5, 5)
        max_generation = 1
        spread_like_bacteria(surface, coordinate, max_generation)
        expected_message = 'Surface must be a dictionary.\n'
        self.assertEqual(expected_message, mock_output.getvalue())
        
        
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_coordinate_outside_surface(self, mock_output):
        surface = {(0, 0): False, (1, 0): False, (2, 0): False, (0, 1): False,
                   (1, 1): False, (2, 1): False, (0, 2): False, (1, 2): False, (2, 2): False}
        coordinate = (5, 5)
        max_generation = 1
        spread_like_bacteria(surface, coordinate, max_generation)
        expected_message = 'A bacteria is outside boundary.\n'
        self.assertEqual(expected_message, mock_output.getvalue())
    
    def test_coordinate_inside_surface(self):
        surface = {(0, 0): False, (1, 0): False, (2, 0): False, (0, 1): False,
                   (1, 1): False, (2, 1): False, (0, 2): False, (1, 2): False, (2, 2): False}
        coordinate = (1, 1)
        max_generation = 1
        spread_like_bacteria(surface, coordinate, max_generation)
        expected_surface = {(0, 0): False, (1, 0): True, (2, 0): False, (0, 1): True, (
            1, 1): True, (2, 1): True, (0, 2): False, (1, 2): True, (2, 2): False}
        self.assertEqual(expected_surface, surface)
    
    def test_max_generation_minus(self):
        surface = {(0, 0): False, (1, 0): False, (2, 0): False, (0, 1): False,
                   (1, 1): False, (2, 1): False, (0, 2): False, (1, 2): False, (2, 2): False}
        coordinate = (1, 1)
        max_generation = -1
        spread_like_bacteria(surface, coordinate, max_generation)
        expected_after_surface = {(0, 0): False, (1, 0): False, (2, 0): False, (0, 1): False, (
            1, 1): False, (2, 1): False, (0, 2): False, (1, 2): False, (2, 2): False}
        self.assertEqual(expected_after_surface, surface)
    
    def test_max_generation_0(self):
        surface = {(0, 0): False, (1, 0): False, (2, 0): False, (0, 1): False,
                   (1, 1): False, (2, 1): False, (0, 2): False, (1, 2): False, (2, 2): False}
        coordinate = (1, 1)
        max_generation = 0
        spread_like_bacteria(surface, coordinate, max_generation)
        expected_after_surface = {(0, 0): False, (1, 0): False, (2, 0): False, (0, 1): False, (
            1, 1): True, (2, 1): False, (0, 2): False, (1, 2): False, (2, 2): False}
        self.assertEqual(expected_after_surface, surface)
    
    def test_max_generation_greater_than_0(self):
        surface = {(0, 0): False, (1, 0): False, (2, 0): False, (0, 1): False,
                   (1, 1): False, (2, 1): False, (0, 2): False, (1, 2): False, (2, 2): False}
        coordinate = (1, 1)
        max_generation = 2
        spread_like_bacteria(surface, coordinate, max_generation)
        expected_after_surface = {(0, 0): True, (1, 0): True, (2, 0): True, (0, 1): True, (
            1, 1): True, (2, 1): True, (0, 2): True, (1, 2): True, (2, 2): True}
        self.assertEqual(expected_after_surface, surface)

if __name__ == "__main__":
    main()
