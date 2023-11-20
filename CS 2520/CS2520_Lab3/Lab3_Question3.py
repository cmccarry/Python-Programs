'''
A program using a function to create a menu mentioned below:

Today's Menu:
   1) Gumbo
   2) Jambalaya
   3) Quit
'''

menu = (f'Today\'s Menu: \
        \n  1)Gumbo \
        \n  2)Jambalaya \
        \n  3)Quit\n')

def main():
    order = ''
    while order != '3':
        options(order)
        order = input('Enter choice: ')
    print(f'Goodbye')

def options(order):
    if order == '1':
        print(f'Order: Gumbo\n')
    elif order == '2':
        print(f'Order: Jambalaya\n')
    print(menu)

main()