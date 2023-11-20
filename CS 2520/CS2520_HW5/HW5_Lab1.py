'''
Keeps a dictionary in which both keys and values are strings—names of students and their course grades. 
Prompts the user to add or remove students, to modify grades, or to print all grades. 
'''

def print_menu():
    #outputs the user options
    print('\n~~~~~~~~~~Menu~~~~~~~~~~ \
          \n 1. Add Student \
          \n 2. Remove Student \
          \n 3. Modify Grade \
          \n 4. Print Class Roster \
          \n 5. Remove Entire Class \
          \n 6. Exit')
    return

def add_student(dictionary):
    #adds a student to the class, given their name and grade
    studentName = (input('Enter the name of the student you wish to add: ')).title()
    studentGrade = (input(f"Enter {studentName}'s grade: ")).upper()
    dictionary[studentName] = studentGrade
    return

def remove_student(dictionary):
    #removes student from class, given their name in the dictionary
    studentName = (input('Enter the name of the student you wish to remove: ')).title()
    if studentName in dictionary:
        del dictionary[studentName]
        print(f'{studentName} was removed from the class')
    else:
        print(f'{studentName} was not found in the class')
    return

def modify_grade(dictionary):
    #changes student grade, given their name and new grade
    studentName = (input('Enter the name of the student to modify their grade: ')).title()
    (studentName[0]).upper()
    if studentName in dictionary:
        newGrade = (input(f"Enter {studentName}'s new grade: ")).upper()
        dictionary[studentName] = newGrade
    else:
        print(f"{studentName} was not found in the class")
    return

def print_grades(dictionary):
    #prints the class roster with format-> name: grade
    print('~~~~~~Class Roster~~~~~~')
    if len(dictionary) == 0:
        print('Empty')
    for name,grade in dictionary.items():
        print(f"{name}: {grade}")
    return

def clear_class(dictionary):
    #does dictionary.clear() if user inputs 'y'
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

        print_menu()

        userChoice = input("\nPlease enter your choice (1-6): ")

        if userChoice == '1':
            add_student(studentGrades)
        elif userChoice == '2':
            remove_student(studentGrades)
        elif userChoice == '3':
            modify_grade(studentGrades)
        elif userChoice == '4':
            print_grades(studentGrades)
        elif userChoice == '5':
            studentGrades = clear_class(studentGrades)
        elif userChoice == '6':
            break
        else:
            print("Invalid input. Please only enter an integer from 1-6.")

    print('Thank you have a good day')

main()