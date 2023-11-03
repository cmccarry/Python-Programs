time1 = int(input("Please enter the first time: "))
time2 = int(input("Please enter the second time: "))
difference = abs(time1-time2)
hour = difference // 100
minute = difference % 100
print ("The time between the two times is " , hour , " hours " , minute , " minutes")