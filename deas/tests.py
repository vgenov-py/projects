import unittest
import main as subject
from main import data

class test_main(unittest.TestCase):
    def test_get_title(self):
        self.assertEqual(subject.get_title(data, "Pública"), 3822)
        self.assertEqual(subject.get_title(data, "Privada"), 3818)
        
    def test_get_inside_M30(self):
        self.assertEqual(subject.get_inside_M30(data), 1667)

if __name__ == '__main__':
    unittest.main()