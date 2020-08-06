##Dominoes
##Dominoes.py
##Maricel Vicente
##bvicente@syr.edu

from graphics import *
from random import randrange


##(CLOD) where you define a class of your own design AND somewhere create an object of a class of your own design.
# The Domino Class contains the left and right sides of the graphical domino
class Domino:
    def __init__ (self,left,right):
        self.left = left
        self.right = right
        self.tile = None
        self.title = None
        self.index = 0
        self.indextext = None
    # Inside the Domino Class, there should be a method to draw the domino
    def draw(self,win,a,b):
        self.tile = Rectangle(Point(a, b), Point(a+1.5,b+1))
        self.tile.draw(win)
        ##(OTXT) somewhere you write to the screen using Text
        self.title = Text(Point(a+.7,b+0.5), str(self.left) + "  -  " + str(self.right))
        self.title.draw(win)
        self.indextext = Text(Point(a+0.75,b+1.5),str(self.index)) 
        self.indextext.draw(win)

    def indexdomino(self,index):
        self.index = index
        
# The GamePlay Class handles all of the logical movements for the gameplay
class GamePlay:
    def __init__(self):
        self.box = None
        # The chain is the center of the board with all of the played dominoes
        self.chain = []
        self.leftcount = 0
        self.rightcount = 0

    # The entry box collects which domino the user wants to play (1,2,3,4) and to place it left or right (r/l)
    def draw(self,win):
        self.box = Entry(Point(5,.7),3)
        self.box.setSize(15)
        self.boxlabel = Text(Point(4.8,0.3), "Which domino? (ex.1r/2l)")
        self.boxlabel.setSize(15)
        self.box.draw(win)
        self.boxlabel.draw(win)

    # Draws the domino the user chose in the center of the screen depending on left or right
    def drawcenter(self,win,leftorright):
        if leftorright == "r":
            # These coordinates were made so that at least 8 dominoes could be drawn in the center and not go off the screen
            rightChain = Rectangle(Point(4.6+(0.9*self.rightcount), 4.7), Point(5.4+(0.9*self.rightcount),5.3))
            self.rightcount += 1
            
        else:
            leftChain = Rectangle(Point(3.7+(0.1*self.leftcount), 4.7), Point(4.5+(0.1*self.leftcount)),5.3)
            self.leftcount += 1
            
    ##(IEB) somewhere you read from an Entry box
    # Return the value in the entry box as an integer and string
    def getboxvalue(self):
        return int(self.box.getText()[0]), self.box.getText()[1]

    # Place the first domino in the center of the chain and the screen
    def addcenter(self,win):
        centerRect = Rectangle(Point(4.6, 4.7), Point(5.4,5.3))
        centerRect.draw(win)

    # Check if the left or right number of the domino the user plays matches the left number on the left side of the chain, add to list and return the chain
    def addleft(self,tile):
        if tile.right == self.chain[0].left:
            self.chain.insert(0,tile)
        elif tile.left == self.chain[0].left:
            self.chain.insert(0,tile)
        return self.chain

    # Check if the left or right number of the domino the user plays matches the right number on the right side of the chain, add to list and return the chain
    def addright(self,tile):
        if tile.left == self.chain[len(self.chain)-1].right:
            self.chain.append(tile)
        elif tile.right == self.chain[len(self.chain)-1].right:
            self.chain.append(0,tile)
        return self.chain
    
    # If a player can actually play, check if each side of the tile and side of the chain matches
    def canplay(self,pile):
        for tile in pile:
            if tile.left == self.chain[0] or tile.right == self.chain[0] or self.right == self.chain[len(chain)-1] or tile.left == self.chain[len(chain)-1]:
                return True
        return False

# The Player Class contains the hand of the player     
class Player:
    def __init__(self,name):
        self.name = name
        # The hand is a pile, which is a list
        self.pile = []

    # Method to remove tile from hand
    def removedomino(self,tile):
        self.pile.remove(tile)

    # Method for player to take turn
    def taketurn(self):
        for i in range(len(self.pile)):
            #Have new updated pile after each turn
            print(str(self.pile[i]))
        
