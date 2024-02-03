import numpy as np
from classes import Beverage
"""In NZ one standard drink is 10g of pure ethanol
 which is 12.67ml of ethanol"""
CONVERSION = 12.67



def calculate_dolars_per_standards(data):
    """calculate the total amount of alcohol in the data"""
    names = []
    dolars_per_standard = []
    for drink in data:
        dolars_per_standard.append(CONVERSION*float(drink.price)/(float(drink.drinks_no)*float(drink.volume)*(float(drink.alcohol_content)/100)))
        names.append(drink.name)
    return names, dolars_per_standard

def calculate_dolars_per_standard(price, number_of_drinks, volume, alcohol_content):
    """calculate the total amount of alcohol in the data"""
    return CONVERSION*float(price)/(float(number_of_drinks)*float(volume)*(float(alcohol_content)/100))
