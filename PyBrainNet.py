"""
#Captain's MODE neural network
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader

ds = SupervisedDataSet(112, 1)
n = FeedForwardNetwork()
n = buildNetwork(112, 10, 2, 1)


inLayer = LinearLayer(112)
hiddenLayer = SigmoidLayer(10)
outLayer = LinearLayer(1)

n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)

in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)

n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)
n.sortModules()
"""




#make dataset from file
line_counter = 0
with open('DOTA_parsed.txt', 'r') as file:
    add_counter = 0

    for line in file:
        if line_counter < 2240:
            # Создать массив с героями (0 и 1) для ID
            list_of_hero_ids = list()
            for i in range(112):
                list_of_hero_ids.append(0)
            items = line.split(',')

            #game mode
            if int(items[1]) == 22:
                line_counter += 1
                for each in items[3:12]:

                    if int(each) == 24:
                        print('ERROR')
                        print('Mistake in match ID: ', items[0])
                        break
                    elif int(each) < 24:
                        list_of_hero_ids[int(each) - 1] = 1
                    elif int(each) > 24:
                        list_of_hero_ids[int(each) - 2] = 1
                    """
                    if int(each) == 24 or int(each) == 24 or int(each) == 113:
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

            # Бинарный список героев          маркер победы
                ds.addSample(list_of_hero_ids, (items[13]))
                add_counter = add_counter+1
                list_of_hero_ids.clear()
                print('added matches: ', add_counter)

trainer = BackpropTrainer(n, ds)
while True:
    print('More? Y/n')
    input1 = input()
    if input1 == 'y':
        for i in range(500):
            print(trainer.train())
    NetworkWriter.writeToFile(n, 'filename.xml')
#ds.clear()
#"""