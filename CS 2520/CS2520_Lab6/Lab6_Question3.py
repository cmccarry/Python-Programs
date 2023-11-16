class VotingMachine:
    def __init__(self):
        self.democrat_votes = 0
        self.republican_votes = 0
    
    def voteDemocrat(self, count = 1):
        self.democrat_votes += count

    def voteRepublican(self, count = 1):
        self.republican_votes += count

    def getTally(self):
        return self.democrat_votes, self.republican_votes
    
    def clearTally(self):
        VotingMachine.__init__(self)

def votes():
    machine1 = VotingMachine()
    machine1.voteDemocrat(10)
    machine1.voteRepublican()
    tally1, tally2 = machine1.getTally()
    print(f"Democratic Votes: {tally1} \
        \nRepublican Votes: {tally2}")

    machine1.clearTally()
    tally1, tally2 = machine1.getTally()
    print(f"Democratic Votes: {tally1} \
        \nRepublican Votes: {tally2}")

votes()
