def powerNum(integer,power):
    if power == 0:
        return 1
    return integer * powerNum(integer,power-1)

def main():
    x = int(input('Integer number: '))
    y = int(input('To the power of: '))
    print(powerNum(x,y))

main()