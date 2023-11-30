'''
A program that generates 3 random numbers within the user defined range
Constraints: define the RandomNumbers class, which has three integer attributes: var1, var2, and var3.
Write getter method for each attribute: get_var1(), get_var2() and get_var3().
Then write the following 2 instance methods:
    set_random_values( ) - accepts a low and high integer values as parameters, and sets var1, var2, and var3 to random numbers within the range of the low and high input values (inclusive).
    get_random_values( ) - prints out the 3 random numbers in the format: "Random values: var1 var2 var3"
'''

import random

class RandomNumbers:
    # constructor
    def __init__(self):
        self.var1 = 0
        self.var2 = 0
        self.var3 = 0

    # getters
    def get_var1(self):
        return self.var1

    def get_var2(self):
        return self.var2

    def get_var3(self):
        return self.var3

    def get_random_values(self):
        print(f"Random values: {self.var1} {self.var2} {self.var3}")

    # setter
    def set_random_values(self, low, high):
        # generates 3 random values in specified range (inclusive)
        self.var1 = random.randint(low, high)
        self.var2 = random.randint(low, high)
        self.var3 = random.randint(low, high)
    

def main():
    random_instance = RandomNumbers()

    # get user defined input range
    low_value = int(input("Enter the number for the lowest input range: "))
    high_value = int(input("Enter the number for the highest input range: "))

    #invalid high value handling
    while high_value < low_value:
        print("Please enter a number higher than the lowest input range")
        high_value = int(input("Enter the number for the highest input range: "))

    # set and output random values
    random_instance.set_random_values(low_value, high_value)
    random_instance.get_random_values()

if __name__ == "__main__":
    main()
