from Lab6_Question4_Main import Letter

def makeLetter():
    letter1 = Letter("Mary","John")
    letter1.addLine("I am sorry we must part.")
    letter1.addLine("I wish you all the best.")
    print(letter1.getText())

makeLetter()
