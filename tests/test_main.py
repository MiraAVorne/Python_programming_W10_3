import unittest
from unittest.mock import patch, mock_open
import io
import sys
import importlib

# Simulated contents of A10_D10.txt
sample_data = "1000\n221\n392\n621\n47\n448\n163\n120\n197\n781\n"
expected_asc = [47, 120, 163, 197, 221, 392, 448, 621, 781, 1000]
expected_desc = list(reversed(expected_asc))

class TestMainBubbleSort(unittest.TestCase):

    @patch("builtins.input", return_value="A10_D10.txt")
    @patch("builtins.open", new_callable=mock_open, read_data=sample_data)
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main_manual_input(self, mock_stdout, mock_file, mock_input):
        import main
        importlib.reload(main)
        main.main()
        output = mock_stdout.getvalue()
        for val in expected_asc + expected_desc:
            self.assertIn(str(val), output)

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.open", new_callable=mock_open, read_data=sample_data)
    def test_main_cli_argument(self, mock_file, mock_stdout):
        with patch.object(sys, "argv", ["main.py", "A10_D10.txt"]):
            import main
            importlib.reload(main)
            main.main()
            output = mock_stdout.getvalue()
            for val in expected_asc + expected_desc:
                self.assertIn(str(val), output)

if __name__ == "__main__":
    unittest.main()
