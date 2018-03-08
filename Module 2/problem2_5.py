import random

def problem2_5():
    """ Simulates rolling a die 10 times."""
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(171)  # don't remove when you submit for grading
    number = []
    for x in range(10):
        number.append(random.randint(1,6))
    # print (number)
    for num in number:
        print (num)
