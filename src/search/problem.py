import math

from src.search.state import State


class Problem:

    def __init__(self, idn, start, goal, available, criteria, world):
        self.client_id = idn
        self.start_node = start
        self.goal_node = goal
        self.available_time = available
        self.optimization_criteria = criteria
        self.unwanted_ride = None
        self.maximum_ride_cost = float("inf")
        self.maximum_ride_duration = float("inf")
        self.maximum_plan_cost = float("inf")
        self.maximum_plan_duration = float("inf")
        self.world = world

    def client_id(self):
        return self.client_id

    def set_unwanted_ride(self, ride):
        self.unwanted_ride = ride

    def set_max_ride_cost(self, number):
        self.maximum_ride_cost = int(number)

    def set_max_ride_dur(self, number):
        self.maximum_ride_duration = int(number)

    def set_max_plan_cost(self, number):
        self.maximum_plan_cost = int(number)

    def set_max_plan_dur(self, number):
        self.maximum_plan_duration = int(number)

    def make_restriction(self, key, value):
        restriction_list = {'A1': self.set_unwanted_ride, 'A2': self.set_max_ride_dur,
                            'A3': self.set_max_ride_cost, 'B1': self.set_max_plan_dur,
                            'B2': self.set_max_plan_cost}
        restriction_list[key](value)

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        return State(self.start_node, None, [math.floor(self.available_time / 1440),
                                                       self.available_time % 1440], 0)


    def isGoalState(self, state):
        """
        Returns True if and only if the state is a valid goal state.
        """
        if int(state.arrives()) == int(self.goal_node):
            return True
        else:
            return False

    def getSuccessors(self, state):
        """
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        trips = self.world.trips_from(state.arrives(), self.unwanted_ride, self.maximum_ride_cost,
                                      self.maximum_ride_duration)
        actions = []
        for t in trips:
            aux = State(t.destination(), t.type(), t.next_available_time(state.available()), t.cost())
            actions.append(aux)
        return actions

    def getCostOfActions(self, actions):
        """
        This method returns the total cost of a particular sequence of actions.
        """
        if self.optimization_criteria == 'tempo':
            return self.getPlanDuration(actions)
        elif self.optimization_criteria == 'custo':
            return self.getPlanCost(actions)
        else:
            return Exception('INVALID OPTIMIZATION CRITERIA')

    def getPlanDuration(self, actions):
        """
        This method returns the duration of the plan
        """
        total_time = actions[-1].available()[0]*1440+actions[-1].available()[1]-self.available_time
        return total_time

    def getPlanCost(self, actions):
        """
        This method returns the total cost of a particular sequence of actions.
        """
        res = 0
        for s in actions:
            res += int(s.cost())
        return res

    def isPlanValid(self, actions):
        """
        This method checks if the plan laid out is valid accordingly to the Bx restrictions
        """
        if self.getPlanCost(actions) <= self.maximum_plan_cost and self.getPlanDuration(actions) <= self.maximum_plan_duration:
            return True
        else:
            return False

    def writeActions(self, actions):
        res = str(self.client_id) + ' '
        if actions is None:
            res += str(-1)
        else:
            for i in range(len(actions)):
                state = actions[i]
                if i == 0:
                    res += str(state.arrives()) + ' '
                else:
                    res += state.transport() + ' ' + state.arrives() + ' '
            res += str(self.getPlanDuration(actions)) + ' ' + str(self.getPlanCost(actions))
        return res

    def __str__(self):
        res = "{id: " + str(self.client_id) + ', start: ' + str(self.start_node) + ', goal: ' \
              + str(self.goal_node) + ', available at: ' + str(self.available_time) \
              + ', optimization criteria: ' + self.optimization_criteria \
              + ', unwanted ride: ' + str(self.unwanted_ride) \
              + ', max ride cost: ' + str(self.maximum_ride_cost) + ', max ride duration: ' \
              + str(self.maximum_ride_duration) + ', max plan cost: ' + str(self.maximum_plan_cost) \
              + ', max plan duration: ' + str(self.maximum_plan_duration)
        return res