import csv
from classes import Beverage
import os


filename = "drinks.csv"

def writer(drinks, filename):
    """write a new csv file"""
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")
    with open(filename, "w") as new_file:
        writer = csv.writer(new_file)
        writer.writerow(["name", "price", "drinks_no", "volume", "alcohol_content", "dollars_per_standard", "alc_type"])
        for drink in drinks:
            writer.writerow([drink.name, drink.price, drink.drinks_no, drink.volume, drink.alcohol_content, drink.dollars_per_standard, drink.alc_type])
    print("file written")