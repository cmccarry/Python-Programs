'''
A program that reads four integers and:
    prints “two pairs” if the input consists of two matching pairs (in some order)  
    print “not two pairs” otherwise.
'''

int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))
int3 = int(input("Enter the third integer: "))
int4 = int(input("Enter the fourth integer: "))
myArray = [int1, int2, int3, int4]
pairCounter = 0
myDict = dict()

for element in myArray:
    myDict[element] = myDict.get(element, 0) + 1
print(myDict)

for value in myDict.values():
    if value > 1:
        pairCounter += 1
    if value == 4:
        pairCounter += 1

if pairCounter == 2:
    print (int1 , int2 , int3 , int4 , "two pairs")
else:
    print (int1 , int2 , int3 , int4 , "not two pairs")

#first attempt
'''
if int1 == int2 or int1 == int3 or int1 == int4:
    pairCounter = pairCounter+1
if int2 == int3 or int2 == int4:
    pairCounter = pairCounter+1
if int3 == int4:
    pairCounter = pairCounter+1
if int1 == int2 and int3 and int4:
    pairCounter = pairCounter-1
if pairCounter == 2:
    print (int1 , int2 , int3 , int4 , "two pairs")
else:
    print (int1 , int2 , int3 , int4 , "not two pairs")
    '''