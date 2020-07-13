class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "P({0}, {1})".format(str(self.x), str(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return (self.x << 16) ^ self.y

    def neighbors(self) -> set:
        return set(map(lambda p: self + p, neighbors))


# noinspection PyPep8Naming
def P(x, y) -> Point:
    return Point(x, y)


neighbors = {P(-1, -1), P(0, -1), P(1, -1), P(-1, 0), P(1, 0), P(-1, 1), P(0, 1), P(1, 1)}
