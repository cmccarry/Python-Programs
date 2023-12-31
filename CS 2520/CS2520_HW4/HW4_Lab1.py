'''
Reads a file containing two columns of floating-point numbers
Prompts the user for the file name
Prints the average of each column
'''

def readFile(filename):
    with open(filename, 'r') as file:
        column1 = []
        column2 = []
        for line in file:
            numbers = line.split()
            column1.append(float(numbers[0]))
            column2.append(float(numbers[1]))
        return column1, column2

def main():
    file_name = input("Enter the file name: ")   #attached example file name is floatcol.txt
    try:
        column1, column2 = readFile(file_name)
        average1 = sum(column1) / len(column1)
        average2 = sum(column2) / len(column2)
        print(f'Average of column 1: {average1:.2f}')
        print(f'Average of column 2: {average2:.2f}')
    except FileNotFoundError:
        print(f'Invalid input: File \'{file_name}\' not found.')

main()