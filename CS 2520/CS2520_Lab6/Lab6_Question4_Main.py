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
