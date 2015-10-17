from src.problem import Problem


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
