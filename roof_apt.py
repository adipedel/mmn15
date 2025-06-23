from special_apt import SpecialApt

class RoofApt(SpecialApt):
    """
        A class to represent apartments that are roof apartments.
        class RoofApt inherits SpecialApt class which inherits Apt class.
        Attributes:
            _floor (int): The apartment's floor.
            _area (int): The apartment's area in square meters.
            _has_view (bool): always True because roof apartments have a view
            _has_pool (bool): True if the apartment has a pool and False if it doesn't
        Methods:
            __init__(self,floor,area,has_pool):: constructor
            get_floor(self): returns _floor value
            get_area(self): returns _area value
            get_has_view(self): returns _has_view value. always True because roof apartments have a view
            get_has_pool(self): returns _has_pool value.
            __eq__(self, other): compares two SpecialApt objects and returns True if they are equal.
            __str__(self): returns a string with the object values
            get_price(self): calculates and returns the price of the apartment
    """
    ROOF_VIEW = True        #roof apartment always have a view
    def __init__(self,floor,area,has_pool):
        super().__init__(floor,area,self.ROOF_VIEW)
        self._has_pool = has_pool

    def get_floor(self):
        return self._floor

    def get_area(self):
        return self._area

    def get_has_view(self):
        return self._has_view

    def get_has_pool(self):
        return self._has_pool

    def __eq__(self, other):
        if isinstance(other, RoofApt):
            return self._area == other._area and self._floor == other._floor and self._has_view == other._has_view and self._has_pool == other._has_pool
        else:
            return NotImplemented

    def __str__(self):
        return f"floor: {self._floor}, area: {self._area}, has_view: {self._has_view}, has_pool: {self._has_pool}"

    def get_price(self):
        roof_price = 40000
        pool_price = 30000
        price = SpecialApt.get_price(self) + roof_price #sends the object to the get_price method of a special apartment which returns the price and adds the roof price
        if self._has_pool:
            price = price + pool_price
        return price
