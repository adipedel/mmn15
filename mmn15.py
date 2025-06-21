"""
Project: Maman15

The functions in this project, calculates data of apartments from the classes: 'Apt', 'SpecialApt', 'RoofApt' and 'GardenApt'
functions:
    average_price(apts): receives a lists of apartments and returns the average price
    how_many_rooftop(apts): receives a lists of apartments and returns the number of apartments with a rooftop and a pool
    how_many_apt_type(apts): receives a lists of apartments and returns a dict with the number of apartments of each type.
    top_price(apts): receives a lists of apartments and returns the most expensive apartment.
    only_valid_apts(apts): receives a lists of apartments and returns a list of apartments with a view or a pool that cost over 1000000 shekels.

ID : 211398029
Author: Adi Pedel
Semester : 2025b
"""

from apt import Apt
from special_apt import SpecialApt
from roof_apt import RoofApt
from garden_apt import GardenApt


def average_price(apts):
    """
        Gets a list of Apts and returns the average apartments price.
        the function will go through the list of apartments and for each apartment will add one to the var apts_count,
        and will add the price of that apartment to the var price_count. the function will check the type of each apartment
        and will use the function get_price() of the appropriate class to calculate the price. after going through the list
        we will calculate the average by dividing price_count with apts_count.

        param:
            apts (list): A list of Apts.
        Returns:
            average: The average price of the apartments
        """
    apts_count = 0
    price_count = 0
    if not apts:
        return 0
    for apartment in apts:
        apts_count += 1
        if isinstance(apartment,GardenApt):
            price_count += GardenApt.get_price(apartment)
        elif isinstance(apartment,RoofApt):
            price_count += RoofApt.get_price(apartment)
        elif isinstance(apartment,SpecialApt):
            price_count += SpecialApt.get_price(apartment)
        elif isinstance(apartment,Apt):
            price_count += Apt.get_price(apartment)
    average = price_count/apts_count
    return average

def how_many_rooftop(apts):
    """
        Gets a list of Apts and returns the number of apartments with a rooftop and a pool.
        the function will go through the list of apartments and will check the type of each apartment.
        if the type is RoofApt we will check if it has a pool using the 'get_has_pool' function, and we will add 1 to the
        var apts_count, this will add up to be the number of apartments with a rooftop. we will return this number.

        param:
            apts (list): A list of Apts.
        Returns:
            apts_count: the number of apartments with a rooftop.
        """
    apts_count = 0
    for apartment in apts:
        if isinstance(apartment,RoofApt):
            if RoofApt.get_has_pool(apartment):
                apts_count += 1
    return apts_count

def how_many_apt_type(apts):
    """
        Gets a list of Apts and returns a dict with the number of apartments of each type.
        the function creates a dictionary with the keys Apt,SpecialApt','RoofApt','GardenApt' for each type.
        the function will go through the list of apartments and will check the type of each apartment.
        we will add 1 to the key in the dictionary that is of the type of that apartment.

        param:
            apts (list): A list of Apts.
        Returns:
            apts_dict: a dict with the number of apartments of each type.
        """
    apts_dict = {'Apt':0, 'SpecialApt':0, 'RoofApt':0, 'GardenApt':0}
    for apartment in apts:
        if isinstance(apartment,GardenApt):
            apts_dict['GardenApt'] += 1
        elif isinstance(apartment,RoofApt):
            apts_dict['RoofApt'] += 1
        elif isinstance(apartment,SpecialApt):
            apts_dict['SpecialApt'] += 1
        elif isinstance(apartment,Apt):
            apts_dict['Apt'] += 1
    return apts_dict

def top_price(apts):
    """
        Gets a list of Apts and returns the apartment with the highest price.
        the function will go through the list of apartments and for each apartment will check if the price is higher
        than the current apartment with the highest price, using the vars: maximum_price for the maximum price value
        and maximum_apt for the apartment object with the maximum value. the function will check the type of each apartment
        and will use the function get_price() of the appropriate class to calculate the price. we will return the apartment
        with the highest price.

        param:
            apts (list): A list of Apts.
        Returns:
            maximum_apt: The apartment with the highest price in the list.
        """
    maximum_price = 0
    maximum_apt = None
    for apartment in apts:
        if isinstance(apartment,GardenApt):
            if GardenApt.get_price(apartment) > maximum_price:
                maximum_price = GardenApt.get_price(apartment)
                maximum_apt = apartment
        elif isinstance(apartment,RoofApt):
            if RoofApt.get_price(apartment) > maximum_price:
                maximum_price = RoofApt.get_price(apartment)
                maximum_apt = apartment
        elif isinstance(apartment,SpecialApt):
            if SpecialApt.get_price(apartment) > maximum_price:
                maximum_price = SpecialApt.get_price(apartment)
                maximum_apt = apartment
        elif isinstance(apartment,Apt):
           if Apt.get_price(apartment) > maximum_price:
                maximum_price = Apt.get_price(apartment)
                maximum_apt = apartment
    return maximum_apt

def only_valid_apts(apts):
    """
        Gets a list of Apts and returns a list with a view or with a pool that cost over 1000000 shekels.
        the function will go through the list of apartments and for each apartment will check if the price is over 1000000
        shekels, and it has a view or pool. If so we will add the apartment to the list 'apts_list'.
        the function will check the type of each apartment and will use the function get_price() of the appropriate class
         to calculate the price. If it's not a normal apartment we will check the value of 'has_view' and if it's a
         roof_apt we will check the value 'has_pool'.
        param:
            apts (list): A list of Apts.
        Returns:
            apts_list: a list of apartments with a view or a pool that cost over 1000000 shekels.
        """
    apts_list = []
    minimum_price = 1000000
    for apartment in apts:
        if isinstance(apartment,GardenApt):
            if (GardenApt.get_price(apartment) > minimum_price) & (GardenApt.get_has_view(apartment) == True):
                apts_list.append(apartment)
        elif isinstance(apartment,RoofApt):
                if (RoofApt.get_price(apartment) > minimum_price) & (RoofApt.get_has_view(apartment) == True |
                                                             RoofApt.get_has_pool(apartment) == True):
                    apts_list.append(apartment)
        elif isinstance(apartment,SpecialApt):
            if (SpecialApt.get_price(apartment) > minimum_price) & (SpecialApt.get_has_view(apartment) == True):
                apts_list.append(apartment)
    if not apts_list:
        return None
    return apts_list
