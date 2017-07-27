import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.neural_network import MLPClassifier
import numpy as np
import matplotlib as plt


number_of_heroes = 112
number_of_matches = 25000
# Input data
dota_X_train = np.arange(number_of_heroes).reshape(number_of_heroes, 1)
# Output data
dota_Y_train = np.zeros((1, 1))
print(dota_Y_train)

#Make dataset from file
with open('DOTA_parsed.txt', 'r') as file:
    append_counter = 0
    line_counter = 0
    for line in file:

        if line_counter < number_of_matches:
            items = line.split(',')
            # Create array of zeros with (number of heroes)x1 size
            list_of_hero_ids = np.zeros((number_of_heroes, 1))

            #Game mode 22 only
            if int(items[1]) == 22:
                line_counter += 1

                if int(items[13]) == 0:
                    win_marker = -1
                else:
                    win_marker = 1

                for each in items[2:12]:
                    #Hero ID cannot be 24
                    if int(each) == 24:
                        print('ERROR')
                        print('Mistake in match ID: ', items[0])
                        break

                    elif int(each) < 24:
                        list_of_hero_ids[int(each) - 1] = 1

                    elif int(each) > 24:
                        list_of_hero_ids[int(each) - 2] = 1

                #Make zeros = -1
                for x in range(len(list_of_hero_ids)):
                    if list_of_hero_ids[x] == 0:
                        list_of_hero_ids[x] = (-1)

                    """
                    # GAME MODE 2
                    if int(each) == 24 or int(each) == 108 or int(each) == 113:
                        print('ERROR')
                        print('ERROR')
                        print('ERROR')
                        print('Mistake in match ID: ', items[0])
                        break
                    elif int(each) < 24:
                        list_of_hero_ids[int(each) - 1] = 1

                    elif int(each) > 24 and int(each) < 108:
                        list_of_hero_ids[int(each) - 2] = 1
                    elif int(each) > 108 and int(each) < 113:
                        list_of_hero_ids[int(each) - 3] = 1
                    """

                # Add Binary heros list to dataset
                dota_X_train = np.append(dota_X_train, list_of_hero_ids, axis=1)
                # Add win marker to dataset
                dota_Y_train = np.append(dota_Y_train, win_marker, axis=1)
                append_counter = append_counter + 1
                list_of_hero_ids.fill(0)
                win_marker = None

# Допилить ТЕСТОВЫЕ СЕТЫ
dota_X_test = 0
dota_Y_test = 0

# Bias array
hat = np.ones((1, number_of_matches), dtype=np.int)

dota_X_train = dota_X_train[..., 1:]

dota_X_train = np.concatenate((hat, dota_X_train), axis=0)
print('Dataset ready')



mlp = MLPClassifier(solver='adam', activation='tanh', alpha=1e-5, hidden_layer_sizes=(224,10), max_iter=400)
mlp.fit(dota_X_train, dota_Y_train)
print("Training set score: %f" % mlp.score(dota_X_train, dota_Y_train))
print("Test set score: %f" % mlp.score(dota_X_test, dota_Y_test))