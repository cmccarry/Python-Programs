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