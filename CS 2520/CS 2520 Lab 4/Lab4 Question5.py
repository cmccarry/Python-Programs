def calc_toll(currHour,ifMorning,ifWeekend):
    if ifWeekend == True:
        if ifMorning == True and currHour < 7:
            toll = 1.05
        if ifMorning == True and 7 <= currHour <= 12:
            toll = 2.15
        if ifMorning == False and currHour < 8:
            toll = 2.15
        if ifMorning == False and 8 <= currHour <= 12:
            toll = 1.10
    elif ifWeekend == False:
        if ifMorning == True and currHour < 7:
            toll = 1.15
        if ifMorning == True and 7 <= currHour < 10:
            toll = 2.95
        if ifMorning == True and 10 <= currHour < 12:
            toll = 1.90
        if ifMorning == False and 12 == currHour or ifMorning == False and currHour < 3:
            toll = 1.90
        if ifMorning == False and 3 <= currHour < 8:
            toll = 3.95
        if ifMorning == False and 8 <= currHour < 12:
            toll = 1.40
    return toll

def main():
    morning = False
    weekend = False
    hour = int(input('Current hour of time: '))
    if input('is morning? t/f: ').upper() == 'T':
        morning = True
    if input('Is weekend? t/f: ').upper() == 'T':
        weekend = True
    print(f'{calc_toll(hour,morning,weekend):.2f}')

main()