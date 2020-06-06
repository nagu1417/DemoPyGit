
class Cricket:
    umpires=3
    def __init__(self):
        self.players=11
        self.overs=50

c1=Cricket();
c2=Cricket()
c1.players=8
c1.overs=20
c1.umpires=2;
print(c1.players,c1.overs,c1.umpires)
print(c2.players,c2.overs,c2.umpires)
