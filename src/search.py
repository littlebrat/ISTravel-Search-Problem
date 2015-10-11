from src.util import Queue,PriorityQueue,Stack
from src.client import Problem

class SearchAgent:

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