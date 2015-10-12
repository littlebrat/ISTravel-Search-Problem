from src.world import World
from src.client import Pawns
from src.search import SearchAgent

earth = World()
earth.from_file('map_files/test_0.map')

clients = Pawns(earth)
clients.from_file('client_files/client_test.cli')

print('>>>  RUN SEARCH')
i=1
towrite = []
for c in clients:
    print('>> client: '+str(i))
    i += 1
    first = SearchAgent()
    plan = first.uniformCostSearch(c)
    print(c.writeActions(plan))
    towrite.append(plan)
clients.to_file(towrite)