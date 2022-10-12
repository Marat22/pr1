from heapq import nlargest

class HighScoreTable:
    def __init__(self, length: int):
        self.lis = []
        self.scores = []
        self.__ln__ = length

    def update(self, val:int):
        self.lis.append(val)
        self.scores = nlargest(self.__ln__, self.lis)

    def reset(self):
        self.lis.clear()
        self.scores = nlargest(self.__ln__, self.lis)
