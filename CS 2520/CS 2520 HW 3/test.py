'''int1 = int(input("Enter the first integer: "))
int2 = int(input("Enter the second integer: "))
int3 = int(input("Enter the third integer: "))
int4 = int(input("Enter the fourth integer: "))
pairCounter = 0
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
    print (int1 , int2 , int3 , int4 , "not two pairs")'''

for i in range(10):
    print(i)
    for j in range(15):
        print(j,end='')
    print()