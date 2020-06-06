from pysnn import train
test = train(number_of_train = 500000000, b = 0, target = 0.4980034275470891, xs = [3.6, 8, 4])
test.ws = test.defaultws()
test.train()