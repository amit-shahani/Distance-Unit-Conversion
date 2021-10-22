def add_unit(list_of_units, arr):
    unit = str(input('Enter the new unit: ').lower())
    conversion_ratio = float(
        input('Enter the conversion ration from metres: '))
    list_of_units.update({unit: conversion_ratio})
    # arr.append(unit)
    return list_of_units, arr


def conversion(list_of_units, arr):
    length = float(input("Length: "))
    unit = input('Unit: ').lower()
    if unit not in list_of_units.keys():
        print("Invalid Unit.")
        return
    print([x for x in arr][:len(arr)])
    targeted_unit = str(input('Targeted Unit: '))
    if targeted_unit not in list_of_units.keys():
        print("Invalid Unit")
        return
    else:
        print(float(length)*list_of_units[targeted_unit])


if __name__ == '__main__':
    n = int(input(
        'Press 1 : For Conversion.\nPress 2 : For For adding a unit.\nPress 3 : To Exit.\n'))
    list_of_units = {'metres': 1, 'yard': 1.094,
                     'inches': 2.54, 'feet': 2.80840, 'kilometre': 0.001}
    arr = ['metres', 'yard', 'inches', 'feet', 'kilometre']

    if(n == 1):
        conversion(list_of_units, arr)

    elif (n == 2):
        add_unit(list_of_units, arr)
    else:
        exit
