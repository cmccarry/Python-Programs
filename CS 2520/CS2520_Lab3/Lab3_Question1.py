'''
Has a function: scramble(word), that constructs a scrambled version of a given word, randomly flipping two characters other than the first and last one. 
A program that reads words and prints the scrambled words
'''

import random
def main():
    phrase = input('Enter a phrase: ')
    newPhrase = scramble(phrase)
    print(f'Your new phrase is: {newPhrase}')

def scramble(toChange):
    words = toChange.split()
    change = ''
    for i in range(len(words)): #goes through each word of the entered phrase
        currWord = words[i]
        length = len(currWord)
        if length >= 4:
            bank = []
            for k in range(length): #makes a list of all letters in the current word so letters aren't used twice
                bank += (currWord[k])
            for j in range(1,length+1):
                location = j
                if location == 1: #keeps first letter
                    change += currWord[location-1]
                    bank.remove(currWord[location-1])
                elif location == length: #keeps last letter
                    change += currWord[location-1]
                    bank.remove(currWord[location-1])
                else: #scrambles all letters in the middle
                    digit = random.randint(1,len(bank)-1)
                    change += bank[digit-1]
                    bank.remove(bank[digit-1])
        else: #add whole word of the phrase to the changed phrase if theres 3 or less characters
            change += currWord
        change += ' '
    return change

main()