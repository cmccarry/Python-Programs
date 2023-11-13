'''
Converts a positive integer into the Roman number system
'''

num = int(input("Enter an integer between 1 and 3999: "))
romanNumeral = ''
i = 0
value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbol = ['M', 'CM', 'D', 'CD', 'C', 'CX', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

#finds the largest number where: integer-largest number >= 0
#adds the corresponding roman numeral to a string
#subtract the number from the integer
#loops until the integer is 0
while num > 0:
    for i in range(0,13):
        if num - value[i] >= 0:
            romanNumeral += symbol[i]
            num -= value[i]
            break
print(romanNumeral)