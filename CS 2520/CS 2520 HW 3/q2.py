before = input('Convert from: ')
after = input('Convert to: ')
value = float(input('Value: '))
convertedValue = 0.0

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