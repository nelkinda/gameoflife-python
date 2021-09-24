from dataclasses import dataclass
from abc import ABC, abstractmethod


class Rules(ABC):
    @abstractmethod
    def survives(self, live_neighbors) -> bool:  # pragma: no cover
        pass

    @abstractmethod
    def born(self, live_neighbors) -> bool:  # pragma: no cover
        pass


def set_str(s: set) -> str:
    return "".join(str(i) for i in s)


@dataclass(frozen=True)
class StandardRules(Rules):
    liveNeighborsForSurvival: set
    liveNeighborsForBirth: set

    def survives(self, live_neighbors) -> bool:
        return live_neighbors in self.liveNeighborsForSurvival

    def born(self, live_neighbors) -> bool:
        return live_neighbors in self.liveNeighborsForBirth

    def __str__(self):
        return "R {0}/{1}".format(
            set_str(self.liveNeighborsForSurvival),
            set_str(self.liveNeighborsForBirth),
        )


ConwayRules = StandardRules({2, 3}, {3})
