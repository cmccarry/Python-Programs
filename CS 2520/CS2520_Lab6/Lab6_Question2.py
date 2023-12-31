'''
Prompt: Implement a class ComboLock that works like the combination lock in a gym locker,
    The lock is constructed with a combination—three numbers between 0 and 39. 
    The reset method resets the dial so that it points to 0.
    The turnLeft and turnRight methods turn the dial by a given number of ticks to the left or right. 
    The open method attempts to open the lock. 
    The lock opens if 
        the user first turned it right to the first number in the combination, 
        then left to the second,
        and then right to the third.
'''

class ComboLock :
    def __init__(self):
        self.combination = dict()
        self.tries = ComboLock.reset(self)

    def ComboLock(self, secret1, secret2, secret3):
        if 0 > secret1 or secret1 > 39 or 0 > secret2 or secret2 > 39 or 0 > secret3 or secret3 > 39:
            print('Invalid combination. Only use numbers from 0-39')
            exit()
        self.combination['combo1'] = secret1
        self.combination['combo2'] = secret2
        self.combination['combo3'] = secret3

    def reset(self):
        return 0

    def turnLeft(self, ticks):
        self.tries += 1
        if self.tries != 2:
            print(f"combination failed")
            exit()
        
        self.combination['combo2'] -= ticks

    def turnRight(self, ticks):
        self.tries += 1
        if self.tries != 1 and self.tries != 3:
            print(f"combination failed")
            exit()
        
        if self.tries == 1:
            self.combination['combo1'] -= ticks
        else:
            self.combination['combo3'] -= ticks

    def open(self) -> bool:
        for value in self.combination.values():
            if value != 0:
                return False
        return True

lock = ComboLock()
lock.reset()
lock.ComboLock(12, 4, 30)
lock.turnRight(12)
lock.turnLeft(4)
lock.turnRight(30)

if lock.open():
    print(f"lock successfully opened")
else:
    print(f"lock failed to open")