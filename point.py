from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    _x: int
    _y: int

    def __str__(self):
        return f"P({self._x}, {self._y})"

    def __add__(self, other):
        return P(self._x + other._x, self._y + other._y)

    def neighbors(self) -> set:
        return set(map(lambda p: self + p, neighbors))


# noinspection PyPep8Naming
def P(x: int, y: int) -> Point:  # NOSONAR P(x, y) is our DSL.
    return Point(x, y)


neighbors = {P(-1, -1), P(0, -1), P(1, -1), P(-1, 0), P(1, 0), P(-1, 1), P(0, 1), P(1, 1)}
