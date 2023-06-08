# Задача №1

from pprint import pprint


with open('recipes.txt', 'rt') as file:
    cook_book = {}
    for line in file:
        name_dish = line.strip()
        ingredients_count = int(file.readline())
        ingredients_list = []
        for i in range(ingredients_count):
            ing = file.readline()
            ingredient_name, quantity, measure = ing.strip().split(' | ')
            ingredients_dict = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredients_list.append(ingredients_dict)
        file.readline()
        cook_book[name_dish] = ingredients_list
    pprint(cook_book, sort_dicts=False)

print()
# Задача №2
print()
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        recipe = cook_book[dish]
        for ing in recipe:
            key = ing['ingredient_name']
            if key not in shop_list:
                new_dict = {
                    'measure': ing['measure'],
                    'quantity': int(ing['quantity']) * person_count
                }
                shop_list[key] = new_dict
            else:
                shop_list[key]['quantity'] += int(ing['quantity']) * person_count

    pprint(shop_list, sort_dicts=False)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)

# Задача №3

import os


current = os.getcwd()
folder = 'sorted'
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
file_name_4 = 'new.txt'

with open(os.path.join(current, folder, file_name_1)) as file1, open(os.path.join(current, folder, file_name_2)) as file2, open(os.path.join(current, folder, file_name_3)) as file3, open(os.path.join(current, folder, file_name_4), 'w') as new_file:
    dict_file = {
        file1: [len(file1.readlines()), file_name_1],
        file2: [len(file2.readlines()), file_name_2],
        file3: [len(file3.readlines()), file_name_3]
    }

    dict_file_sort = dict(sorted(dict_file.items(), key=lambda item: item[1][0]))
    # pprint(dict_file_sort, sort_dicts=False)
    file1.seek(0)
    file2.seek(0)
    file3.seek(0)

    for keys, values in dict_file_sort.items():
        new_file.writelines(f'{values[1]}\n')
        new_file.writelines(f'{values[0]}\n')
        for line in keys.readlines():
            new_file.writelines(f'{line}')
        new_file.writelines('\n')




