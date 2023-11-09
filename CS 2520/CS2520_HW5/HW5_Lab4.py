def build_dictionary(words):
    dictionary = {}
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary

def main():
    words = (input("Enter a list of words separated with a space: ")).split()
    fullDictionary = build_dictionary(words)
    sortedDictionary = sorted(fullDictionary.items(), key = lambda x: x[0])
    for word, frequency in sortedDictionary:
        print(f"{word} - {frequency}")

main()