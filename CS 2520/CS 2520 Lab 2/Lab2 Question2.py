user_input = str(input('Enter a password: '))
newPassword = ''
for i in range(len(user_input)):
    if 'a' == user_input[i]:
        newPassword += '@'
    elif 'i' == user_input[i]:
        newPassword += '1'
    elif 'm' == user_input[i]:
        newPassword += 'M'
    elif 'B' == user_input[i]:
        newPassword += '8'
    elif 's' == user_input[i]:
        newPassword += '$'
    else:
        newPassword += user_input[i]
newPassword += '!'
print(newPassword)