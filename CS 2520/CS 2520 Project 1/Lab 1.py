#function to get the user's message
def getMessage():
    user_input = str(input('Enter a sample text: '))
    print(f'You entered: {user_input}\n')
    return user_input

#function that prints the menu
def print_menu():
    print(f'MENU \nc - Number of non-whitespace characters \nw - Number of words \nf - Fix capitalization \nr - Replace punctuation \ns - Shorten spaces \nq - Quit \n')

#function to perform the menu option chosen
def execute_menu(choice,text):
    if choice == 'c':
        output = get_num_of_non_WS_characters(text)
    if choice == 'w':
        output = get_num_of_words(text)
    if choice == 'f':
        output = fix_capitalization(text)
    if choice == 'r':
        output = replace_punctuation(text)
    if choice == 's':
        output = shorten_space(text)
    if choice == 'q':
        output = ''
    return output

#function for option c
def get_num_of_non_WS_characters(text):
    '''for each character in text: if not equal to whitespace, add 1 to counter'''
    number = 0
    for i in text:
        if i == ' ':
            number = number
        else:
            number += 1
    return number

#function for option w
def get_num_of_words(text):
    number = len(text.split())
    return number

#function for option f
def fix_capitalization(text):
    '''when a period, question mark, exclamation mark is found, boolean is set to true
    when boolean is true: the next non-whitespace character is capitalized and boolean set to false'''
    newText = ''
    number = 0
    doCapitalization = True
    for char in text:
        if char != ' ':
            if doCapitalization:
                char = char.upper()
                doCapitalization = False
                number += 1
            if char in '.!?':
                doCapitalization = True
        newText += char
    print(f'Number of letters capitalized: {number}')
    return newText
        
#function for option r
def replace_punctuation(text,exclamation_count=0,semicolon_count=0):
    '''each exclamation is counted then replaced with a period
    each semicolon is counted then replaced with a comma'''
    exclamation_count = text.count('!')
    newText = text.replace('!','.')
    semicolon_count = text.count(';')
    newText = newText.replace(';',',')
    if exclamation_count == 0 and semicolon_count == 0:
        print(f'No Punctuation was replaced \nexclamation_count: {exclamation_count} \nsemicolon_count: {semicolon_count}')
    else:
        print(f'Punctuation replaced \nexclamation_count: {exclamation_count} \nsemicolon_count: {semicolon_count}')
    return newText

#function for option s
def shorten_space(text):
    '''if the character is a space the boolean is set to true
    if the character after is a space the second space isn't added to the new string 
    and boolean set back to false
    if the character is not a space the boolean is set to or kept at false'''
    newText = ''
    removeSpace = False
    for char in text:
        if char == ' ':
            if removeSpace == True:
                newText = newText
                removeSpace = False
            else:
                newText += char
            removeSpace = True
        else:
            newText += char
            removeSpace = False
    return newText

#function to determine the full string output based on the option chosen
def option_output(option,output):
    if option == 'c':
        print(f'Number of non-whitespace characters: {output} \n')
    if option == 'w':
        print(f'Number of words: {output} \n')
    if option in 'frs':
        print(f'Edited text: {output} \n')
    if option == 'q':
        print('Thank you come again')

#main function
def main():
    message = getMessage()
    print_menu()
    user_choice = str(input('Choose an option: '))
    options = ['c','w','f','r','s','q']
    output = ''
    while user_choice != 'q':
        while user_choice not in options:
            print('Please enter a valid option')
            user_choice = (input('Choose an option: ')).lower()
        output = execute_menu(user_choice,message)
        option_output(user_choice,output)
        print_menu()
        user_choice = str(input('Choose an option: '))
    option_output(user_choice,output)

main()