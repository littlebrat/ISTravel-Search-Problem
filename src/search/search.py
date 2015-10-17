from src.utils.util import PriorityQueue,Stack,Queue


class SearchAgent:
    """
    Search algorithms to be used with the problems.
    """
    def __init__(self):
        self.data = None

    @staticmethod
    def depth_first_search(problem):
        """
        This search algorithm uses the depth first search algorithm for finding a path to its goal.
        Not optimal
        """
        closed = set()
        fringe = Stack()
        fringe.push([problem.getStartState()])
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
                        fringe.push(aux)

    @staticmethod
    def breadth_first_search(problem):
        """
        This search algorithm uses the breadth first search algorithm for finding a path to its goal.
        Not optimal because it doesn't use a cost for finding the optimal cost.
        """
        closed = set()
        fringe = Queue()
        fringe.push([problem.getStartState()])
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
                        fringe.push(aux)

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
