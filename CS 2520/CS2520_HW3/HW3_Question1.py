'''
Takes user input describing a playing card in the following shorthand notation:
A          Ace
2 ... 10   Card values 
J          Jack 
Q          Queen 
K          King 
D          Diamonds 
H          Hearts 
S          Spades 
C          Clubs
ex. QD, 8H, JS
Print the full description of the card
'''

card = input('Enter the card notation: ')
card = card.upper()

if len(card) == 2:
    value = card[0]
    suit = card[1]
else:
    value = card[0] + card[1]
    suit = card[2]

valueDictionary = {'A': 'Ace', 'J': 'Jack', 'Q': 'Queen', 'K': 'King'}
suitDictionary = {'D': 'Diamonds', 'H': 'Hearts', 'S': 'Spades', 'C': 'Clubs'}

value = valueDictionary.get(value, value)
suit = suitDictionary.get(suit, suit)

print(f'{value} of {suit}')

'''
if value == 'A':
    value = 'Ace'
if value == 'J':
    value = 'Jack'
if value == 'Q':
    value = 'Queen'
if value == 'K':
    value = 'king'
if suit == 'D':
    suit = 'Diamonds'
if suit == 'H':
    suit = 'Hearts'
if suit == 'S':
    suit = 'Spades'
if suit == 'C':
    suit = 'Clubs'
    
print(f'{value} of {suit}')
'''