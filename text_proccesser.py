"""
Description: This file contains the functions 
that are used to process the text data from the website
"""


def get_volume(title):
    measured_in_litres = False
    index = title.find("ML")
    if index == -1:
        index = title.find("LT")
        measured_in_litres = True
        if index == -1:
            return 999
    volume_string = ''
    index -= 1
    while title[index].isdigit():
        volume_string = title[index] + volume_string
        index -= 1
    number = int(volume_string)
    if measured_in_litres:
        number *= 1000
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
        return -2
    alc_string = ''
    index -= 1
    while description[index].isdigit() or description[index] == "." and index >= 0:
        alc_string = description[index] + alc_string
        index -= 1
    # print(alc_string + "%")
    alc_content = float(alc_string)
    if alc_content == 0:
        return -1
    return alc_content

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

