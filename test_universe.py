import unittest
from universe import Universe
from rules import StandardRules
from point import P


class UniverseTest(unittest.TestCase):
    def test_equality(self):
        u1 = Universe(rules=StandardRules(set(), set()), life=set())
        u2 = Universe(rules=StandardRules(set(), set()), life=set())
        self.assertEqual(u1, u2)

    def test_inEquality(self):
        u1 = Universe(rules=StandardRules(set(), {1}), life=set())
        u2 = Universe(rules=StandardRules({1}, set()), life=set())
        self.assertNotEqual(u1, u2)

    def test_str(self):
        self.assertEqual("Universe{R 23/3\n[P(0, 1)]}", Universe(life={P(0, 1)}).__str__())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
