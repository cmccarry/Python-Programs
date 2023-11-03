costNew = int(input("The cost of the hyrbid car: $"))
car = input("Enter the year, make, and model of the hybrid car: ")
MILES_PER_YEAR = 15000 #The estimated miles driven per year will be 15000
GAS_PRICE = 5.43 #The estimated gas price in California is $5.43
mpg = int(input("The efficiency in miles per gallon: "))
resaleValue = costNew * 0.6 #Estimated car value after 5 years is 60% of initial cost
totalCost = round(costNew + (MILES_PER_YEAR * GAS_PRICE // mpg * 5) - resaleValue)
print ("The total cost of owning a " + str(car) + " for five years: $" + str(totalCost))