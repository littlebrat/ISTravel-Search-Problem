from src.world import World
from src.client import Pawns


earth = World()
earth.from_file('map_files/test_0.map')
print(earth)

clients = Pawns(earth)
clients.from_file('client_files/client_test.cli')

print('>>>  TESTS')
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
