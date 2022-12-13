class Calender:
    def __init__(self, day, month, year):
        if isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            if year > 1:
                self.year = year
            else:
                raise Exception("Year must be above 0!")
            if 1 <= month <= 12:
                self.month = month
            else:
                raise Exception("Month must be between 1 and 12!")
            if self.month_day(month, year) >= day >=1:
                self.day = day
            else:
                raise Exception("Day must be between 1 and " + str(self.month_day(month, year)) + "!")
        else:
            raise Exception("Day must be integer!")
            
    def month_day(self, month, year):
        if month == 2:
            if year % 4 == 0:
                return 29
            else:
                return 28
        elif month in (1, 3, 5, 7, 8, 10,12):
            return 31
        else:
            return 30

    def __eq__(self, other):
        if isinstance(other, Calender):
            return self.day == other.day and self.month == other.month and self.year == other.year
        else:
            raise Exception("Must compare with instance of Calendar!")

    def __ne__(self, other):
            return not self == other


    def __gt__(self, other):
        if isinstance(other, Calender):
            if self.year < other.year:
                return False
            elif self.year > other.year:
                return True
            else:
                if self.month < other.month:
                    return False
                elif self.month > other.month:
                    return True
                else:
                    if self.day <= other.day:
                        return False
                    else:
                        return True
        else:
            raise Exception("Must compare with instance of Calendar")

    def __lt__(self, other):
        if isinstance(other, Calender):
            return not (self > other or self == other)
        else:
            raise Exception("Must compare with instance of Calendar")

    def __ge__(self, other):
        if isinstance(other, Calender):
            return self > other or self == other
        else:
            raise Exception("Must compare with instance of Calendar")

    def __le__(self, other):
        if isinstance(other, Calender):
            return self < other or self == other
        else:
            raise Exception("Must compare with instance of Calendar")

    def __iadd__(self, other):
        if isinstance(other, Calender):
            self.year += other.year
            self.month += other.month
            self.day += other.day
            max_days = self.month_day(self.month, self.year)

            while self.month > 12:
                self.month -= 12
                self.year += 1

            while self.day > max_days:
                self.day -= max_days
                self.month += 1

            if self.month > 12:
                self.month -= 12
                self.year += 1
            return self
        else:
            raise Exception("Must be an instance of Calendar")

    def __isub__(self, other):
        if isinstance(other, Calender):
            self.year -= other.year
            self.month -= other.month
            self.day -= other.day
            max_days = self.month_day(self.month, self.year)

            while self.month <= 0:
                self.month += 12
                self.year -= 1

            while self.day <= 0:
                self.day += max_days
                self.month -= 1

            if self.month <= 0:
                self.month += 12
                self.year -= 1
            return self
        else:
            raise Exception("Must be an instance of Calendar")