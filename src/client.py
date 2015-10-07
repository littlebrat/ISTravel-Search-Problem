import math


class Client:

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
        self.maximum_ride_cost = number

    def set_max_ride_dur(self, number):
        self.maximum_ride_duration = number

    def set_max_plan_cost(self, number):
        self.maximum_plan_cost = number

    def set_max_plan_dur(self, number):
        self.maximum_plan_duration = number

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
                    aux = Client(words[0], int(words[1]), int(words[2]), int(words[3]), words[4])
                    self.clients.append(aux)
                elif (len(words) is 8 or 10) and (words[5] is '1' or '2'):
                    aux = Client(words[0], int(words[1]), int(words[2]), int(words[3]), words[4])

                    self.clients.append(aux)
                else:
                    # return an exception if we don't find the expected number of words in a line.
                    return Exception('Wrong file format.')
