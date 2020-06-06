from tqdm import tqdm
import random
import time
import numpy as np

class train():
    def __init__(self, number_of_train, b, target, xs : list, alpha = -0.000000001, ws = []):
        self.number_of_train = number_of_train
        self.b = b
        self.target = target
        self.ws = ws
        self.xs = xs
        self.alpha = alpha
        self.ws = ws
    
    def sigmoid(self):
        1/(1+np.exp(-self.x))

    def defaultws(self):
        for item in range(len(self.xs)): 
            self.ws.append(random.random())
        return self.ws

    def model(self):
        predictions = []
        _sum = 0
        for w in ws:  
            for x in xs:
                predictions.append(wheigt * x + b)
        
        for time in range(len(predictions)):
            _sum += predictions[time]
        return self.sigmoid(_sum)

    def cost(self):
        return (self.model() - self.target) ** 2

    def slope(self):
        return 2 * (self.model()-self.target)

    def aproximate_slope(self):
        h = 0.0000001
        return (self.cost(self.b + h, 4) - self.cost(self.b, 4)) / h

    def dcdw(self, w):
        dcdwl = []
        for function in range(int(len(self.ws))):
            dcdwl.append(2 * (w * self.xs[function] + self.b - self.target) * function)
        _sum = 0
        for item in dcdwl:
            _sum += item
        return _sum
    
    def dcdb(self, w):
        dcdbl = []
        for function in range(int(len(self.ws))):
            dcdbl.append(2 * (w * self.xs[function] + self.b - self.target))
        _sum = 0
        for item in dcdbl:
            _sum += item
        return _sum

    def train(self):
        
        global b
        print(self.b)
        print(self.ws)
        print(self.target)
        steta = st = time.time()
        with tqdm(total=self.number_of_train) as pbar:
            for train in range(self.number_of_train):
                for w in range(len(self.ws)):
                    self.ws[w] = self.ws[w] + self.alpha * self.dcdw(w)
                    self.b = self.b + self.alpha * self.dcdb(w)
                pbar.update(1)
        ft = time.time()
        tt = float(ft) - float(st)
        print("weights: " + str(self.ws))
        print("bios: " + str(self.b))
        print("time took to train: " + str(tt))
        open("./parameters.txt", "w+").write("bios: " + str(self.b) + "\nweights: " + str(self.ws) + "\ntime took to train: " + str(tt))

class use():
    def __init__(self, bios, inputs, weights):
        self.bios = bios
        self.inputs = inputs
        self.weights = weights

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def predict(self):
        predictions = []
        sums = 0
        for weight in range(len(self.weights)):
            predictions.append(self.weights[weight] * self.inputs[weight] + self.bios)
        for predictionnum in range(len(predictions)):
            sums += predictions[predictionnum]
        return self.sigmoid(sums)
