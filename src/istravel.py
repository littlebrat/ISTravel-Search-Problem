import sys

from src.map.world import World
from src.clients.clients import Pawns
from src.search.search import SearchAgent


def main(args):

    if len(args) == 4 and args[3] == '-d':
        debug = True
    else:
        debug = False

    # Create the map object for this file
    earth = World()
    earth.from_file(args[1])

    # Create the client requests object for this file
    clients = Pawns(earth)
    clients.from_file(args[2])

    #Search Procedure
    if debug is True:
        print('>>>  RUN SEARCH')
        i = 1
    towrite = []
    for c in clients:
        if debug is True:
            print('>> client: '+str(i))
            i += 1
        first = SearchAgent()
        plan = first.uniformCostSearch(c)
        if debug is True:
            print(c.writeActions(plan))
        towrite.append(plan)
    clients.to_file(towrite)

if __name__ == "__main__":
    main(sys.argv)