# Set up the graphics window with coordinates and return  
def setUpWindow():
    win = GraphWin("Dominoes", 750, 750)
    win.setCoords(0,0,10,10)
    return win

# Create dominoes and do not repeat values from 0-3
def dominoMaker():
    dominoList=[]
    for i in range(0,4):
        for j in range(i,4):
            newDomino = Domino(i,j)
            dominoList.append(newDomino)
    return dominoList

# Shuffle the dominoes by using random
##(RND) where you use a random number generator.
def listShuffle(aList):
    for i in range(len(aList)):
        r = randrange(i,len(aList))
        aList[i], aList[r] = aList[r], aList[i]
    return aList
        

# Main for Dominoes
def playDominoes():

    ##(GW) where you open a GraphWin
    win = setUpWindow()
    dominoes = dominoMaker()

    ##(FNC) somewhere you call a function of your own design
    listShuffle(dominoes)

    ##(LOOD) somewhere you use a list of objects of your own design
    player1 = Player("Player")
    computer = Player("Computer")

    # Distribute 4 dominoes to player and draw to window
    for i in range(5):
        #print(domino.left, domino.right)
        dominoes[i].indexdomino(i+1)
        dominoes[i].draw(win,(2.5/6)*(i+1)+i*1.5, 1)
        player1.pile.append(dominoes[i])

    # Distribute 4 dominoes to computer and draw to window
    for i in range(5,9):
        dominoes[i].indexdomino(i-4)
        dominoes[i].draw(win,(2.5/6)*(i+1)+i*1.5, 9)
        computer.pile.append(dominoes[i])
        
    
    turn = 0
    ##(CLOD) where you define a class of your own design AND somewhere create an object of a class of your own design.
    gamePlay = GamePlay()
    
      # Check if the pile is correct of the player
    print(player1.pile[0].right)
    print(player1.pile[0].left)
##    player1.pile.pop(player1.pile[0].right)
##    print(player1.pile[0].right)
    i=0
    while True: #game loop

        gamePlay.draw(win)
        gamePlay.addcenter(win)
        ##(IMS) somewhere you use the mouse's location
        mouseClick = win.getMouse()
        d1,lr = gamePlay.getboxvalue()


        if d1 == 1:
            print(player1.pile[0].left, player1.pile[0].right)
            i=i+1
        elif d1 == 2:
            print(player1.pile[1].left,player1.pile[1].right)
            i+=1
        elif d1 == 3:
            print(player1.pile[2].left,player1.pile[2].right)
            i+=1
        elif d1 == 4:
            print(player1.pile[3].left,player1.pile[3].right)
            i+=1
        else:
            print(player1.pile[4].left,player1.pile[4].right)
            i+=1
        print(i)

        # Use input/output files
        ##(IFL) somewhere you read from an input file
        games = open("games.txt","r")
        scoresFile = open("scores.txt", "w")
    
        for line in games:
            print(line,end="",file=scoresFile)
        ##(OFL) somewhere you write to an output file
        if i > 4:
            print("game4 win", file=scoresFile)
        else:
            print("game4 lose", file=scoresFile)

    games.close()
    scoresFile.close()
        
##        if lr == "r":
##            gamePlay.drawcenter(win, "r")
        # Switch turns between player and computer
##        if turn == 0:
##                # add center domino piece
##            # if user chooses left 'l'
##            if lr == "r":
##                # know which domino user chooses by knowing which number domino(1-4)
##                dominochoice = gamePlay.addright(player1.pile[d1-1].right) 
##                gamePlay.drawcenter(win, "r",dominochoice)
##            # if user chooses left 'l'
##            elif lr == 'l':
##                dominochoice = gamePlay.addleft(player1.pile[d1-1].left)
##                gamePlay.drawcenter(win, "l",dominochoice)
##            turn = 1



    win.close()
        
playDominoes()
