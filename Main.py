import random
from PIL import Image
import matplotlib.pyplot as plt
from GameInfo import GameInfo
import time

try:
  from google.colab  import output
  IN_COLAB = True
except:
  IN_COLAB = False


def showMap(index): #index of country or "blank map" for map without any country highlighted
    def set_size(w,h, ax=None):
        """ w, h: width, height in inches """
        if not ax: ax=plt.gca()
        l = ax.figure.subplotpars.left
        r = ax.figure.subplotpars.right
        t = ax.figure.subplotpars.top
        b = ax.figure.subplotpars.bottom
        figw = float(w)/(r-l)
        figh = float(h)/(t-b)
        ax.figure.set_size_inches(figw, figh)

    image = Image.open("Images/MapChart_Map (" + str(index) + ").jpeg")
    fig, ax=plt.subplots()
    ax.plot([1,3,2])
    set_size(6,6)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(image)
    plt.show()

def showScore(info):
    print("Correct: " + str(info.correct) + "/" + str(info.maxCorrect) + "        " + "Score: " + str(info.score) + "/" + str(info.maxScore))

def askQuestion(info, index):
    #info.capitalDict[index] = correct answers
    for posScore in range(3, 0, -1):
        if IN_COLAB:
            output.clear()
        showScore(info)
        showMap(index)
        if posScore < 3:
            hint = []
            for i in range(0, len(info.capitalDict[index])):
                hint.append(info.capitalDict[index][i][0].upper() + ("*" * (len(info.capitalDict[index][i]) - 1)))
            if posScore == 1:
                for i in range(0, len(info.capitalDict[index])):
                    hint[i] = hint[i][0:-1] + info.capitalDict[index][i][-1]
            hintString = hint[0]
            for i in range(1, len(hint)):
                hintString += ", " + hint[i]

            print("Hint: " + hintString)
        time.sleep(.5)
        response = input("Capital: ")
        if response.lower() in info.capitalDict[index]:
            print("Correct!")
            info.score += posScore
            info.correct += 1
            time.sleep(1)
            return
        else:
            print("Incorrect")
            time.sleep(1)
    info.incorrect.append(index)
    print("You ran out of attempts")

def game():
    info = GameInfo()
    if IN_COLAB:
        output.clear()
    startGame = True
    while startGame:
        info.newGame()
        showMap("blank")
        time.sleep(.5)
        start = input("Type y to begin: ")
        start = time.time()
        while len(info.toAsk) > 0:
            index = info.toAsk.pop(0)
            askQuestion(info, index)
        if IN_COLAB:
            output.clear()
        showScore(info)
        gameLengthSecs = int(time.time() - start)
        gameLength = "" + str(gameLengthSecs / 60) + ":" + str(gameLengthSecs % 60)
        info.previousScores[len(info.previousScores)] = (str(len(info.previousScores)), str(info.score), str(gameLength))
        print("Time: " + str(gameLength))
        print("Incorrect Countries: ")
        for i in info.incorrect:
          print(i)
        print()
        time.sleep(1)
        input("To move on to the scores screen, type y: ")
        print("Attempt              Score               Time")
        for i in info.previousScores:
            print(info.previousScores[i[0]] + "                  " + info.previousScores[i[1]] + "                " + previousScores[i[2]])
        print()
        print()
        response = input("Type y to try again or q to quit: ")
        if response != "y":
            startGame = False
            print("Goodbye")
            

game()
