import random
from PIL import Image
import matplotlib.pyplot as plt
from IPython.core.display import clear_output
from GameInfo import GameInfo
import time

def showMap(index):
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
    set_size(10,10)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(image)
    plt.show()

def showScore(info):
    print("Score: " + info.score + "/" + info.maxScore + "        Correct: " + info.correct + "/" + info.maxCorrect)

def questionAnswer(info, index):
    correctAnswers = info.capitalDict[index]
    for posScore in range(3, 0, -1):
        clear_output()
        showScore(info)
        showMap(index)
        if posScore < 3:
            hint = []
            for i in range(0, len(info.capitalDict[index])):
                hint[i] = info.capitalDict[index][i][0] + "*" * len(info.capitalDict[index][i] - 1)
            if posScore == 1:
                for i in range(0, len(info.capitalSict[index])):
                    hint[i][-1] = info.capitalDict[index][i][-1]
            print("Hint: " + hint)
        response = input("Capital: ")
        if response in info.capitalDict[index]:
            print("Correct!")
            info.score += posScore
            info.correct += 1
            time.sleep(1)
            info.capitalDict[index].remove(response)
            if len(info.capitalDict[index]) == 0:
                info.capitalDict.remove(index)
            return
        else:
            print("Incorrect")
            time.sleep(1)
    info.capitalDict.remove(index)

def game():
    info = GameInfo()
    clear_output()
    showMap("blank")
    input("Type y to begin: ")
    start = time.time()
    while len(info.toAsk) > 0:
        index = info.toAsk.pop(0)
        questionAnswer(info, index)
    clear_output()
    showScore(info)
    showMap("blank")
    gameLength = int(time.time() - start)
    print("Time: " + time)