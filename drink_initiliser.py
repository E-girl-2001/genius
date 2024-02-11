from classes import Beverage
from text_proccesser import *
DEFULT_BEER_ALC_CONTENT = 3.99 # if the alc content is not found in the description
DEFULT_RTD_ALC_CONTENT = 4.99 # if the alc content is not found in the description
DEFULT_WINE_ALC_CONTENT = 12.99 # if the alc content is not found in the description
DEFULT_SPIRIT_ALC_CONTENT = 30.99 # if the alc content is not found in the description
MISSING_ALC_CONTENT = -1
ZERO_ALC_CONTENT = 0


def init_drink(title, description, price, drink_type):
    print("1")
    if drink_type == "wine" or drink_type == "spirits":
        number_of_drinks = 1
    else:
        number_of_drinks = get_number_of_drinks(title)
    print("2")
    volume = get_volume(title)
    print("3")
    temp_alcohol_content = get_alc_content(title, description)
    print("4")
    if temp_alcohol_content == -1:
        if drink_type == "beer":
            alcohol_content = DEFULT_BEER_ALC_CONTENT
        elif drink_type == "rtd":
            alcohol_content = DEFULT_RTD_ALC_CONTENT
        elif drink_type == "wine":
            alcohol_content = DEFULT_WINE_ALC_CONTENT
        elif drink_type == "spirits":
            alcohol_content = DEFULT_SPIRIT_ALC_CONTENT
    elif temp_alcohol_content == -2:
        alcohol_content = ZERO_ALC_CONTENT
    else:
        alcohol_content = temp_alcohol_content
    print("5")
    drink = Beverage(title, price, number_of_drinks,
                    volume, alcohol_content, drink_type)
    print("6")
    return drink

