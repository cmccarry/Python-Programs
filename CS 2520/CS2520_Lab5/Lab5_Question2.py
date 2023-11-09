import random

def doToss():
    dieTosses = []
    for i in range(20):
        dieTosses.append(random.randint(0,6))
    return dieTosses


def findRuns(x):
    dieTosses = x
    fullSet = []
    j = 0
    check = ''

    for i in dieTosses:
        current = str(i)
        j += 1
        if j == len(dieTosses):
            if i == dieTosses[-2]:
                fullSet.append(check)
            else:
                fullSet.append(current)
        elif i == dieTosses[j]:
            if check == '':
                check = current
            check = check + str(dieTosses[j])
        else:
            if check != '':
                fullSet.append(check)
            else:
                fullSet.append(current)
            check = ''
    return fullSet


def findLongestRun(x):
    max = 0
    theRun = ''
    L = 0

    for i in range(len(x)):
        if len(x[i]) > max:
            max = len(x[i])
            index = i

    if index == 0 and max == 1:
        for j in x:
            if len(j) > 1:
                for k in range(len(j)):
                    theRun += str(j[k]) + ' '
            else:
                theRun += str(j) + ' '
        print(f'Answer(No groups): {theRun}')
    
    else:
        for j in x:
            if j == x[index]:
                if L == 0:
                    theRun += '('
                    for k in range(len(j)):
                        if k == len(j)-1:
                            theRun += str(j[k])
                        else:
                            theRun += str(j[k]) + ' '
                    theRun += ') '
                    L += 1
            elif len(j) > 1:
                for k in range(len(j)):
                    theRun += str(j[k]) + ' '
            else:
                theRun += str(j) + ' '
        print(f'Answer: {theRun}')


def main():
    tossOutput = doToss()
    print(f'{tossOutput} sequence of 20 random die tosses')
    list = findRuns(tossOutput)
    print(f'{list} list with same numbers in sequence grouped together')
    findLongestRun(list)

main()