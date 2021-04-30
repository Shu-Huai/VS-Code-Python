class Time(object):
    def __init__(self, hour=0, minute=0, second=0) -> None:
        super().__init__()
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        return "%02d:%02d:%02d" % (self.__hour, self.__minute, self.__second)

    def __add__(self, T):
        hour = self.__hour + T.__hour
        minute = self.__minute + T.__minute
        second = self.__second + T.__second
        if second >= 60:
            second -= 60
            minute += 1
        if minute >= 60:
            minute -= 60
            hour += 1
        if hour >= 24:
            hour -= 24
        return Time(hour, minute, second)

    def TimeToInt(self):
        return self.__second + 60 * self.__minute + 3600 * self.__hour

    def PrintTime(self):
        print("Time is: %02d:%02d:%02d." % (self.__hour, self.__minute, self.__second))

    def IsAfter(self, T):
        if self.TimeToInt() > T.TimeToInt():
            return True
        return False

    def Increment(self, incrementSecond):
        if incrementSecond <= 0:
            return self
        hour = self.__hour
        minute = self.__minute
        second = self.__second
        second += incrementSecond
        minute += second // 60
        second = second % 60
        hour += minute // 60
        minute = minute % 60
        hour = hour % 24
        return Time(hour, minute, second)

    def IsValid(self):
        if self.__hour >= 24:
            return False
        if self.__minute >= 60:
            return False
        if self.__second >= 60:
            return False
        return True


T = Time(0, 1, 30)
print("Time is: %s." % T)
print("Time + 00:00:30 = %s." % (T + Time(0, 0, 30)))
print("Convert to second: %ds." % T.TimeToInt())
T.PrintTime()
print("Time is after 00:00:30:", T.IsAfter(Time(0, 0, 30)))
print("Time after 120s is: %s." % T.Increment(120))
print("Time is valid:", T.IsValid())