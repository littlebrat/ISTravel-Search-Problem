import math


class Timetable:
    """
    Class that describes the schedule for a specific trip.
    """

    def __init__(self, ti, tf, p):
        self.table = []
        i = 0
        while ti + i * p <= tf:
            self.table.append(ti + i * p)
            i += 1

    def next_trip(self, time):
        i = 0
        while i < len(self.table):
            if time[1] <= self.table[i]:
                return [time[0], self.table[i]]
            i += 1
        return [time[0]+1, self.table[0]]

    def __str__(self):
        res = '( '
        for x in self.table:
            res += str(x) + ' '
        return res + ')'


class Trip:
    """
    This class defines the structure of a trip in a graph accordingly to the following arguments:
        1) departure city
        2) arrival city
        3) type of transport
        4) duration of the trip
        5) cost of the trip
        6) opening minute of the trip
        7) last trip of the day minute
        8) period of the trip
    """

    def __init__(self, dest, ty, dur, c, ti, tf, p):
        self.__destination = dest
        self.__type = ty
        self.__duration = dur
        self.__cost = c
        self.__schedule = Timetable(int(ti), int(tf), int(p))

    def destination(self):
        return self.__destination

    def type(self):
        return self.__type

    def duration(self):
        return self.__duration

    def cost(self):
        return self.__cost

    def schedule(self):
        return self.__schedule

    def next_available_time(self, time):
        next_trip = self.__schedule.next_trip(time)
        duration = [math.floor(self.__duration / 1440),self.__duration % 1440]
        return next_trip + duration

    def __str__(self):
        res = self.__destination + ' ' + self.__type + ' ' + self.__duration + ' ' + self.__cost + ' ' + str(self.__schedule)
        return res


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
                    for x in range(1,cities):
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
        trips = self.__graph[city]
        # if there is no preference return all edges.
        if type_set is None:
            type_set = ''
        if max_cost is None:
            max_cost = math.inf
        if max_dur is None:
            max_dur = math.inf
        res = []
        for t in trips:
            if t.type() != type_set and max_cost >= int(t.cost()) and max_dur >= int(t.duration()):
                res.append(t)
        return res

    def __str__(self):
        res = ''
        for key in sorted(self.__graph.keys()):
            res += 'NODE: ' + str(key) + ': \n'
            for trip in self.__graph[key]:
                res += trip.__str__() + '\n'
        return res



# testing
earth = World()
earth.from_file('map_files/test_0.map')
print("\n>> test 1\n")
print(earth)

print("\n>> test 2\n")
list2 = earth.trips_from(9)
for trip in list2:
    print(trip)

print("\n>> test 3\n")
list3 = earth.trips_from(9,'comboio')
for trip in list3:
    print(trip)

print("\n>> test 4\n")
list3 = earth.trips_from(9,'comboio',8)
for trip in list3:
    print(trip)

print("\n>> test 5\n")
list3 = earth.trips_from(9,'comboio',None,25)
for trip in list3:
    print(trip)

print("\n>> test 6\n")
scdl = Timetable(0, 1000, 200)
print(scdl)
print(scdl.next_trip([4,1001]))

