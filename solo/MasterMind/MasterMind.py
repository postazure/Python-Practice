import random

def selectColors():
    for i in range(4):
        hiddenColorList[i] = random.choice(colorKey)
        
        
def getGuess():
    i = 0
    for looper in hiddenColorList:
        currentGuess[i] = raw_input(str(i+1) + ". Color:")
        i += 1

        
def checkGuess():
    global correctColor,correctSpot, correctSpotNum
    correctColor = 0
    correctSpot = [0,0,0,0]
    correctSpotNum = 0
       
    i = 0
    for guess in currentGuess:
        if guess == hiddenColorList[i]:
            correctSpot[i] = 1
            correctSpotNum += 1            
        i += 1
    
    for guess in currentGuess:
        
        j = 0    #for loop to check all of j's
        for color in hiddenColorList:
            if correctSpot[j] == 0:
                if guess == color:
                    correctColor += 1
                    correctSpot[j] = 1
            
            j += 1



#-----------Setup
colorKey = ["blue","green","pink","red"]
hiddenColorList = [0,0,0,0]
currentGuess = [0,0,0,0]

selectColors()
print "Guess the 4 colors that the computer has selected in order.\n Your options are: "
print colorKey

#-----------Main
running = 1
while running<12:
    print "\n \n \n_________________________\nThis is guess number", running
    getGuess()
    checkGuess()
    print "Your Results for:",
    print currentGuess
    print "Color & Spot: ", correctSpotNum,
    print " Color Only: ", correctColor
    running += 1
    if correctSpotNum == 4:
        print "\n \n \n"
        print "**********************"
        print ">>>>>>>You Win<<<<<<<<"
        print "**********************"
        running = 100
    if running == 12:
        print "\n \n \n"
        print "You Lose :("
        print "The correct answer was ", hiddenColorList
