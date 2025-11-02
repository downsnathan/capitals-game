import random
import re

class GameInfo:
    
    def makeDicts(self, countries, capitals):
        file = open("Capitals.txt")
        for line in file:
            split = line.split(",")
            if split[1] == "Afghanistan": #get rid of random characters added to start of file for some reason
                split[0] = 0
            countries[int(split[0])] = split[1] 
            capitals[int(split[0])] = [split[-1][0:-1]] 
            if len(split) > 3: #if more than one capital, add the rest to the list
                for i in range(2, len(split) - 1):
                    capitals[int(split[0])].append(split[i])

    def newGame(self):
        for i in range(0, self.maxCorrect):
            self.toAsk.append(i)
        random.shuffle(self.toAsk)
        self.incorrect = []
        self.score = 0
        self.correct = 0

    def __init__(self):
        self.score = 0
        self.correct = 0
        self.maxCorrect = 6
        self.maxScore = self.maxCorrect * 3
        self.countryDict = {} #map index to country
        self.capitalDict = {} #map index to capital(s)
        self.toAsk = []
        self.incorrect = []
        self.previousScores = {}

        self.makeDicts(self.countryDict, self.capitalDict)

