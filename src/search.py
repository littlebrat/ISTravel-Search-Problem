from src.util import Queue,PriorityQueue,Stack

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """

    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """

    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """

class SearchAgent:

    def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    closed = set()
    fringe = Stack()
    fringe.push([problem.getStartState(),[]])
    while True:
        if fringe.isEmpty(): return None
        v = fringe.pop()
        if problem.isGoalState(v[0]):
            return v[1]
        if v[0] not in closed:
            closed.add(v[0])
            for child in problem.getSuccessors(v[0]):
                way = v[1]+[child[1]]
                fringe.push([child[0],way])

    def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    closed = set()
    fringe = Queue()
    fringe.push([problem.getStartState(),[]])
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
                fringe.push([child[0],way])

    def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    closed = set()
    fringe = PriorityQueue()
    fringe.push([problem.getStartState(),[]],problem.getCostOfActions([]))
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
                fringe.push([child[0],way],problem.getCostOfActions(way))

    def aStarSearch(problem, heuristic=0):
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