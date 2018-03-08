import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    number = []
    for x in range(10):
        number.append((random.random() * 5) + 30)
    print (number)

