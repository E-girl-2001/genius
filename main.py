from classes import Beverage
from liquorland import *
from write_to_csv import writer

drinks = get_drinks_data("spirits")

writer(drinks, "drinks.csv")




    
