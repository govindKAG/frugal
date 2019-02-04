class Item(object):
    def __init__(self):
        self.price = None
        self.years = None
        self.usage = None
        self.label = None

    def called(self, label):
        self.label = label
        return self

    def whichcosts(self, price):
        self.price = price
        return self

    def whichlasts(self, years):
        self.years = years
        return self

    def used(self, usage):
        self.usage = usage
        return self

    def __str__(self):
        return f"""{self.label}
        lasted {self.years}
        use per year {self.usage}
        cost {self.price}"""
    def as_tuple(self):
        return (self.price, self.years, self.usage, self.label)
