'''
Has a function: getTimeName(hours, minutes), that returns the English name for a point in time, such as:
    "ten minutes past two"
    "half past three"
    "a quarter to four"
    "five o'clock"
Assumes that hours are between 1 and 12.
'''

def main():
    userHour = int(input('Enter the hour: '))
    userMinute = int(input('Enter the minutes: '))
    if 1 > userHour or userHour > 12 or 0 > userMinute or userMinute > 59:
        print('INVALID TIME')
    else:
        englishTime = getTimeName(userHour,userMinute)
        print(f'{englishTime}')

def getTimeName(hours,minutes):
    #hours and minutes get changed into their word counterparts
    timeH = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
    timeM = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','Seventeen','eighteen','nineteen','twenty','twenty-one','twenty-two','twenty-three','twenty-four','twenty-five','twenty-six','twenty-seven','twenty-eight','twenty-nine','thirty','thirty-one','thirty-two','thirty-three','thirty-four','thirty-five','thirty-six','thirty-seven','thirty-eight','thirty-nine','forty','forty-one','forty-two','forty-three','forty-four','forty-five','forty-six','forty-seven','forty-eight','forty-nine','fifty','fifty-one','fifty-two','fifty-three','fifty-four','fifty-five','fifty-six','fifty-seven','fifty-eight','fifty-nine','sixty']
    hour = timeH[hours]
    minute = timeM[minutes]
    
    #the appropriate english phrase for the time is found
    if minutes == 0:
        phrase = (f'{hour} o\' clock')
    elif minutes == 15:
        phrase = (f'a quarter past {hour}')
    elif minutes == 30:
        phrase = (f'half past {hour}')
    elif minutes == 45:
        hour = timeH[hours+1]
        phrase = (f'a quarter to {hour}')
    else:
        if minutes < 30:
            phrase = (f'{minute} minutes past {hour}')
        else:
            hour = timeH[hours+1]
            minute = timeM[60-minutes]
            phrase = (f'{minute} minutes to {hour}')
    return phrase

main()