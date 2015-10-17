from src.map.trip import Trip


class World:
    """
    This class defines the world for the search problem on a graph like structure - a dictionary
    """

    def __init__(self):
        self.__graph = {}

    def from_file(self, path):
        # this method loads a file into a object of this class.
        with open(path) as file:
            # from now on treat object as variable file.
            for line in file:
                # for each line in the file verify if the structure of the line is correct.
                words = line.split()
                if len(words) is 2:
                    # if we are on the first line of the file, declare the structure of the dictionary.
                    cities = int(words[0])
                    for x in range(1, cities+1):
                        self.__graph[x] = []
                elif len(words) is 8:
                    # if we are on another line of the file with 8 words add edge to the graph. Graph is symmetrical so we add one edge to the inverse connection.
                    aux = Trip(words[1],words[2],words[3],words[4],words[5],words[6],words[7])
                    self.__graph[int(words[0])].append(aux)
                    auxreturn = Trip(words[0],words[2],words[3],words[4],words[5],words[6],words[7])
                    self.__graph[int(words[1])].append(auxreturn)
                else:
                    # return an exception if we don't find the expected number of words in a line.
                    return Exception('Wrong file format.')

    def trips_from(self, city, type_set = None, max_cost = None, max_dur = None):
        # receives a current city and an optional argument referring to the impossible means
        #  of transportation (this argument has a structure of a set)
        trips = self.connections(int(city))
        # if there is no preference return all edges.
        if type_set is None:
            type_set = ''
        if max_cost is None:
            max_cost = float("inf")
        if max_dur is None:
            max_dur = float("inf")
        res = []
        for t in trips:
            if t.type() != type_set and max_cost >= int(t.cost()) and max_dur >= int(t.duration()):
                res.append(t)
        return res

    def connections(self,node):
        return self.__graph[node]

    def __str__(self):
        res = ''
        for key in sorted(self.__graph.keys()):
            res += 'NODE: ' + str(key) + ': \n'
            for trip in self.__graph[key]:
                res += trip.__str__() + '\n'
        return res
