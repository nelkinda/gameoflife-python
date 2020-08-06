from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __str__(self):
        return "P({0}, {1})".format(str(self.x), str(self.y))

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def neighbors(self) -> set:
        return set(map(lambda p: self + p, neighbors))


# noinspection PyPep8Naming
def P(x, y) -> Point:  # NOSONAR P(x, y) is our DSL.
    return Point(x, y)


neighbors = {P(-1, -1), P(0, -1), P(1, -1), P(-1, 0), P(1, 0), P(-1, 1), P(0, 1), P(1, 1)}
