import unittest
from Rules import ConwayRules, StandardRules


class RulesTest(unittest.TestCase):
    def assertSurvival(self, rules, live_neighbors):
        map(lambda it: self.assertEqual(it in live_neighbors, rules.survives(it)), range(9))

    def assertBirth(self, rules, live_neighbors):
        map(lambda it: self.assertEqual(it in live_neighbors, rules.born(it)), range(9))

    def test_ConwayRules(self):
        self.assertEqual("R 23/3", ConwayRules.__str__())
        self.assertSurvival(ConwayRules, {2, 3})
        self.assertBirth(ConwayRules, {3})

    def test_Equality(self):
        rules1 = StandardRules(set(), set())
        rules2 = StandardRules(set(), set())
        self.assertEqual(rules1, rules2)

    def test_InEquality(self):
        rules1 = StandardRules(set(), set())
        rules2 = StandardRules({1}, set())
        self.assertNotEqual(rules1, rules2)


if __name__ == '__main__':
    unittest.main()
