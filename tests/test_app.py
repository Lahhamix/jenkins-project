import unittest
import sys
import os

# Add parent directory (where app.py is) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World from Hadi Elham!")

if __name__ == "__main__":
    unittest.main()
