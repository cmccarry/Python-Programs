def findValue(x):
    if x == 'M': return 1000
    if x == 'D': return 500
    if x == 'C': return 100
    if x == 'L': return 50
    if x == 'X': return 10
    if x == 'V': return 5
    if x == 'I': return 1
    return -1

def romanToDecimal(roman):
    endDecimal = 0
    i = 0
    while (i < len(roman)):
        firstRoman = findValue(roman[i])
        if (i+1 < len(roman)):
            secondRoman = findValue(roman[i+1])
            if (firstRoman >= secondRoman):
                endDecimal += firstRoman
                i += 1
            else:
                difference = secondRoman - firstRoman
                endDecimal += difference
                i += 2
        else:
            endDecimal += firstRoman
            i += 1
    return endDecimal

def main():
    romanNumeral = input('Enter the roman numeral: ').upper()
    print(romanToDecimal(romanNumeral))

main()