'''
Asks the users from which unit they want to convert (fl. oz, gal, oz, lb, in, ft, mi) 
    and to which unit they want to convert          (ml, l, g, kg, mm, cm, m, km)
Ask for the value to be converted, then display the result
Rejects incompatible conversions (such as gal ➔ km)
'''

before = input('Convert from: ')
after = input('Convert to: ')
value = float(input('Value: '))

conversions_dictionary = {
    'fl. oz': {'ml': 29.5735, 'l': 0.0295735},
    'gal': {'ml': 3785.41, 'l': 3.78541},
    'oz': {'g': 28.3495, 'kg': 0.0283495},
    'lb': {'g': 453.592, 'kg': 0.453592},
    'in': {'mm': 25.4, 'cm': 2.54, 'm': 0.0254, 'km': 0.0000254},
    'ft': {'mm': 304.8, 'cm': 30.48, 'm': 0.3048, 'km': 0.0003048},
    'mi': {'mm': 1609350, 'cm': 160935, 'm': 1609.35, 'km': 1.60935}
}

if before in conversions_dictionary and after in conversions_dictionary[before]:
    converted_value = value * conversions_dictionary[before][after]
    print(f'{value} {before} = {converted_value} {after}')
else:
    print('ERROR: Incompatible conversion')

'''
if before == 'fl. oz' or before == 'gal':
    if after == 'ml':
        if before == 'fl. oz':
            convertedValue = value*29.5735
        if before == 'gal':
            convertedValue = value*3785.41
        print(f'{value} {before} = {convertedValue} {after}')
    elif after == 'l':
        if before == 'fl. oz':
            convertedValue = value*0.0295735
        if before == 'gal':
            convertedValue = value*3.78541
        print(f'{value} {before} = {convertedValue} {after}')
    else:
        print(f'ERROR \nincompatible conversion')

elif before == 'oz' or before =='lb':
    if after == 'g':
        if before == 'oz':
            convertedValue = value*28.3495
        if before == 'lb':
            convertedValue = value*453.592
        print(f'{value} {before} = {convertedValue} {after}')
    elif after == 'kg':
        if before == 'oz':
            convertedValue = value*0.0283495
        if before == 'lb':
            convertedValue = value*0.453592
        print(f'{value} {before} = {convertedValue} {after}')
    else:
        print(f'ERROR \nincompatible conversion')

elif before == 'in' or before == 'ft' or before =='mi':
    if after == 'mm':
        if before == 'in':
            convertedValue = value*25.4
        if before == 'ft':
            convertedValue = value*304.8
        if before == 'mi':
            convertedValue = value*1609350
        print(f'{value} {before} = {convertedValue} {after}')
    elif after == 'cm':
        if before == 'in':
            convertedValue = value*2.54
        if before == 'ft':
            convertedValue = value*30.48
        if before == 'mi':
            convertedValue = value*160935
        print(f'{value} {before} = {convertedValue} {after}')
    elif after == 'm':
        if before == 'in':
            convertedValue = value*0.0254
        if before == 'ft':
            convertedValue = value*0.3048
        if before == 'mi':
            convertedValue = value*1609.35
        print(f'{value} {before} = {convertedValue} {after}')
    elif after == 'km':
        if before == 'in':
            convertedValue = value*0.0000254
        if before == 'ft':
            convertedValue = value*0.0003048
        if before == 'mi':
            convertedValue = value*1.60935
        print(f'{value} {before} = {convertedValue} {after}')
    else:
        print(f'ERROR \nincompatible conversion')
'''