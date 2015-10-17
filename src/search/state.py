class State:
    """
    State describes the formulation used for this state in particular.
    A state is composed by:
        - a current node;
        - transport used to get here.
        - time that actor is available to travel.
        - monetary cost of the last trip.
    """

    def __init__(self, now, transport, timestamp, trip_cost):
        self.__now = now
        self.__transport = transport
        self.__time_available = timestamp
        self.__cost = trip_cost

    def transport(self):
        return self.__transport

    def arrives(self):
        return self.__now

    def available(self):
        return self.__time_available

    def cost(self):
        return self.__cost

    def __str__(self):
        return  'to: ' + str(self.__now) \
               + ', transport:  ' + str(self.__transport) + ', available at: ' \
               + str(self.__time_available) + ', cost: ' + str(self.__cost)