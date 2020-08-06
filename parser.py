from universe import Universe
from point import P


def parse_simplified_life1_05(life1_05) -> Universe:
    cells = set()
    line = 1
    column = 1

    for c in life1_05:
        if c == '\n':
            column = 0
            line += 1
        elif c == '*':
            cells.add(P(column - 1, line - 1))
        elif c == '.':
            # Skip '.', it's a dead cell.
            pass
        else:
            raise ValueError(
                "Unexpected character \'{0}\' at line {1}, column {2}".format(str(c), str(line), str(column)))
        column += 1

    return Universe(life=cells)
