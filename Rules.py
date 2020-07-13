class Rules:
    def survives(self, live_neighbors) -> bool:
        pass

    def born(self, live_neighbors) -> bool:
        pass


class StandardRules(Rules):
    def __init__(self, live_neighbors_for_survival, live_neighbors_for_birth):
        self.liveNeighborsForSurvival = live_neighbors_for_survival
        self.liveNeighborsForBirth = live_neighbors_for_birth

    def survives(self, live_neighbors) -> bool:
        return live_neighbors in self.liveNeighborsForSurvival

    def born(self, live_neighbors) -> bool:
        return live_neighbors in self.liveNeighborsForBirth

    def __str__(self):
        return "R " + "".join(str(i) for i in self.liveNeighborsForSurvival) + "/" +\
               "".join(str(i) for i in self.liveNeighborsForBirth)

    def __eq__(self, other):
        return self.liveNeighborsForSurvival == other.liveNeighborsForSurvival and\
               self.liveNeighborsForBirth == other.liveNeighborsForBirth


ConwayRules = StandardRules({2, 3}, {3})
