class State:

    def __init__(self, fr, to, transport, timestamp, trip_cost):
        self.__before = fr
        self.__now = to
        self.__transport = transport
        self.__time_available = timestamp
        self.__cost = trip_cost

    def transport(self):
        return self.__transport

    def departs(self):
        return self.__before

    def arrives(self):
        return self.__now

    def available(self):
        return self.__time_available

    def cost(self):
        return self.__cost

    def __str__(self):
        return 'from: ' + str(self.__before) + ', to: ' + str(self.__now) \
               + ', transport:  ' + str(self.__transport) + ', available at: ' \
               + str(self.__time_available) + ', cost: ' + str(self.__cost)