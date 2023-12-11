import random, math
'''
text = "python program"
N = len(text)
print(N)
num = int("45")*float("1.5")
print(num)
destination = "Eiffel Tower"
print(destination[0] + " " + destination[7])
print("He said \"Hello\"") 
'''

'''
import math
x = float(input("enter the first integer: "))
y = float(input("enter the second integer: "))
z = float(input("enter the third integer: "))
print(f'{x**z:.2f} \n{x**(y**z):.2f} \n{abs(x-y):.2f} \n{math.sqrt(x**z):.2f}')
'''

'''
HOTEL_RATE = 150
numYear = int(input("Enter the years married: "))
if numYear == 50:
    print("Congratulations on your 50 years of marriage")
    HOTEL_RATE = HOTEL_RATE/2
print(f'Your hotel rate is: ${HOTEL_RATE:.2f}')
'''

'''
NUM_EGGS = 6
if NUM_EGGS <= 6:
    print('b')
else:
    print('d')
print('g')
'''

'''
x = float(input('Enter the first number: '))
y = float(input('Enter the second number: '))
if x == 0.0 and y == 0.0:
    print('Both of the two integers are zero')
else:
    if x == 0.0 or y == 0.0:
        print('One of the two integers is zero')
    if x != 0.0 and y != 0.0:
        print('Neither of the two integers is zero')
'''

'''
phrase1 = str(input('Enter the first phrase: '))
phrase2 = str(input('Enter the second phrase: '))
if phrase1 == phrase2:
    print('Both phrases match')
elif phrase1 in phrase2:
    print(f'{phrase1} is found within {phrase2}')
elif phrase2 in phrase1:
    print(f'{phrase2} is found within {phrase1}')
else:
    print('No matches')
'''

'''
phr1 = abs(int(input('Enter the first integer: ')))
phr2 = abs(int(input('Enter the second integer: ')))
phr3 = abs(int(input('Enter the third integer: ')))
phr4 = abs(int(input('Enter the fourth integer: ')))
oddCounter = 0
if phr1 % 2 == 1:
    oddCounter += 1
if phr2 % 2 == 1:
    oddCounter += 1
if phr3 % 2 == 1:
    oddCounter += 1
if phr4 % 2 == 1:
    oddCounter += 1
print(oddCounter)
'''

'''
i = 0
total = 0
while total <= 10:
    i = i+1
    total = total+i
    print(i,total)
'''

'''
import random
print('Tell me something about yourself. ')
print('You can type "\goodbye\" anytime to quit. ')
user_text = input()
while user_text != "goodbye":
    random_num = random.randint(0 , 2)
    if random_num == 0:
        print("\nplease explain further")
    elif random_num == 1:
        print(f'\nWhy do you say {user_text}?')
    else:
        print('Something went wrong try again.')
    user_text = input()
print('It was nice talking to you today.')
'''

'''
end = 101
i = 0
sum = 0
while i != end:
    sum = sum+i
    i += 1
print(sum)
'''

'''
integer = int(input('Enter the integer you want converted to binary: '))
binary = ""

while integer > 0:
    binary += str(integer % 2)
    integer = integer // 2
print(binary)
'''

'''
import random
bid = str(input("Place a bid? (y/n): "))
amount = 0
while bid != 'n':
    amount = amount + random.randint(1,10)
    print(f"I'll bid ${amount}! ")
    bid = str(input("Keep bidding? (y/n): "))
print("No more bids")
'''

'''
sum = 0
value = 0
while value != -1 :
    value = int(input("Enter a value: "))
    sum = sum + value
    print(sum)
print(sum)
'''

'''
i = 0
stateName = 'California'
while i < len(stateName):
    letter = stateName[i]
    print(letter)
    i = i+1

for letter in stateName:
    print(letter)

#from index 1 to 10 every 2 = output of 1 3 5 7 9
for i in range(1,10,2):
    print(i)

i = 1
while i < 10:
    print(i)
    i = i+1

#use end='' to print on the same line
for i in range(4):
    print(3-i, end = '')
print('')

name = 'Fred'
for i in range(len(name)-1,-1,-1):
    print(name[i],end='')
print('')

for i in range(3,0,-1):
    print(i)
'''

'''
for i in range(10,-1,-1):
    print(str(i)+'...',end='')
print('Liftoff')
'''

'''
print('Two letter domain name: ')
letter1 = 'a'
letter2 = 'b'
while letter1 <= 'z':
    letter2 = 'a'
    while letter2 <= 'z':
        print(f'{letter1}{letter2}.com')
        letter1 = chr(ord(letter2)+1)
    letter1 = chr(ord(letter1)+1)
'''

