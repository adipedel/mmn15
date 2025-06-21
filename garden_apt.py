from special_apt import SpecialApt

class GardenApt(SpecialApt):
    """
        Apartments that are garden apartments.
        class GardenApt inherits SpecialApt class which inherits Apt class.
        Attributes:
            _floor (int): The apartment's floor. (always 0 for garden apartment)
           _area (int): The apartment's area in square meters.
           _has_view (bool): True if the apartment has a view and False if it doesn't (always False for garden apartment)
           _garden_area (int): The apartment's garden area in square meters.
        Methods:
            __init__(self,area,garden_area): constructor
            get_floor(self): returns _floor value
            get_area(self): returns _area value
            get_has_view(self): returns _has_view value. always True because roof apartments have a view
            get_garden_area(self): returns _garden_area value.
            __eq__(self, other): compares two SpecialApt objects and returns True if they are equal.
            __str__(self): returns a string with the object values
            get_price(self): calculates and returns the price of the apartment
        """
    GARDEN_FLOOR = 0            #garden apartment floor is always 0.
    GARDEN_VIEW = False         #garden apartment has no view.
    def __init__(self,area,garden_area):
        super().__init__(self.GARDEN_FLOOR,area,self.GARDEN_VIEW)
        self._garden_area = garden_area

    def get_floor(self):
        return self._floor

    def get_area(self):
        return self._area

    def get_has_view(self):
        return self._has_view

    def get_garden_area(self):
        return self._garden_area

    def __eq__(self, other):
        if isinstance(other, GardenApt):
            return self._area == other._area & self._floor == other._floor & self._has_view == other._has_view & self._garden_area == other._garden_area
        else:
            return NotImplemented

    def __str__(self):
        return f"floor: {self._floor}, area: {self._area}, has_view: {self._has_view}, garden_area: {self._garden_area}"

    def get_price(self):
        price = SpecialApt.get_price(self) #sends the object to the get_price method of a special apartment which returns the price
        return price
