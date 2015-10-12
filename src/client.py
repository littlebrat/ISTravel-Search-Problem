from src.state import State
from src.world import Trip
import math


class Problem():

    def __init__(self, idn, start, goal, available, criteria, world):
        self.client_id = idn
        self.start_node = start
        self.goal_node = goal
        self.available_time = available
        self.optimization_criteria = criteria
        self.unwanted_ride = None
        self.maximum_ride_cost = math.inf
        self.maximum_ride_duration = math.inf
        self.maximum_plan_cost = math.inf
        self.maximum_plan_duration = math.inf
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
        return State(math.inf, self.start_node, None, [math.floor(self.available_time / 1440),self.available_time % 1440], 0)


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
        trips = self.world.trips_from(state.arrives(), self.unwanted_ride, self.maximum_ride_cost, self.maximum_ride_duration)
        actions = []
        for t in trips:
            aux = State(state.arrives(), t.destination(), t.type(), t.next_available_time(state.available()), t.cost())
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

    def getPlanCost(self,actions):
        """
        This method returns the total cost of a particular sequence of actions.
        """
        res = 0
        for s in actions:
            res += int(s.cost())
        return res

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


class Pawns:

    def __init__(self, world):
        self.clients = []
        self.world = world
        self.index = 0

    def __iter__(self):
         return self

    def __next__(self):
         try:
             result = self.clients[self.index]
         except IndexError:
             raise StopIteration
         self.index += 1
         return result

    def from_file(self, path):
        self.file_name , garbage = path.split('.')
        with open(path) as file:
            # from now on treat object as variable file.
            for line in file:
                # for each line in the file verify if the structure of the line is correct.
                words = line.split()
                if len(words) is 1:
                    # verifying the number of clients
                    clients_req = int(words[0])
                elif len(words) is 6 and words[5] is '0':
                    aux = Problem(words[0], int(words[1]), int(words[2]), int(words[3]), words[4], self.world)
                    self.clients.append(aux)
                elif (len(words) is 8 or 10) and (words[5] is '1' or '2'):
                    aux = Problem(words[0], int(words[1]), int(words[2]), int(words[3]), words[4], self.world)
                    aux.make_restriction(words[6], words[7])
                    if words[5] is '2':
                        aux.make_restriction(words[8], words[9])
                    self.clients.append(aux)
                else:
                    # return an exception if we don't find the expected number of words in a line.
                    return Exception('Wrong file format.')
        if clients_req is not len(self.clients):
            return Exception('Wrong file format.')

    def to_file(self, bulk):
        with open(self.file_name + '.solx', "w") as file:
            for i in range(len(bulk)):
                p = self.clients[i]
                aux = p.writeActions(bulk[i]) + '\n'
                file.write(aux)
            file.close()

    def __str__(self):
        res = ''
        for c in self.clients:
            res += str(c) + '\n'
        return res