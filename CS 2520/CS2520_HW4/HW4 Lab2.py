def reverse(myArray):
    reversedArray = []
    for element in myArray:
        if element[-1] == '\n':
            reversedArray.insert(0,element[0:-1])
        else:
            reversedArray.insert(0,element)
    return reversedArray

def main():
    with open('input.txt','r') as file:
        reversedInput = reverse(file.readlines())
    with open('output.txt','w') as file:
        for line in reversedInput:
            if reversedInput.index(line) == len(reversedInput)-1:
                file.write(line)
            else:
                file.write(line+'\n')
    with open('output.txt','r') as file:
        print(file.read())

main()