from dataclasses import dataclass
import abc


class Rules(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def survives(self, live_neighbors) -> bool:
        pass

    @abc.abstractmethod
    def born(self, live_neighbors) -> bool:
        pass


@dataclass(frozen=True)
class StandardRules(Rules):
    liveNeighborsForSurvival: set
    liveNeighborsForBirth: set

    def survives(self, live_neighbors) -> bool:
        return live_neighbors in self.liveNeighborsForSurvival

    def born(self, live_neighbors) -> bool:
        return live_neighbors in self.liveNeighborsForBirth

    def __str__(self):
        return "R " + "".join(str(i) for i in self.liveNeighborsForSurvival) + "/" +\
               "".join(str(i) for i in self.liveNeighborsForBirth)


ConwayRules = StandardRules({2, 3}, {3})
