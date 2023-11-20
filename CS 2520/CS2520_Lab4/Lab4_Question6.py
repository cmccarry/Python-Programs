'''
Defines a function named coin_flip that returns "Heads" or "Tails" according to a random value 1 or 0.
Assume the value 1 represents "Heads" and 0 represents "Tails".
Has a main program that:
    reads the desired number of coin flips as an input
    calls function coin_flip() repeatedly according to the number of coin flips
    outputs the results.
Assumes the input is a value greater than 0.
'''

import random
random.seed(14)

def coin_flip():
    x = random.randint(0,1)
    if x == 0:
        return 'Tails'
    if x == 1:
        return 'Heads'

def main():
    flips = int(input('Desired number of coin flips: '))
    for i in range(flips):
        print(coin_flip())

main()