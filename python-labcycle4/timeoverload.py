class Time:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __add__(self, other):
        return self.hour + other.hour, self.minute + other.minute, self.second + other.second

o1 = Time(8, 9, 12)
o2 = Time(5, 25, 33)
result = o1 + o2
print("sum of time", result)
