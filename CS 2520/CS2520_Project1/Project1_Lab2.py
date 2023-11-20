import math

#function to get circle dimensions
def get_circle(message,decider):
    '''message prompt for what value the user to enter is displayed and user input is returned
    if a user doesn't enter an integer value, an x-coordinate or y-coordinate in quadrant 1, or a postive integer for the radius, the chances counter increases
    if the counter goes up to 3 it exits the program'''
    chances = 2
    while chances != -1:
        try:
            chancePrompt = (f'Chances left: {chances}')
            value = int(input(message))
            if decider == 'x' or decider =='y':
                if value >= 0:
                    return value
                else:
                    chances -= 1
                    print(f'Invalid input. Please enter an integer value for this coordinate in Quadrant 1 \n{chancePrompt}\n')
            elif decider == 'r':
                if value >= 0:
                    return value
                else:
                    chances -= 1
                    print(f'Invalid input. Please enter a valid radius \n {chancePrompt}\n')
        except ValueError:
            chances -= 1
            print(f'Invalid Input. Please enter an integer value \n{chancePrompt}\n')
    print('\nToo many incorrect data input attempts. Program will now end\n')
    exit()

#function that calculates the distance (d) and determines the result
def calculateCircles(x0,y0,r0,x1,y1,r1):
    d = math.sqrt((x1-x0)**2 + (y1-y0)**2)
    print(f'Distance: {d:.2f}')
    if d > (r0+r1):             #Example data: circle1: 1 1 1 , circle2: 5 5 1
        result = 'The two circles do not intersect and are separate'
    elif d < abs(r0-r1):        #Example data: circle1: 5 5 1 , circle2: 5 5 10
        result = 'The two circles do not intersect, and one is contained within the other'
    elif d == (r0+r1):          #Example data: circle1: 1 1 1 , circle2: 3 1 1
        result = 'The two circles intersect at a single point'
    elif d == 0 and r0 == r1:   #Example data: circle1: 1 1 1 , circle2: 1 1 1
        result = 'The two circles are coincident'
    else:                       #Example data: circle1: 1 1 1 , circle2 2 2 1
        result = 'The two circles intersect at two points'
    return result

#main function
def main():
    option = ''
    while option != 'n':
        x0 = get_circle('Enter x-coordinate of the first circle center: ','x')
        y0 = get_circle('Enter y-coordinate of the first circle center: ','y')
        r0 = get_circle('Enter radius of the first circle: ','r')
        x1 = get_circle('Enter x-coordinate of the second circle center: ','x')
        y1 = get_circle('Enter y-coordinate of the second circle center: ','y')
        r1 = get_circle('Enter radius of the second circle: ','r')
        print(f'\nFirst circle: coordinates({x0},{y0}) radius:{r0}')
        print(f'Second circle: coordinates({x1},{y1}) radius:{r1}')
        print(calculateCircles(x0,y0,r0,x1,y1,r1)+'\n')
        option = (input('Would you like to continue? (y/n): ')).lower()
        while option not in 'yn':
            print(f'Invalid input. Please only enter \'y\' for yes or \'n\' for no')
            option = (input('Would you like to continue? (y/n): ')).lower()
    print('Have a nice day. Goodbye')
    
main()