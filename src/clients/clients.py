from src.search.problem import Problem
from src.search.heuristics import Heuristic

class Pawns:

    def __init__(self, world):
        self.clients = []
        self.world = world
        self.index = 0
        self.local_cost_min = world.get_min_cost_matrix()
        self.local_cost_min = Heuristic.make_optimal(self.local_cost_min)
        self.local_dur_min = world.get_min_time_matrix()
        self.local_dur_min = Heuristic.make_optimal(self.local_dur_min)

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
        self.file_name, garbage = path.split('.')
        with open(path) as file:
            # from now on treat object as variable file.
            for line in file:
                # for each line in the file verify if the structure of the line is correct.
                words = line.split()
                if len(words) is 1:
                    # verifying the number of clients
                    clients_req = int(words[0])
                elif len(words) is 6 and words[5] is '0':
                    if words[4] == 'tempo':
                        aux = Problem(words[0], int(words[1]), int(words[2]), int(words[3]), words[4], self.world, self.local_dur_min)
                    elif words[4] == 'custo':
                        aux = Problem(words[0], int(words[1]), int(words[2]), int(words[3]), words[4], self.world, self.local_cost_min)
                    self.clients.append(aux)
                elif (len(words) is 8 or 10) and (words[5] is '1' or '2'):
                    if words[4] == 'tempo':
                        aux = Problem(words[0], int(words[1]), int(words[2]), int(words[3]), words[4], self.world, self.local_dur_min)
                    elif words[4] == 'custo':
                        aux = Problem(words[0], int(words[1]), int(words[2]), int(words[3]), words[4], self.world, self.local_cost_min)
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
        with open(self.file_name + '.sol', "w") as file:
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
