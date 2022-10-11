from heapq import nlargest

class HighScoreTable:
    def __init__(self, lis: list):
        self.lis = lis

    def update(self, val:int):
        self.lis.append(val)

    def scores(self):
        return nlargest(3,self.lis)

hs = HighScoreTable([])

hs.update(10)
hs.update(10)
hs.update(-10)
hs.update(119)

print(hs.scores())