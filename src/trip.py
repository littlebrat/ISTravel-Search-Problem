import math
from src.time import Timetable

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
        minutes = (next_trip[1] + int(self.__duration)) % 1440
        days = next_trip[0] + math.floor((int(self.__duration)+next_trip[1]) / 1440)
        return [days, minutes]

    def __str__(self):
        res = self.__destination + ' ' + self.__type + ' ' + self.__duration + ' ' + self.__cost + ' ' + str(self.__schedule)
        return res