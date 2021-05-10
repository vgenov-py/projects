import unittest
from models import Dea 

sbj = Dea(443120, 4475002)

class dea_funcs(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(sbj.distance(443123, 4475002), 0)

if __name__ == '__main__':
    unittest.main()