from tqdm import tqdm
import random
import time

class train():
    def __init__(self, number_of_train, b, target, xs : list, alpha = -0.000000001, ws = []):
        self.number_of_train = number_of_train
        self.b = b
        self.target = target
        self.ws = ws
        self.xs = xs
        self.alpha = alpha
        self.ws = ws
    
    def defaultws(self):
        for item in range(len(self.xs)): 
            self.ws.append(random.random())
        return self.ws

    def model(self):
        for w in ws:
            for x in xs:
                return wheigt * x + b

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
        sum = 0
        for item in dcdwl:
            sum += item
        return sum
    
    def dcdb(self, w):
        dcdbl = []
        for function in range(int(len(self.ws))):
            dcdbl.append(2 * (w * self.xs[function] + self.b - self.target))
        sum = 0
        for item in dcdbl:
            sum += item
        return sum
    def train(self):
        
        global b
        print(self.b)
        print(self.ws)
        print(self.target)
        n = 0
        steta = st = time.time()
        with tqdm(total=self.number_of_train) as pbar:
            for train in range(self.number_of_train):
                for w in range(len(self.ws)):
                    self.ws[w] = self.ws[w] + self.alpha * self.dcdw(w)
                    self.b = self.b + self.alpha * self.dcdb(w)
                pbar.update(1)
        ft = time.time()
        tt = float(ft) - float(st)
        print("wheights: " + str(self.ws))
        print("bios: " + str(self.b))
        print("time took to train: " + str(tt))
        open("./parameters.txt", "w+").write("bios: " + str(self.b) + "\nwheights: " + str(self.ws) + "\ntime took to train: " + str(tt))
