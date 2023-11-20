'''
Has a recursive function called draw_triangle() that outputs lines of '*' to form a right side up isosceles triangle.
Function draw_triangle() has one parameter, an integer representing the base length of the triangle.
Assumes the base length is always odd and less than 20.
Outputs 9 spaces before the first '*' on the first line for correct formatting.
'''

def draw_triangle(baseL,space,star):
    print(' '*space,end='')
    print('*'*star)
    baseL -= 2
    if baseL > 0:
        draw_triangle(baseL,space-1,star+2)

def main():
    baseLength = int(input('Base length of the triangle: '))
    draw_triangle(baseLength,9,1)

main()