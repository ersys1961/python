import time


class Date:
    def __init__(self, year, month, day):
        Date.validate(year, month, day)
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def date(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    @staticmethod
    def validate(year, month, day):
        if year < 0:
            raise Exception('***validate: year < 0')
        if month < 1 or month > 12:
            raise Exception('***validate: month < 1 or month > 12')
        if day < 1 or day > 31:
            raise Exception('***validate: day < 1 or day > 31')


d = Date(2021, 1, 12)
print(f' {d.year} {d.month}  {d.day}')
d = Date.date()
print(f' {d.year} {d.month}  {d.day}')
d = Date(2021, 1, 32)
print(f' {d.year} {d.month}  {d.day}')

