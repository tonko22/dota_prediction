from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet


net = buildNetwork(110, 1, 1)
net.activate([110, 1])