'''
for i in range(3):
    for j in range(4):
        print('*',end='')
    print()
'''

'''
#checkerboard pattern
for i in range(3):
    for j in range(5):
        if i%2 == j%2:
            print('x',end='')
        else:
            print(' ',end='')
    print()
'''

'''
stop = int(input('enter an integer:  '))
result = 0
for n in range(10):
    result += n*3
    if result > stop:
        break
    print(n)
print(result)
for i in range(5):
    if i<10:
        continue
    print(i)
'''

'''
sum2 = lambda x,y:x+y
print(sum2(1,2))

def myFunction(n):
    return lambda a:a*n
myDouble = myFunction(2)
myTriple = myFunction(3)
print(myDouble(11))
print(myTriple(11))
'''

'''
def generatorName(n):
    value = 0
    while value < n:
        yield value
        value += 1
for value in generatorName(3):
    print(value)

generator = (i*i for i in range(5))
for i in generator:
    print(i)
'''

'''
l = float(input())
w = float(input())
h = float(input())

def area(l,w):
    return l*w

def calc_pyramid_volume(l,w,h):
    return area(l,w)*h/3

print(f'Pyamid volume is {calc_pyramid_volume(l,w,h):.2f}')
'''

'''
def countdown(count):
    if count == 0:
        print('GO!')
    else:
        print(str(count) + ' ',end='')
        countdown(count-1)
countdown(10)
'''

'''
#list manipulations
myList = ['apple','banana','cherry','apple','strawberry','melon']
for x in myList:
    if myList.count(x) > 1: #counts number of times the value is in the list
        myList.remove(x)
print(myList)
print(len(myList))
print(myList[0]) #returns first index
print(myList[-1]) #returns last index, -2 returns the second to last etc.
print(myList[1:4]) #returns indexes at 1,2,3 and stops before printing fourth

anyList = ['string',True,40,19.07] #lists can be any data type
print(anyList)

embedList = list(('watermelon','strawberry'))
print(embedList)
aList = list('123')
print(aList)

text = "hello world welcome to my crib"
newText = text.split() #splits words from string into list with own index, default seperator with space
print(newText)
text2 = "hello world, welcome to my, sick crib"
newText2 = text2.split(',') #splits string into list with a ',' as the seperator
print(newText2)

list1 = [1,2,3]+[4]
print(list1,'add')
list1[1] = 9 #changes second index to 9
print(list1,'change')
del list1[2] #removes third index
print(list1,'remove')
list1.remove(9) #removes 9 from the list
print(list1,'remove')
list2 = list1[:] #creates a reference copy of list1
print(list2,'copy')
list2 = list(list1) #creates full copy of list1
print(list2,'copy')
list2.append(29) #adds 29 to end of the list
print(list2,'append')
list2.extend([13,21]) #adds multiple entries to end of the list
print(list2,'extend')
list2.index(13) #returns index of the value
print(list2.index(13))
list2.insert(1,10) #adds 10 as the second entry after the first
print(list2,'insert')
list2.pop(0) #removes and returns first entry
print(list2,"pop")
list2.sort() #sorts the list
print(list2,'sort')
list2.reverse() #reverses the list
print(list2,'reverse')
print(all(list2),'all') #returns true if list has 0, false if not
print(max([1,2,3,5]),'max') #returns max value in list
print(min([1,2,3,5]),'min') #returns min value in list
print(any([0,2]),'any') #returns true if any element in list is true
print(sum([1,2,3,5]),'sum') #returms sum of values in list
#for my_variable in list_name:  <- iterates through entries of list2
'''

'''
#list comprehension
myList = [10,20,30]
listPlus5 = [(i+5)for i in myList] #adds 5 to every value in myList
print(listPlus5) 
list1 = [-1,0,1,2]
list2 = [number*3 for number in list1] #multiplies every value in list1 by 3
print(list2)

#enumerate function
x = ('apple','orange')
y = enumerate(x) #returns index of list values
print(list(y))
for item in enumerate(x):
    print(item)

#nested list manipulation
list3 = [[10,20],[30,40]]
print(f'First nested list: {list3[0]}')
print(f'Second nested list: {list3[1]}')
print(f'First value of first nested list: {list3[0][0]}')

tictac = [['X','O','X'],[' ','X',' '],['O','X','O']]
print(tictac[0][0],tictac[0][1],tictac[0][2])
print(tictac[1][0],tictac[1][1],tictac[1][2])
print(tictac[2][0],tictac[2][1],tictac[2][2])
for row in tictac:
    for cell in row:
        print(cell + ' ',end='') #nested for loop that does same as above
    print()
for rowIndex, row in enumerate(tictac):
    for columnIndex, item in enumerate(row):
        print(f'Tic Tac Toe[{rowIndex}][{columnIndex}] is {item}')
'''

