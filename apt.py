class Apt:
    """
        Apartments.
        Attributes:
            _floor (int): The apartment's floor.
            _area (int): The apartment's area in square meters.
        Methods:
            __init__(self,floor,area): constructor
            get_floor(self): returns _floor value
            get_area(self): returns _area value
            __eq__(self, other): compares two SpecialApt objects and returns True if they are equal.
            __str__(self): returns a string with the object values
            get_price: calculates and returns the price of the apartment
    """
    def __init__(self,floor,area):
        self._floor = floor
        self._area = area

    def get_floor(self):
        return self._floor

    def get_area(self):
        return self._area

    def __eq__(self, other):
        if isinstance(other, Apt):
            return self._area == other._area and self._floor == other._floor
        else:
            return NotImplemented

    def __str__(self):
        return f"floor: {self._floor}, area: {self._area}"

    def get_price(self):
        price_per_square_meter = 20000
        price_per_floor = 5000
        first_floor = 1
        price = self._area*price_per_square_meter
        if self._floor > first_floor:
            price = price + price_per_floor * self._floor
        return price