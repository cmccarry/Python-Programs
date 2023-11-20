'''
Has a recursive function
    def isPalindrome(string):
that returns True if string is a palindrome, that is, a word that is the same when reversed.
'''

def isPalindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return isPalindrome(word[1:-1])

def main():
    user_word = input('enter word to check if palindrome: ')
    print(isPalindrome(user_word))

main()