import unittest
from Point import P


class PointTest(unittest.TestCase):
    def test_str(self):
        self.assertEqual("P(0, 1)", P(0, 1).__str__())

    def test_equalPoints(self):
        p1 = P(0, 0)
        p2 = P(0, 0)
        self.assertEqual(p1, p2)

    def test_notEqualPoints(self):
        p1 = P(0, 0)
        p2 = P(0, 1)
        self.assertNotEqual(p1, p2)

    def test_plus(self):
        self.assertEqual(P(3, 30), P(2, 20) + P(1, 10))

    def test_neighbors(self):
        self.assertEqual({P(4, 4), P(4, 5), P(4, 6), P(5, 4), P(5, 6), P(6, 4), P(6, 5), P(6, 6)}, P(5, 5).neighbors())


if __name__ == '__main__':
    unittest.main()
