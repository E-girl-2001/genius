
from classes import Beverage
from calcs import calculate_dolars_per_standard
DEFULT_ALC_CONTENT = 3.99 # if the alc content is not found in the description

def init_beer(title, description, price):
    name = get_name(title)
    # print(name)
    number_of_drinks = get_number_of_drinks(title)
    # print(number_of_drinks)
    volume = get_volume(title)
    # print(volume)
    alcohol_content = get_alc_content(description)
    # print(alcohol_content)
    drink = Beverage(name, price, number_of_drinks,
                    volume, alcohol_content, "beer")
    return drink

def get_volume(title):
    index = title.find("ML")
    volume_string = ''
    index -= 1
    while title[index].isdigit():
        volume_string = title[index] + volume_string
        index -= 1
    number = int(volume_string)
    # print(str(number) + "ml")
    return number

def get_number_of_drinks(title):
    index = title.find("PACK")
    num_string = ''
    index -= 2
    while title[index].isdigit():
        num_string = title[index] + num_string
        index -= 1
    number = int(num_string)
    # print(str(number) + " per pack")
    return number

def get_alc_content(description):
    index = description.find("%")
    if index == -1:
        return DEFULT_ALC_CONTENT
    alc_string = ''
    index -= 1
    while description[index].isdigit() or description[index] == "." and index >= 0:
        alc_string = description[index] + alc_string
        index -= 1
    # print(alc_string + "%")
    return alc_string

def get_name(title):
    name = ''
    for i in title:
        if not i.isdigit():
            name += i
        else:
            break
    return name

# print(get_volume("BAVARIA HOLLAND 8.6 4 PACK CANS 500ML"))
# print(get_number_of_drinks("BAVARIA HOLLAND 8.6 4 PACK CANS 500ML"))

