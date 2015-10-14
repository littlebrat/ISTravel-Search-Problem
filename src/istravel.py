import sys
from src.world import World
from src.client import Pawns
from src.search import SearchAgent


def main(args, debug = False):
    # Create the map object for this file
    earth = World()
    earth.from_file(args[1])

    # Create the client requests object for this file
    clients = Pawns(earth)
    clients.from_file(args[2])

    if debug is True:
        print('>>>  RUN SEARCH')
        i=1
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
    main(sys.argv,True)