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