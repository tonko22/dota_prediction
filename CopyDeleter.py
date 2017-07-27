import numpy as np


counter = 0
array_of_ids = list()

#split lines and stote ids to array
with open('DOTA_parsed.txt', 'r') as file:
    for line in file:
        items = line.split(',')
        array_of_ids.append(items[0])

copy = 0
len_ids = len(array_of_ids)

#check for copies
list_of_copies = list()
for i in range(len_ids-1):
    for j in range(i+1, len_ids):
        if array_of_ids[i] == array_of_ids[j]:
            copy = copy +1
            list_of_copies.append(j)
            #print(i, j)

#print(list_of_copies)
print('Number of matches', len_ids)
print('Number of copies', copy)

"""
with open('DOTA_parsed.txt', 'r+') as f:
    with open('DOTA_parsed.txt', 'w+') as f2:
        d = f.readlines()
        #print(len(d))
        for i in range(len(d)):
            copy_counter = 0
            for each in list_of_copies:
                if i == each:
                    copy_counter = copy_counter +1
                    #print(i,each)
            if copy_counter == 0:
                f2.write(d[i])

#print(copy_counter)
"""