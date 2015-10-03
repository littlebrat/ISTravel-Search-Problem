class Trip:

    def __init__(self,dest,ty,dur,c,ti,tf,p):
        self.__destination = dest
        self.__type = ty
        self.__duration = dur
        self.__cost = c
        self.__timeinit = ti
        self.__timefinal = tf
        self.__periodicity = p



class World:

    def __init__(self):
        self.__graph = {}

    def from_file(self,path):
        with open(path) as file:
            for line in file:
                words = line.split()
                if len(words) is 2:

                else:
                    if words[0] is '*':
                        self.root.set_next_hop(words[1])
                    else:
                        self.insert(words[0],words[1])