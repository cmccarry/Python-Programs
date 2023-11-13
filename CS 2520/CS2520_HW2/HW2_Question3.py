'''
reads two times in military format, ex:(0900, 1730)
prints the number of hours and minutes between the two times
'''

time1 = int(input("Please enter the first time: "))
time2 = int(input("Please enter the second time: "))
difference = abs(time1-time2)
print(difference)
hour = str(difference)[:-2] or 0
minute = str(difference)[-2:] or 0
print (f"The time between the two times is {hour} hours {minute} minutes")