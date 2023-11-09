import random

for j in range(10):
    fullList = [1,2,3,4,5,6,7,8,9,10]
    permutation = []
    for i in range(10):
        position = random.randint(0,len(fullList)-1)
        permutation.append(fullList.pop(position))
    print(permutation)