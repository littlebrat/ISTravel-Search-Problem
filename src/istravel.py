from src.world import World
from src.client import Pawns
from src.search import SearchAgent

earth = World()
earth.from_file('map_files/test_0.map')
#print(earth)

clients = Pawns(earth)
clients.from_file('client_files/client_test.cli')

"""
print('>>>  Show Problems')
i=1
for c in clients:
    print('>> client: '+str(i))
    i += 1
    state = c.getStartState()
    print('Current state: '+ str(state))
    successors = c.getSuccessors(state)
    for s in successors:
        if c.isGoalState(s):
            print(s)
    print('\n')
"""

print('>>>  RUN SEARCH')
i=1
for c in clients:
    print('>> client: '+str(i))
    i += 1
    if i != 4:
        first = SearchAgent()
        plan = first.uniformCostSearch(c)
        res = ''
        for s in plan:
            res += str(s)+' '
        print(res)
        print('\n')

