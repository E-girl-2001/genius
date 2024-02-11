
CONVERSION = 12.67

class Beverage:
    """A class to represent a beverage.
    Attributes:
        name (str): the name of the drink
        price (float): the price of the drink
        drinks_no (int): the number of drinks in a pack
        volume (int): the volume of each drink
        alcohol_content (float): the percentage of alcohol in the drink
        dollar_per_standard (float): the price of the drink per standard drink
        type (str): the type of the drink
        
        format: name, price, drinks_no, volume, alcohol_content, dollar_per_standard, alc_type"""
    def __init__(self, name, price, drinks_no, volume, alcohol_content, alc_type):
        self.name = name
        self.price = price
        self.drinks_no = drinks_no
        self.volume = volume
        self.alcohol_content = alcohol_content
        if alcohol_content == 0:
            self.dollars_per_standard = 0
        else:
            self.dollars_per_standard = round(CONVERSION*float(price)/(float(drinks_no)*float(volume)*(float(alcohol_content)/100)), 2)
        self.alc_type = alc_type


    def __repr__(self):
        return f"{self.name}, ${self.price}, {self.drinks_no} Drinks, {self.volume}ml, {self.alcohol_content}%, ${self.dollars_per_standard} per standard, {self.alc_type}"