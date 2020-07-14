from dataclasses import dataclass
from rules import ConwayRules
import point
import rules


@dataclass(frozen=True)
class Universe:
    life: set
    rules: rules = ConwayRules

    def __add__(self, other):
        return Universe(rules=self.rules, life=self.surviving_cells() | self.born_cells())

    def __eq__(self, other):
        return self.rules == other.rules and self.life == other.life

    def __str__(self):
        return "Universe{{{0}\n[{1}]}}".format(str(self.rules), ", ".join(map(lambda it: str(it), self.life)))

    def surviving_cells(self) -> set:
        return set(filter(lambda cell: self.cell_survives(cell), self.life))

    def dead_neighbors_of_living_cells(self) -> set:
        return set([
            dead_neighbor
            for dead_neighbors in map(lambda live_cell: self.cell_dead_neighbors(live_cell), self.life)
            for dead_neighbor in dead_neighbors
        ])

    def born_cells(self) -> set:
        return set(filter(lambda cell: self.cell_born(cell), self.dead_neighbors_of_living_cells()))

    def cell_is_alive(self, cell):
        return cell in self.life

    def cell_survives(self, cell):
        return self.rules.survives(self.cell_count_live_neighbors(cell))

    def cell_born(self, cell):
        return self.rules.born(self.cell_count_live_neighbors(cell))

    def cell_dead_neighbors(self, cell: point) -> set:
        return set(filter(lambda it: not self.cell_is_alive(it), cell.neighbors()))

    def cell_live_neighbors(self, cell: point) -> set:
        return set(filter(lambda it: self.cell_is_alive(it), cell.neighbors()))

    def cell_count_live_neighbors(self, cell):
        return len(self.cell_live_neighbors(cell))
