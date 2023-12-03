import io
from unittest import TestCase
from unittest.mock import patch
from unittest import main
from bacteria import print_surface


class TestPrintSurface(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_1_grid(self, mock_output):
        surface = {(0, 0): False}
        print_surface(surface)
        expected_output = '0\n'
        self.assertEqual(expected_output, mock_output.getvalue())
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_row(self, mock_output):
        surface = {(0, 0): True, (1, 0): False, (2, 0): False, (3, 0): False}
        print_surface(surface)
        expected_output = '*000\n'
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_column(self, mock_output):
        surface = {(0, 0): False, (0, 1): True, (0, 2): False}
        print_surface(surface)
        expected_output = '0\n*\n0\n'
        self.assertEqual(expected_output, mock_output.getvalue())
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_all_False(self, mock_output):
        surface = {(0, 0): False, (1, 0): False, (2, 0): False,
                   (0, 1): False, (1, 1): False, (2, 1): False}
        print_surface(surface)
        expected_output = '000\n000\n'
        self.assertEqual(expected_output, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_all_True(self, mock_output):
        surface = {(0, 0): True, (1, 0): True, (0, 1): True, (1, 1): True}
        print_surface(surface)
        expected_output = '**\n**\n'
        self.assertEqual(expected_output, mock_output.getvalue())
        
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_normal_case(self, mock_output):
        surface = {(0, 0): False, (1, 0): False, (2, 0): False, (0, 1): False, (1, 1): True, (2, 1): False, (0, 2): True, (1, 2): True, (2, 2): True, (0, 3): False, (1, 3): True, (2, 3): False}
        print_surface(surface)
        expected_output = '000\n0*0\n***\n0*0\n'
        self.assertEqual(expected_output, mock_output.getvalue())
    
    

if __name__ == "__main__":
    main()