'''
#read and write files
f= open('file.txt','r')
print(f.read())
f.close()
f = open('file.txt','w')
f.write('writing in a new string to text file \nnice')
f.write('\nnew line')
f.write(' : not  a new line')
f.close()
f = open('file.txt','r')
print(f.readlines()) #returns each line as an element in array
f.close()

element = ['mary had a little lamb\n']
for item in element:
    print(item[0:-1])
'''

'''
newFlower = input('flower:').split()
print(newFlower)
myArray = []
for flower in newFlower:
    myArray.append(list(flower))
print(myArray)
'''


'''
#sets and functions
num1 = set([1,2,3]) #has 1, 2, 3
num2 = {7,8,9}  #has 8, 7, 9
print(num1) #num1 is a set
print(num2) #num2 is also a set

firstName = ['Ava','Ron','Ron','Tom','Don']
nameSet = set(firstName)    #sets remove duplicate values
print(nameSet)

name1 = {'pedro','samantha','george'}
name2 = {'emily','shawn','timothy'}
name1.add('john')   #add 'john' to the set
name2.remove('timothy') #remove 'timothy' from the set
print(name1)
print(name2)
name2.clear()   #remove all elements from a set
print(name2)

mix = {'hello',4,1.3}   #sets can contain multiple variable types
print(mix)

emptySet = set()
print(type(emptySet))

company = {'honda','toyota'}
techCompany = {'tesla','apple','facebook'}
company.update(techCompany) #adds techCompany set contents to company set
print(company)

language = {'java','python','C++'}
print("initial set:",language)
for x in language:
    print(x)
print("length:",len(language))
value = language.discard('java')    #same as remove function but doesn't raise exception if 'java' is not in the set
print("new set:",language)

A = {1,2,3,4,5}
B = {4,5,6}
print('Union using |:', A|B)    #elements of A and B combined
print('Union using function:', A.union(B))  #elements of A and B combined
print('Intersection using &:', A&B) #element(s) present in A and B
print('Intersection using function:', A.intersection(B))    #element(s) present in A and B
print('Difference using -:',A-B)    #element(s) in C not present in D
print('Difference using function:',A.difference(B)) #element(s) in C not present in D
print('Symmetric difference using ^:', A^B) #elements in A and B without the elements present in both
print('Symmetric difference using function:', A.symmetric_difference(B))    #elements in A and B without the elements present in both

A.intersection_update(B)    #updates A to only elements present in A and B
print('elements present in A and B:',A)

E = {1,2,3}
F = {4,5,6}
G = {1,2,3,7,8,9}
print(E.isdisjoint(F))  #True is sets E and F don't contain any same elements, False if not
print(E.issubset(G))    #True is all elements in set E are in set G, False if not
print(E.issuperset(G))  #True if all elements of G are in E, False if not
print(G.issuperset(E))  #True if all elements of E are in G, False if not

#nameList = [input(),input(),input()]
#print(sorted(nameList)
'''

'''
class time:
    def __init__(self):
        self.hour = 0
        self.minute = 0

my_time = time()
my_time.hour = 7
my_time.minute = 8
print(my_time.hour)
print(my_time.minute)
my_time2 = time()
my_time2.hour = 12
my_time2.minute = 33
print(f"{my_time2.hour}:{my_time2.minute}")


class bankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    def __displayAccount__(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")

b = bankAccount(1234, 5000)
b.__displayAccount__()


class person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def _display(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")

p = person('Connor', 22)
p._display()


class coin:
    def __init__(self):
        self.side_up = "heads"
    def toss(self):
        if random.randint(0,1) == 0:
            self.side_up = "heads"
        else:
            self.side_up = "tails"
    def get_side_up(self):
        return self.side_up
    
def main():
    my_coin = coin()
    print(f"This side is facing up: {my_coin.get_side_up()}")
    print("I am tossing the coin...")
    my_coin.toss()
    print(f"This side is facing up: {my_coin.get_side_up()}")

main()
'''

'''string = input().split()
print(str(string))
string.remove('water')
string.remove('2')
print(string)'''

'''user_input = ['water','1','2']
wordString = ''
for word in user_input:
    print(word)
    wordString += word
    wordString += ', '
wordString.rstrip(' ')
print(wordString)'''

'''i1 = 1
while i1 < 19:
    i2 = 3
    while i2 <= 9:
        print(f'{i1}{i2}',end='')
        i2 = i2 + 3
    i1 = i1 + 10'''
    