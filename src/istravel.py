from src.world import World
from src.client import Pawns

earth = World()
earth.from_file('map_files/test_0.map')
print(earth)

clients = Pawns(earth)
clients.from_file('client_files/client_test.cli')
print(clients)