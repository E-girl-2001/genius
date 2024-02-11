"""
Description: This file contains the functions 
that are used to process the text data from the website
"""

REALISTIC_DRINK_MAX = 30


def get_volume(title):
    measured_in_litres = False
    index = title.find("ML")
    if index == -1:
        index = title.find("LT")
        if index == -1:
            return 999
        measured_in_litres = True
    volume_string = ''
    index -= 1
    while title[index].isdigit():
        volume_string = title[index] + volume_string
        index -= 1
    number = int(volume_string)
    if measured_in_litres:
        number *= 1000
    print(str(number) + "ml")
    return number


def get_number_of_drinks(title):
    index = title.find("PACK")
    if index == -1:
        return 1
    num_string = ''
    index -= 2
    while title[index].isdigit():
        num_string = title[index] + num_string
        index -= 1
    number = int(num_string)
    if number > REALISTIC_DRINK_MAX:
        return 1
    print(str(number) + " per pack")
    return number


def get_alc_content(title, description):
    if "%" in title:
        index = title.find("%")
        alc_string = ''
        index -= 1
        while title[index].isdigit() or title[index] == "." and index >= 0:
            alc_string = title[index] + alc_string
            index -= 1
    elif "%" in description:
        index = description.find("%")
        alc_string = ''
        index -= 1
        while description[index].isdigit() or description[index] == "." and index >= 0:
            alc_string = description[index] + alc_string
            index -= 1
    else:
        return -1
    alc_content = float(alc_string)
    if alc_content == 0:
        return -2
    return alc_content

