'''
Provide a class Letter for authoring a simple letter. In the constructor, supply the names of the sender and the recipient:
def __init__(self, letterFrom, letterTo):
    Supply a method
def addLine(self, line):
    to add a line of text to the body of the letter. Supply a method
def getText(self):
    that returns the entire text of the letter. 
The text has the form:
Dear recipient name:
blank line
first line of the body
second line of the body
. . .
last line of the body
blank line
Sincerely,
blank line
sender name
Also supply a driver program that prints the following letter.
'''

class Letter:
    def __init__(self, letterFrom, letterTo):
        self.letterFrom = letterFrom
        self.letterTo = letterTo
        self.contents = ""

    def addLine(self, line):
        self.contents += f"{line} \n"

    def getText(self):
        return f"Dear {self.letterTo}: \n \
               \n{self.contents} \
               \nSincerely, \n \
               \n{self.letterFrom}"
