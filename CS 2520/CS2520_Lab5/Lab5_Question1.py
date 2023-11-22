'''
list functions that carry out specific tasks for a list of integers
'''

original = [1,4,7,9,8,2,21,39]
print(f'Original List : {original}')


#a. Swap the first and last elements in the list.
def partA():
    listA = original[1:-1]
    listAFirst = original[0]
    listALast = original[-1]
    listA.insert(0,listALast)
    listA.append(listAFirst)
    print(listA,'part A')


#b. Shift all elements by one to the right and move the last element into the first position. For example, 1 4 9 16 25 would be transformed into 25 1 4 9 16.
def partB():
    listB = list(original)
    listB.insert(0,original[-1])
    del listB[-1]
    print(listB,'part B')


#c. Replace all even elements with 0.
def partC():
    listC = list(original)
    j = -1
    for i in listC:
        j += 1
        if i % 2 == 0:
            listC[j] = 0
    print(listC,'part C')


#d. Replace each element except the first and last by the larger of its two neighbors.
def partD():
    listD = list(original)
    for i in range(len(listD)):
        if i != 0 and i != len(listD)-1:
            if listD[i] < listD[i-1]:
                listD[i] = listD[i-1]
            if listD[i] < listD[i+1]:
                listD[i] = listD[i+1]
    print(listD,'part D')


#e. Remove the middle element if the list length is odd, or the middle two elements if the length is even.
def partE():
    listE = list(original)
    listLength = len(original)
    half = listLength // 2
    if listLength % 2 != 0:
        del listE[half]
    if listLength % 2 == 0:
        del listE[half-1]
        del listE[half-1]
    print(listE,'part E')


#f. Move all even elements to the front, otherwise preserving the order of the elements.
def partF():
    listF = list(original)
    j = -1
    for i in listF:
        j += 1
        if i % 2 == 0:
            listF.insert(0,i)
            del listF[j+1]
    print(listF,'part F')


#g. Return the second-largest element in the list.
def partG():
    listG = list(original)
    listG.remove(max(listG))
    print(max(listG),'part G')


#h. Return true if the list is currently sorted in increasing order.
def partH():
    listH = list(original)
    allSorted = False
    listH.sort()
    if listH == original:
        allSorted = True
    print(allSorted,'part H')


#i. Return true if the list contains two adjacent duplicate elements.
def partI():
    listI = list(original)
    adjacent = False
    j = -1
    for i in listI:
        j += 1
        if j == 0:
            if i == listI[j+1]:
                adjacent = True
        if j == len(listI)-1:
            if i == listI[j-1]:
                adjacent = True
        elif i == listI[j+1] or i == listI[j-1]:
            adjacent = True
    print(adjacent,'part I')


#j. Return true if the list contains duplicate elements (which need not be adjacent).
def partJ():
    listJ = list(original)
    adjacent = False
    for i in listJ:
        checkListJ = list(listJ)
        checkListJ.remove(i)
        if i in checkListJ:
            adjacent = True
    print(adjacent,'part J')


def main():
    partA(),partB(),partC(),partD(),partE(),partF(),partG(),partH(),partI(),partJ()

main()