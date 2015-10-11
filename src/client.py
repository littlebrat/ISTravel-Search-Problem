import math

class State:

    def __init__(self, fr, to, transport, timestamp, trip_cost):
        self.__before = fr
        self.__now = to
        self.__transport = transport
        self.__time_available = timestamp
        self.__cost = trip_cost

    def transport(self):
        return self.__transport

    def departs(self):
        return self.__before

    def arrives(self):
        return self.__now

    def available(self):
        return self.__time_available

    def cost(self):
        return self.__cost

class Problem():

    def __init__(self, idn, start, goal, available, criteria):
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
        if state.arrives() is self.goal_node:
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
        return

    def getCostOfActions(self, actions):
        """
        This method returns the total cost of a particular sequence of actions.
        """
        res = 0
        for s in actions:
            res += s.cost()
        return res

    def getPlanDuration(self, actions):
        """
        This method returns the duration of the plan
        """
        return actions[-1].available()

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

    def __init__(self):
        self.clients = []

    def from_file(self, path):
        with open(path) as file:
            # from now on treat object as variable file.
            for line in file:
                # for each line in the file verify if the structure of the line is correct.
                words = line.split()
                if len(words) is 1:
                    # verifying the number of clients
                    clients_req = int(words[0])
                elif len(words) is 6 and words[5] is '0':
                    aux = Problem(words[0], int(words[1]), int(words[2]), int(words[3]), words[4])
                    self.clients.append(aux)
                elif (len(words) is 8 or 10) and (words[5] is '1' or '2'):
                    aux = Problem(words[0], int(words[1]), int(words[2]), int(words[3]), words[4])
                    aux.make_restriction(words[6], words[7])
                    if words[5] is '2':
                        aux.make_restriction(words[8], words[9])
                    self.clients.append(aux)
                else:
                    # return an exception if we don't find the expected number of words in a line.
                    return Exception('Wrong file format.')
        if clients_req is not len(self.clients):
            return Exception('Wrong file format.')

    def set_world(self,w):
        self.world = w

    def __str__(self):
        res = ''
        for c in self.clients:
            res += str(c) + '\n'
        return res

# testing
print("\n>> test 1\n")
clients = Pawns()
clients.from_file('client_files/client_test.cli')
print(clients)