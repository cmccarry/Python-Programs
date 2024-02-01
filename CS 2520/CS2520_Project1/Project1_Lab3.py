import random

# function to get a valid user choice
def getValidGuess(validChoices):
    user_guess = 0
    while user_guess not in validChoices:
        try:
            user_guess = input('Enter your guess (or q to exit): ')
            user_guess = int(user_guess)
            if user_guess > 100 or user_guess < 1:
                print('Please only enter a number from 1 to 100 or q')

        # if user_guess can't be converted to an integer
        except ValueError:
            if user_guess == 'q':
                print('Have a good day.')
                exit()
            print('Please only enter an integer number from 1 to 100 or q')
    return user_guess

# function to play the guessing game
def guessingGame():
    '''validity is checked by the guess being an integer and between 1 and 100
    loops user inputs until the random number is guessed'''
    validChoices = []
    for i in range(1,101):
        validChoices.append(i)
        validChoices.append(str(i))
    option = input(f'Would you like to play a guessing game: guessing a number from 1-100? (y/n): ')
    while option != 'n':
        random_number = random.randint(1, 100)
        user_guess = 0
        guesses = 0
        while True:
            user_guess = getValidGuess(validChoices)
            guesses += 1
            if user_guess < random_number:
                print('That guess was too low, try again \n')
            elif user_guess > random_number:
                print('That guess was too high, try again \n')
            else:
                print(f'Congratulations! You guessed the number: {random_number} \
                      \non guess number {guesses}')
                break
        option = input('Would you like to keep playing? (y/n): ')
    print('Thank you! Have a good day.')

guessingGame()
