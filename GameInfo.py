import random

class GameInfo:
    
    def makeDicts(self, countries, capitals):
        file = open("capitals-game/Capitals.txt")
        for line in file:
            split = line.split()
            countries[int(split[0])] = split[1] 
            capitals[int(split[0])] = split[2:-1] #might have to take out \n

    def __init__(self):
        self.score = 0
        self.correctAnswers = 0
        self.maxCorrect = 197
        self.maxScore = 197 * 3
        self.countryDict = {}
        self.capitalDict = {}
        self.toAsk = [range(0, 198)]
        self.incorrect = []
        
        self.makeDicts(self.countryDict, self.capitalDict)
        random.shuffle(self.toAsk)
