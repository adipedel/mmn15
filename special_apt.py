from apt import Apt

class SpecialApt(Apt):
    """
        A class to represent apartments that are special apartments.
        class SpecialApt inherits Apt class.
        Attributes:
            _floor (int): The apartment's floor.
            _area (int): The apartment's area in square meters.
            _has_view (bool): True if the apartment has a view and False if it doesn't
        Methods:
            __init__(self,floor,area,has_view): constructor
            get_floor(self): returns _floor value
            get_area(self): returns _area value
            get_has_view(self): returns _has_view value
            __eq__(self, other): compares two SpecialApt objects and returns True if they are equal.
            __str__(self): returns a string with the object values
            get_price: calculates and returns the price of the apartment
    """
    def __init__(self,floor,area,has_view):
        super().__init__(floor,area)
        self._has_view = has_view

    def get_floor(self):
        return self._floor

    def get_area(self):
        return self._area

    def get_has_view(self):
        return self._has_view

    def __eq__(self, other):
        if isinstance(other, SpecialApt):
            return self._area == other._area & self._floor == other._floor & self._has_view == other._has_view
        else:
            return NotImplemented

    def __str__(self):
        return f"floor: {self._floor}, area: {self._area}, has_view: {self._has_view}"

    def get_price(self):
        price_per_floor = 600
        price = Apt.get_price(self) #sends the object to the get_price method of a regular apartment which returns the price
        if self._has_view:
            price = price + price_per_floor*self._floor
        return price
