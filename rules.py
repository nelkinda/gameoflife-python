from dataclasses import dataclass
from abc import ABC, abstractmethod


class Rules(ABC):
    @abstractmethod
    def survives(self, live_neighbors: int) -> bool:  # pragma: no cover
        pass

    @abstractmethod
    def born(self, live_neighbors: int) -> bool:  # pragma: no cover
        pass


def set_str(s: set) -> str:
    return "".join(str(i) for i in s)


@dataclass(frozen=True)
class StandardRules(Rules):
    _liveNeighborsForSurvival: set
    _liveNeighborsForBirth: set

    def survives(self, live_neighbors: int) -> bool:
        return live_neighbors in self._liveNeighborsForSurvival

    def born(self, live_neighbors: int) -> bool:
        return live_neighbors in self._liveNeighborsForBirth

    def __str__(self) -> str:
        return f"R {set_str(self._liveNeighborsForSurvival)}/{set_str(self._liveNeighborsForBirth)}"


ConwayRules = StandardRules({2, 3}, {3})
