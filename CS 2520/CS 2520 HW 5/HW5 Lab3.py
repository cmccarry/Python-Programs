def commonCharacters(set1, set2):
    common = set1.intersection(set2)
    return sorted(common)

def uniqueCharacters(set1, set2):
    unique = set1.difference(set2)
    return sorted(unique)

def missingCharacters(set1, set2):
    set3 = set()
    for i in range(ord('a'), ord('z')+1):
        set3.add(chr(i))
    missing = set3.difference(set1)
    missing = missing.difference(set2)
    return sorted(missing)

def main():
    userString1 = set(input("Enter the first string: "))
    userString2 = set(input("Enter the second string: "))
    print(f"\nCharacters that occur in both strings: {commonCharacters(userString1,userString2)}")
    print(f"Characters that occur in the first string but not the second: {uniqueCharacters(userString1,userString2)}")
    print(f"Characters that occur in the second string but not the first: {uniqueCharacters(userString2,userString1)}")
    print(f"Characters that don't occur in either string: {missingCharacters(userString1,userString2)}\n")

main()