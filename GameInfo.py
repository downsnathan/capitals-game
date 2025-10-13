import random
import re

class GameInfo:
    
    def makeDicts(self, countries, capitals):
        file = open("Capitals.txt")
        for line in file:
            
            split = line.split(",")
            if split[1] == "Afghanistan":
                split[0] = 0
            countries[int(split[0])] = split[1] 
            capitals[int(split[0])] = [split[-1][0:-1]] 
            if len(split) > 3:
                for i in range(2, len(split) - 1):
                    capitals[int(split[0])].append(split[i])

    def __init__(self):
        self.score = 0
        self.correctAnswers = 0
        self.maxCorrect = 197
        self.maxScore = 197 * 3
        self.countryDict = {}
        self.capitalDict = {}
        self.toAsk = []
        self.incorrect = []

        self.makeDicts(self.countryDict, self.capitalDict)
        for i in range(0, 198):
            self.toAsk.append(i)
        random.shuffle(self.toAsk)
        print(self.toAsk)

