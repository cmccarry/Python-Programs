'''
Prompts the user for two integers and then prints
⦁	The sum
⦁	The difference
⦁	The product
⦁	The average
⦁	The distance (absolute value of the difference)
⦁	The maximum (the larger of the two)
⦁	The minimum (the smaller of the two)

'''

int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))
sum = int1 + int2
difference = int1 - int2
product = int1 * int2
average = (int1 + int2) // 2
distance = abs(difference)
maximum = max(int1, int2)
minimum = min(int1, int2)
print ("sum: " , sum)
print ("difference: " , difference)
print ("product: " , product)
print ("average: " , average)
print ("distance: " , distance)
print ("maximum: " , maximum)
print ("minimum: " , minimum)