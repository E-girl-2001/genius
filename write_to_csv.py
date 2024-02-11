import csv
from classes import Beverage
import os


def init_csv(filename):
    """initialise the csv file"""
    if os.path.exists(filename):
        print("File already exists")
        return
    else:
        print("Creating New File...")
        with open(filename, "w") as new_file:
            writer = csv.writer(new_file)
            writer.writerow(["name", "price", "drinks_no", "volume", "alcohol_content", "dollars_per_standard", "alc_type"])
            print("File Initialised")
        return


# def add_drink_to_csv(drink, filename):
#     """generate drinks from the csv file"""
#     # print(f"Adding {drink.name} to file")
#     print(f"Adding {drink.name} to file")
#     if drink.name not in open(filename).read():
#         with open(filename, "a") as file:
#             writer = csv.writer(file)
#             writer.writerow([drink.name, drink.price, drink.drinks_no, drink.volume, drink.alcohol_content, drink.dollars_per_standard, drink.alc_type])
#         print(f"NEW: {drink.name} ADDED TO FILE")
#         print("Drink Added")
    
def is_drink_in_file(drink_name, filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == drink_name:
                return True
    return False

def add_drink_to_csv(drink, filename):
    """Add drink to the CSV file"""
    if not is_drink_in_file(drink.name, filename):
        with open(filename, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([drink.name, drink.price, drink.drinks_no, drink.volume, drink.alcohol_content, drink.dollars_per_standard, drink.alc_type])
        print(f"NEW: {drink.name} ADDED TO FILE")




def clear_csv(filename):
    """clear the csv file"""
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")
    print("file cleared")
    
    