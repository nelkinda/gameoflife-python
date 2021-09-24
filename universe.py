from dataclasses import dataclass
from rules import ConwayRules, Rules
from point import Point


@dataclass(frozen=True)
class Universe:
    life: set
    _rules: Rules = ConwayRules

    def __add__(self, other: Point):
        return Universe(_rules=self._rules, life=self.cells_of_next_generation())

    def __eq__(self, other) -> bool:
        return self._rules == other._rules and self.life == other.life

    def __str__(self) -> str:
        return f"Universe{{{self._rules}\n[{', '.join(map(str, self.life))}]}}"

    def cells_of_next_generation(self) -> set:
        return self.surviving_cells() | self.born_cells()

    def surviving_cells(self) -> set:
        return set(filter(self.cell_survives, self.life))

    def born_cells(self) -> set:
        return set(filter(self.cell_born, self.dead_neighbors_of_living_cells()))

    def dead_neighbors_of_living_cells(self) -> set:
        return {
            dead_neighbor
            for dead_neighbors in map(self.cell_dead_neighbors, self.life)
            for dead_neighbor in dead_neighbors
        }

    def cell_survives(self, cell: Point) -> bool:
        return self._rules.survives(self.cell_count_live_neighbors(cell))

    def cell_born(self, cell: Point) -> bool:
        return self._rules.born(self.cell_count_live_neighbors(cell))

    def cell_is_alive(self, cell: Point) -> bool:
        '''Returns whether the given cell is alive.'''
        return cell in self.life

    def cell_is_dead(self, cell: Point) -> bool:
        return cell not in self.life

    def cell_dead_neighbors(self, cell: Point) -> set:
        return set(filter(self.cell_is_dead, cell.neighbors()))

    def cell_live_neighbors(self, cell: Point) -> set:
        return set(filter(self.cell_is_alive, cell.neighbors()))

    def cell_count_live_neighbors(self, cell: Point) -> int:
        return len(self.cell_live_neighbors(cell))
