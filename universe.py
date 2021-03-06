from dataclasses import dataclass
from rules import ConwayRules, Rules
from point import Point


@dataclass(frozen=True)
class Universe:
    life: set
    rules: Rules = ConwayRules

    def __add__(self, other):
        return Universe(rules=self.rules, life=self.surviving_cells() | self.born_cells())

    def __eq__(self, other):
        return self.rules == other.rules and self.life == other.life

    def __str__(self):
        return "Universe{{{0}\n[{1}]}}".format(str(self.rules), ", ".join(map(str, self.life)))

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

    def cell_survives(self, cell):
        return self.rules.survives(self.cell_count_live_neighbors(cell))

    def cell_born(self, cell):
        return self.rules.born(self.cell_count_live_neighbors(cell))

    def cell_is_alive(self, cell):
        return cell in self.life

    def cell_is_dead(self, cell):
        return cell not in self.life

    def cell_dead_neighbors(self, cell: Point) -> set:
        return set(filter(self.cell_is_dead, cell.neighbors()))

    def cell_live_neighbors(self, cell: Point) -> set:
        return set(filter(self.cell_is_alive, cell.neighbors()))

    def cell_count_live_neighbors(self, cell):
        return len(self.cell_live_neighbors(cell))
