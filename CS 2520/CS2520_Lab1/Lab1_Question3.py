'''
A program that takes a date as input and outputs the date's season in the northern hemisphere. 
The input is a string to represent the month and an int to represent the day
'''

month = str(input("Enter the month: "))
date = int(input("Enter the day: "))
month = month.lower()
monthList = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
if month in monthList:
    if month in monthList[1]:
        if date <= int(28):
            print("Winter")
        else:
            print("Invalid input")
    elif month in monthList[0] or month in monthList[2] or month in monthList[4] or month in monthList[6] or month in monthList[7] or month in monthList[9] or month in monthList[11]:
        if date <= int(31):
            if month in monthList[0]:
                print("Winter")
            if month in monthList[2]:
                if date >= int(20):
                    print("Spring")
                else:
                    print("Winter")
            if month in monthList[4]:
                print("Spring")
            if month in monthList[6]:
                print("Summer")
            if month in monthList[7]:
                print("Summer")
            if month in monthList[9]:
                print("Autumn")
            if month in monthList[11]:
                if date >= int(21):
                    print("Winter")
                else:
                    print("Autumn")
        else:
            print("Invalid input")
    elif month in monthList[3] or month in monthList[5] or month in monthList[8] or month in monthList[10]:
        if date <= int(30):
            if month in monthList[3]:
                print("Spring")
            if month in monthList[5]:
                if date >= int(21):
                    print("Summer")
                else:
                    print("Spring")
            if month in monthList[8]:
                if date >= int(22):
                    print("Autumn")
                else:
                    print("Summer")
            if month in monthList[10]:
                print("Autumn")
        else:
            print("Invalid input")
else:
    print("Invalid input")