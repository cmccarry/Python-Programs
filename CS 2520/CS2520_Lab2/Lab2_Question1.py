'''
Given a line of text as input, outputs:
    the number of characters excluding spaces, periods, exclamation points, or commas
'''

user_input = str(input('Enter a string: '))
length = len(user_input)
for i in range(length):
    if user_input[i] in ' .!,':
        length -= 1
print(length)