from src.utils.util import PriorityQueue


class SearchAgent:
    """
    Search algorithms to be used with the problems.
    """
    def __init__(self):
        self.data = None


    @staticmethod
    def uniformCostSearch(problem,heuristic=0):
        """
        This search algorithm can be used for Uniform Cost Search or A* depending on the given heuristic function.
        """
        closed = set()
        fringe = PriorityQueue()
        fringe.push([problem.getStartState()],problem.getCostOfActions([problem.getStartState()]) + heuristic)
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
                        fringe.push(aux, problem.getCostOfActions(aux)+heuristic)
