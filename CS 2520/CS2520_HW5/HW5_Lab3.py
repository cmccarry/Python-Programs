'''
Given 2 strings, prints:
    the characters that occur in both strings.
    the characters that occur in one string but not the other.
    the letters that don't occur in either string.
'''

def common_characters(set1, set2):
    common = set1.intersection(set2)
    return sorted(common)

def unique_characters(set1, set2):
    unique = set1.difference(set2)
    return sorted(unique)

def missing_characters(set1, set2):
    #creates a set(set3) with all characters in the alphabet
    #compares both sets to set3 using .difference()
    set3 = set()
    for i in range(ord('a'), ord('z')+1):
        set3.add(chr(i))
    missing = set3.difference(set1)
    missing = missing.difference(set2)
    return sorted(missing)

def main():
    userString1 = set(input("Enter the first string: "))
    userString2 = set(input("Enter the second string: "))
    print(f"\nCharacters that occur in both strings: {common_characters(userString1,userString2)}")
    print(f"Characters that occur in the first string but not the second: {unique_characters(userString1,userString2)}")
    print(f"Characters that occur in the second string but not the first: {unique_characters(userString2,userString1)}")
    print(f"Characters that don't occur in either string: {missing_characters(userString1,userString2)}\n")

main()