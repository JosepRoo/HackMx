import time


class Period(object):
    def __init__(self, day, initialTime, finalTime):
        self.day = day
        self.initialTime = time.strptime(initialTime, "%H:%M")
        self.finaTime = time.strptime(finalTime, "%H:%M")

    @staticmethod
    def create_period(period):
        return Period(period['day'], period['initialTime'], period['finalTime'])

    def json(self):
        return {
            'day': self.day,
            'initialTime': time.strftime("%H:%M", self.initialTime),
            'finalTime': time.strftime("%H:%M", self.finaTime),
        }

