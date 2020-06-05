from lib import train
test = train(number_of_train = 40000000, b = 0, target = 498.0034275470891, xs = [3.6, 8, 4])
test.ws = test.defaultws()
test.train()
