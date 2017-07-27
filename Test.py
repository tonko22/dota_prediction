import json
import numpy as np



array_of_names = list()
for i in range(110):
    array_of_names.append('{0}'.format(i))
print(array_of_names)

with open('D:/Python/Lib/site-packages/dota2api/ref/heroes.json') as heroes_json:
    heroes = json.load(heroes_json)
    with open('DOTA_heroes.txt', 'r') as file:
        i=0
        for hero in heroes['heroes']:
            id = int(hero['id'])
            if id < 24:
                array_of_names[i] = hero['localized_name']
                i += 1
            elif id > 24 and id < 108:
                array_of_names[i] = hero['localized_name']
                i += 1
            elif id > 108 and id < 113:
                array_of_names[i] = hero['localized_name']
                i += 1
i = 0
for each in array_of_names:
    print(i, each)
    i += 1

#"""

