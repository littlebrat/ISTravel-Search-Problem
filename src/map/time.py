class Timetable:
    """
    Class that describes the schedule for a specific trip.
    """

    def __init__(self, ti, tf, p):
        self.table = []
        i = 0
        while ti + i * p <= tf:
            self.table.append(ti + i * p)
            i += 1

    def next_trip(self, time):
        i = 0
        while i < len(self.table):
            if time[1] <= self.table[i]:
                return [time[0], self.table[i]]
            i += 1
        return [time[0]+1, self.table[0]]

    def __str__(self):
        res = '( '
        for x in self.table:
            res += str(x) + ' '
        return res + ')'
