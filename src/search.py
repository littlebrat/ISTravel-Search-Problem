from src.util import PriorityQueue


class SearchAgent:
    def __init__(self):
        self.data = None

    def uniformCostSearch(self, problem):
        """Search the node of least total cost first."""
        closed = set()
        fringe = PriorityQueue()
        fringe.push([problem.getStartState()],problem.getCostOfActions([problem.getStartState()]))
        while True:
            if fringe.isEmpty():
                return None
            v = fringe.pop()
            if problem.isGoalState(v[-1]):
                return v
            if v[-1].arrives() not in closed:
                closed.add(v[-1].arrives())
                # put everything tabbed if we used closed sets
                for child in problem.getSuccessors(v[-1]):
                    aux = v + [child]
                    if problem.isPlanValid(aux):
                        fringe.push(aux, problem.getCostOfActions(aux))

    def aStarSearch(self, problem, heuristic=0):
        """Search the node that has the lowest combined cost and heuristic first."""
        closed = set()
        fringe = PriorityQueue()
        fringe.push([problem.getStartState(),[]],problem.getCostOfActions([])+heuristic(problem.getStartState(),problem))
        while True:
            if fringe.isEmpty():
                return None
            v = fringe.pop()
            if problem.isGoalState(v[0]):
                return v[1]
            if v[0] not in closed:
                closed.add(v[0])
                for child in problem.getSuccessors(v[0]):
                    way = v[1]+[child[1]]
                    fringe.push([child[0],way],problem.getCostOfActions(way)+heuristic(child[0],problem))