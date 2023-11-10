'''
Builds a word frequency dictionary from a list of words.
The main code builds the word list from an input string, calls build_dictionary() to build the dictionary, and displays the dictionary sorted by key value.
'''

def build_dictionary(words):
    #builds dictionary using .get() with default value of one if the word is not already in the dictionary
    #key gets increased by one for every instance of the word
    dictionary = {}
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary

def main():
    words = (input("Enter a list of words separated with a space: ")).split()
    fullDictionary = build_dictionary(words)

    #sorts dictionary by words and keeps key values
    sortedDictionary = sorted(fullDictionary.items(), key = lambda x: x[0])

    #prints the dictionary with format-> word - frequency
    for word, frequency in sortedDictionary:
        print(f"{word} - {frequency}")

main()