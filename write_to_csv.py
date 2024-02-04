import csv
from classes import Beverage
import os


filename = "drinks.csv"

def write_from_list(drinks, filename):
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

def init_csv(filename):
    """initialise the csv file"""
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("Creating new file")
    with open(filename, "w") as new_file:
        writer = csv.writer(new_file)
        writer.writerow(["name", "price", "drinks_no", "volume", "alcohol_content", "dollars_per_standard", "alc_type"])
        print("file initialised")


def add_drink_to_csv(drink, filename):
    """generate drinks from the csv file"""
    if drink.name in open(filename).read():
        print(f"{drink.name} is already in the file")
    else:
        with open(filename, "a") as file:
            writer = csv.writer(file)
            writer.writerow([drink.name, drink.price, drink.drinks_no, drink.volume, drink.alcohol_content, drink.dollars_per_standard, drink.alc_type])
        print("drink added to file")




def clear_csv(filename):
    """clear the csv file"""
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")
    print("file cleared")
    
    