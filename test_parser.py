import unittest
from parser import parse_simplified_life1_05
from point import P
from universe import Universe


class ParserTest(unittest.TestCase):

    def parses(self, spec, cells):
        self.assertEqual(Universe(life=cells), parse_simplified_life1_05(spec))

    def test_parses(self):
        self.parses("", set())
        self.parses("*", {P(0, 0)})
        self.parses("**", {P(0, 0), P(1, 0)})
        self.parses("*\n*", {P(0, 0), P(0, 1)})
        self.parses("*.*", {P(0, 0), P(2, 0)})

    def test_invalid(self):
        with self.assertRaisesRegex(ValueError, "Unexpected character 'o' at line 1, column 1"):
            parse_simplified_life1_05("o")


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
