'''
Toll roads have different fees based on the time of day and on weekends.
Has a function calc_toll() that has three parameters:
    the current hour of time (int)
    whether the time is morning (boolean)
    whether the day is a weekend (boolean)
The function returns the correct toll fee (float), based on the chart below.
Weekday Tolls
    Before 7:00 am ($1.15)
    7:00 am to 9:59 am ($2.95)
    10:00 am to 2:59 pm ($1.90)
    3:00 pm to 7:59 pm ($3.95)
    Starting 8:00 pm ($1.40)
Weekend Tolls
    Before 7:00 am ($1.05)
    7:00 am to 7:59 pm ($2.15)
    Starting 8:00 pm ($1.10)
'''

def calc_toll(currHour,ifMorning,ifWeekend):
    if ifWeekend:
        if ifMorning and currHour < 7:
            toll = 1.05
        if ifMorning and 7 <= currHour <= 12:
            toll = 2.15
        if not ifMorning and currHour < 8:
            toll = 2.15
        if not ifMorning and 8 <= currHour <= 12:
            toll = 1.10
    else:
        if ifMorning and currHour < 7:
            toll = 1.15
        if ifMorning and 7 <= currHour < 10:
            toll = 2.95
        if ifMorning and 10 <= currHour < 12:
            toll = 1.90
        if not ifMorning  and 12 == currHour or not ifMorning and currHour < 3:
            toll = 1.90
        if not ifMorning and 3 <= currHour < 8:
            toll = 3.95
        if not ifMorning and 8 <= currHour < 12:
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
    print(f'Toll Fee: {calc_toll(hour,morning,weekend):.2f}')

main()