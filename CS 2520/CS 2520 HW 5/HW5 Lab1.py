def addStudent(dictionary):
    studentName = input('Enter the name of the student you wish to add: ')
    studentGrade = input(f"Enter {studentName}'s grade: ")
    dictionary[studentName] = studentGrade
    return

def removeStudent(dictionary):
    studentName = input('Enter the name of the student you wish to remove: ')
    if studentName in dictionary:
        del dictionary[studentName]
        print(f'{studentName} was removed from the class')
    else:
        print(f'{studentName} was not found in the class')
    return

def modifyGrade(dictionary):
    studentName = input('Enter the name of the student to modify their grade: ')
    if studentName in dictionary:
        newGrade = (input(f"Enter {studentName}'s new grade: ")).upper()
        dictionary[studentName] = newGrade
    else:
        print(f"{studentName} was not found in the class")
    return

def printGrades(dictionary):
    print('~~~~~~~~~~Class Roster~~~~~~~~~~')
    if len(dictionary) == 0:
        print('Empty')
    for name,grade in dictionary.items():
        print(f"{name}: {grade}")
    return

def clearClass(dictionary):
    option = (input('Would you like to clear the entire class roster and grades? (y/n): ')).lower()
    if option == 'y':
        dictionary.clear()
        print("Your class roster has been cleared")
    else:
        print('Operation stopped')
    return dictionary

def main():
    studentGrades = {}

    while True:
        print('\n~~~~~~~~~~Menu~~~~~~~~~~')
        print('1. Add Student')
        print('2. Remove Student')
        print('3. Modify Grade')
        print('4. Print Class Roster')
        print('5. Remove Entire Class')
        print('6. Exit')

        userChoice = input("\nPlease enter your choice (1-6): ")

        if userChoice == '1':
            addStudent(studentGrades)
        elif userChoice == '2':
            removeStudent(studentGrades)
        elif userChoice == '3':
            modifyGrade(studentGrades)
        elif userChoice == '4':
            printGrades(studentGrades)
        elif userChoice == '5':
            studentGrades = clearClass(studentGrades)
        elif userChoice == '6':
            break
        else:
            print("Invalid input. Please only enter an integer from 1-6.")

    print('Thank you have a good day')

main()