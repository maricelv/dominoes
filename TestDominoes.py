
from graphics import *
from random import randrange
import random

class Domino:
    def __init__ (self,left,right):
        self.left = left
        self.right = right
        
    def draw(self,win,a,b):
        Rectangle(Point(a, b), Point(a,b)).draw(win)

    
def setUpWindow():
    win = GraphWin("Dominoes", 1200, 750)
    win.setCoords(0,0,10,10)
    return win

def dominoMaker():
    dominoList=[]
    for i in range(0,4):
        for j in range(0,4):
            newDomino = Domino(i,j)
            dominoList.append(newDomino)

    return dominoList

def listShuffle(alist):
    for i in range(len(aList)):
        r = randrange(i,15)
        aList[i], aList[r] = aList[r], aList[i]
    return aList




def drawEntryBoxes(win):

    LRBox=Entry(Point(4,1),3)
    LRBox.setSize(20)
    LRBoxLabel=Text(Point(4,0.5),"(Left or Right (L/R)")
    LRBoxLabel.setSize(20)
    LRBox.draw(win)
    LRBoxLabel.draw(win)
    win.getMouse()

    DBox=Entry(Point(7,1),3)
    DBox.setSize(20)
    DBoxLabel=Text(Point(7,0.5),"Which domino? (1-4)")
    DBoxLabel.setSize(20)
    DBox.draw(win)
    DBoxLabel.draw(win)
    win.getMouse()

    return LRBox,DBox

def welcomeWindow(win2):
    message = Text(Point(5,9), "Welcome to Dominoes")
    message.setSize(25)
    message.draw(win2)

    button = Rectangle(Point(5,4.5),Point(6,5.8))
    button.setFill("light gray")
    buttonLabel=Text(Point(5.5,5.15),"Click to Play")
    button.draw(win2)
    buttonLabel.draw(win2)

    rules=Text(Point(5,3),"Rules: The player who drew the highest double goes first, Laying the dominoes end to end (the touching ends must match: i.e., one’s touch one’s, two’s touch two’s, etc.)")
    rules.draw(win2)

def playDominoes():

    win = setUpWindow()
    win2 = setUpWindow()

    welcomeWindow(win2)

    dominoes = dominoMaker()
    listShuffle(dominoes)
    
    LRBox, DBox = drawEntryBoxes(win)
    
    
    #player1(win)
    #compPlayer(win)

    
    for i in range(0,4):
        playerHand = random.sample(range(45),4)
        compList = random.sample(range(45),4)

    print(playerHand)
    print(compList)


    
    flag = [0,0,0,0]
    location = [(1.5,2.5),(3.5,4.5),(5.5,6.5),(7.5,8.5)]
    i = 0
    for x in playerHand:
        if x >= 10:
            left = x//10
            right = x-(left*10)
        else:
            left = 0
            right = x
        val = str(left) + " - " + str(right)
        if flag[i] == 0:
            insideText = Text(Point((location[i][0]+location[i][1])/2,2.4),val).draw(win)
            domino1 = Domino(Point(location[i][0],2), Point(location[i][1],2.8))
            numText1 = Text(Point((location[0][0]+location[0][1])/2,1.8),"1").draw(win)
            numText2 = Text(Point((location[1][0]+location[1][1])/2,1.8),"2").draw(win)
            numText3 = Text(Point((location[2][0]+location[2][1])/2,1.8),"3").draw(win)
            numText4 = Text(Point((location[3][0]+location[3][1])/2,1.8),"4").draw(win)
            domino1.draw(win)
        i+=1
        clickPoint = win.getMouse()
        
    #LR = LRBox.getText() # gets L/R value

    #D = DBox.getText()
    #D = int(D)
    #if D == 1:
        # add to L/R side of chain
    #elif D == 2:
        
    
    firstPiece = Domino(Point(4.5,5.5),Point(5.5,6.3))
    firstPiece.draw(win)
    firstPieceText = Text(Point(5,5.9),"4 - 4")
    firstPieceText.draw(win)

    

    
    
    
   
    win.getMouse() # pause for click in window
    win.close()


playDominoes()
