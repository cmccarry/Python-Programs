firstInput = str(input("Enter a string: "))
secondInput = str(input("Enter a string: "))
thirdInput = str(input("Enter a string: "))
aList = [firstInput , secondInput , thirdInput]
aList = sorted(aList)
print(f'{aList[0]} \n{aList[1]} \n{aList[2]}')