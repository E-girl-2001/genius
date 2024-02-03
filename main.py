from classes import Beverage
from liquorland import *
from calcs import calculate_dolars_per_standards
from plotter import plot_drinks
from write_to_csv import writer

beers = get_beer_data()
print(beers)
print(len(beers))
writer(beers, "beers.csv")





    
