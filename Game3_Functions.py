################################################
##Final Project COM313
##Date: 2019-11-15
##Created by: Mathieu Vigneault
##
##File Description:
##
##    The file support all the functions that allows the Game 3 main file to run and execute.
##    Most of the functions utilize the Game1_Functions since Game1 and Game3 are similar. 
##    The file also uses the Button and graphics  files to help with object creation and button creation.
##    All these functions are outside of Game 3 main to help with organization and shorter Game 3 main method.
#################################################

## Other files that this file uses for efficiency ##
from Button import *
from graphics import *
from random import *
from time import *
from Game1_Functions import *
from Game3_Objects import *


## This method just add and remove house images that ##
## are printed on the GUI.                           ##
def HouseArray3_Help1(HouseArray, house_image, i):

    #Check if the Housearray is empty or not
    # if not need to undraw current image before inserting new one
    if(HouseArray[i] != ""):
        HouseArray[i].undraw()
        HouseArray[i] = house_image
    else:
        HouseArray[i] = house_image

## The method below helps with the drawing of the house images on the GUI        ##
## Depending on the number of individuals, the house will be printed differently ##       
def HouseArray3_Help2(N):

    #Original Setting with 30 individuals (max)
    Left_x = 45
    Left_y = 415
    Top_x = 50
    Top_y = 45
    Right_x = 140
    Right_y = 45
    Down_x = 750
    Down_y = 415
    vertical = 6
    horizontal = 9
    vstep = 75
    hstep = 90

    return Left_x, Left_y, Top_x, Top_y, Right_x, Right_y, Down_x, Down_y, vertical, horizontal, vstep, hstep

## The function below finds out which house picture is needed  ##
## and print it out on the GUI                                 ##
def House3_Draw(win, array, N, HouseArray):
    
    ## Receive the parameters from the method above so that the houses are printed at the right spot ##
    Left_x, Left_y, Top_x, Top_y, Right_x, Right_y, Down_x, Down_y, vertical, horizontal, vstep, hstep = HouseArray3_Help2(N)  

    vcount = 0
    hcount = 0
    line = 0
    
    for i in range(len(array)):

        ## Print houses that should face the left side on the screen. ##
        if(vcount < vertical and (line % 2) == 0):
            ## Check if should print an egoist or altruist house ##
            if(array[i] == "A"):
                house_image = Image(Point(Left_x,Left_y), "Images/House2-Left.png")
                house_image.draw(win)
                Left_y -= vstep
                HouseArray3_Help1(HouseArray, house_image, i)
                
            else:
                house_image = Image(Point(Left_x,Left_y), "Images/House1-Left.png")
                house_image.draw(win)
                Left_y -= vstep
                HouseArray3_Help1(HouseArray, house_image, i)

            vcount += 1
            if(vcount == vertical):
                line += 1

        ## Print houses that should face the right side on the screen. ##
        elif(hcount < vertical and (line % 2) != 0):
            ## Check if should print an egoist or altruist house ##
            if(array[i] == "A"):
                house_image = Image(Point(Right_x,Right_y), "Images/House2-Right.png")
                house_image.draw(win)
                Right_y += vstep
                HouseArray3_Help1(HouseArray, house_image, i)    
            else:
                house_image = Image(Point(Right_x,Right_y), "Images/House1-Right.png")
                house_image.draw(win)
                Right_y += vstep
                HouseArray3_Help1(HouseArray, house_image, i)    

            hcount += 1
            if(hcount == vertical):
                line += 1
            if(hcount == vertical and vcount == vertical): ##reset coordinates at right spot##
                vcount = 0
                hcount = 0
                Left_x += (2 * hstep)
                Left_y += (vertical * vstep)
                Right_x += (2 * hstep)
                Right_y -= (vertical * vstep)
                  

    return HouseArray

#################################################

## Change the array to the next round and displays it on the GUI ##
def Round_Next3(win, array, scorearray, N, C, U, Round, BigArray, BigArrayScore, HouseArray, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Round_Entry):

    try:   ## Try, except, and finally
        
        ##Check if the entry is an interger
        round_value = int(Round_Entry.getText())
        
        ##Get rid of the warning message
        warning_text1.setText("")
        
        ##Calculate the score of each agent, then adapt their behavior
        ##End up with calculating population and draw new individuals on GUI
        ##Do the instructions above the number of times specified by user
        ##Add all results inside a big array to store past rounds data
        for i in range(round_value):
            scorearray = ScoreCalc3(array,C)
            array = ChangeAttitude3(array, U, scorearray)
            BigArray.append(array)
            BigArrayScore.append(scorearray)

        HouseArray = House3_Draw(win, array, N, HouseArray)
        Calc_Percentage(array, NumAltruists_text, NumEgoists_text)

        Round += round_value
        RoundNumber_text.setText("Round Number: " + str(Round))

    except ValueError:
        warning_text1.setText("Please Enter an Integer Value")
    finally:
        return array, BigArray, BigArrayScore, HouseArray, Round

## Change the array to the previous round and displays it on the GUI ##
def Round_Previous3(win, array, scorearray, N, C, U, Round, BigArray, BigArrayScore, HouseArray, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Round_Entry):

    try:   ## Try, except, and finally

        ##Check if the entry is an interger
        round_value = int(Round_Entry.getText())

        ##Get rid of the warning message
        warning_text1.setText("")
        
        ## Check for the past array and use it as current array 
        length = int(len(BigArray))
        if(((length-1)-round_value) >= 0):
            newarray = BigArray[((length-1)-round_value)]
        
            ## Remove all preious arrays in the list 
            for i in range(length):
                if(i > (length-round_value-1)):
                    BigArray.remove(BigArray[(len(BigArray)-1)])

        scorearray = ScoreCalc3(newarray,C)
        Calc_Percentage(newarray, NumAltruists_text, NumEgoists_text)
        HouseArray = House3_Draw(win, newarray, N, HouseArray)
        array = newarray

        Round -= round_value
        RoundNumber_text.setText("Round Number: " + str(Round))

    except ValueError:
        warning_text1.setText("Please Enter an Integer Value")
    except IndexError:
        warning_text1.setText("Previous Round Inexistant")
    except UnboundLocalError:
        warning_text1.setText("Previous Round Inexistant")
    finally:
        return array, BigArray, BigArrayScore, HouseArray, Round

## The following function finds the round at which the game reaches an equilibrium ##
## or an absorbing set in other words. User can click on a Button to find out      ##
def Equilibrium_Round3(array, C, U, Equilibrium_Round):

    FakeBigArray = []
    FakeBigArray.append(array)
    Equilibrium_Round = 0
    
    for i in range(1000): ##Run rounds for almost infinite amount
        EQUILIBRIUM = False
        fakescorearray = ScoreCalc3(FakeBigArray[i], C)
        fakearray = ChangeAttitude3(FakeBigArray[i], U, fakescorearray)
        FakeBigArray.append(fakearray) ## add new array inside another big array 

        ##Check different cases where it is possible that we have reach equilibrium
        ##If equilibrium set is reached, then quit and return the round value
        for j in range(len(FakeBigArray)):
            if(j != (len(FakeBigArray)-1) and FakeBigArray[j] == FakeBigArray[len(FakeBigArray)-1]):
                Equilibrium_Round = i
                EQUILIBRIUM = True
                break

        if(EQUILIBRIUM == True):
            break

    return Equilibrium_Round

## The following function use the round at which the game reaches an equilibrium ##
## and look for the number of absorbing set present at that state.               ##
## User can click on a Button to find out                                        ##
def AbsorbingSet3(array, scorearray, C, U, abset, eqround):

    FakeBigArray = []
    FakeBigArray.append(array)

    if(eqround != 0):
        for i in range(eqround): ##Run until it reaches an equilirium round
            fakescorearray = ScoreCalc3(FakeBigArray[i], C)
            fakearray2 = ChangeAttitude3(FakeBigArray[i], U, fakescorearray)
            FakeBigArray.append(fakearray2) ## add new array inside another big array
    else:
        fakearray2 = array


    abset = 0
    ## go through the equilibrium array and check for specific absorbing sets ##
    for j in range(len(fakearray2)):

        ## Various cases of sub absorbing set within the equilibrium/absorbing set ##
        if((j < (len(fakearray2)-1) and (fakearray2[j] == "E") and (fakearray2[j+1] == "A"))):
            #print("Option 1 " + str(j) + str(abset))
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "A") and (fakearray2[j+1] == "A")):
                #print("AEA")
                abset += 1
                
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "E") and (fakearray2[j-2] == "A") and (fakearray2[j+1] == "A")):
                #print("AEEA")
                abset += 1
                
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "E") and (fakearray2[0] == "A") and (fakearray2[j-2] == "E") and (fakearray2[j-3] == "E") and (fakearray2[j-4] == "E") and (fakearray2[j-5] == "A")):
                #print("AEEEEEA")
                abset += 1
                
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "E") and (fakearray2[0] == "E") and (fakearray2[j-2] == "E") and (fakearray2[j-3] == "E") and (fakearray2[j-4] == "E")):
                #print("EEEEEE")
                abset += 1
                break
            
        if((j == (len(fakearray2)-1) and (fakearray2[j] == "E") and (fakearray2[0] == "A"))):
            #print("Option 2 " + str(j) + str(abset))
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "A") and (fakearray2[0] == "A")):
                #print("AEA")
                abset += 1
                
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "E") and (fakearray2[j-2] == "A") and (fakearray2[0] == "A")):
                #print("AEEA")
                abset += 1
                
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "E") and (fakearray2[0] == "A") and (fakearray2[j-2] == "E") and (fakearray2[j-3] == "E") and (fakearray2[j-4] == "E") and (fakearray2[j-5] == "A")):
                #print("AEEEEEA")
                abset += 1
                
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "E") and (fakearray2[0] == "E") and (fakearray2[j-2] == "E") and (fakearray2[j-3] == "E") and (fakearray2[j-4] == "E")):
                #print("EEEEEE")
                abset += 1
                break

    if(abset == 0):
        abset += 1
    
    return abset



## The following method creates an array the same length as number ##
## of individuals in game and fills it with their respective score ##
def ScoreCalc3(array, C):

    ## Creating and Filling the array that keeps track fo the score of all individuals
    scorearray = [0] * len(array)
    
    for i in range(len(scorearray)):

        if(array[i] == "A"):
            count = 0
            ##Checking the left neighbor
            if((array[i-1] == "A") and ((i-1) >= 0) and ((i-1) != (0 or 6 or 12 or 18 or 24 or 30 or 36 or 42 or 48))):
                if(count == 0):
                    scorearray[i] += (1-C)
                    count += 1
                else:
                    scorearray[i] += 1

            if((array[i-1] == "E") and ((i-1) >= 0) and ((i-1) != (0 or 6 or 12 or 18 or 24 or 30 or 36 or 42 or 48))):
                if(count == 0):
                    scorearray[i] += -C
                    count += 1

                
            ##Checking the right neighbor
            if(((i+1) < len(array)) and (array[i+1] == "A") and ((i+1) != (5 or 11 or 17 or 23 or 29 or 35 or 41 or 47 or 53))):
                if(count == 0):
                    scorearray[i] += (1-C)
                    count += 1
                else:
                    scorearray[i] += 1

            if(((i+1) < len(array)) and (array[i+1] == "E") and ((i+1) != (5 or 11 or 17 or 23 or 29 or 35 or 41 or 47 or 53))):
                if(count == 0):
                    scorearray[i] += -C
                    count += 1

            ##Checking for front and back neighborgs
            result = (i % 12)
            if(result >= 6):
                value = ((12 - result) - 1)
            else:
                value = result
            total = 11
            for j in range(value):
                total -= 2
                
            if(result >= 6):
                if((i-total >= 0) and (array[(i-total)] == "A")):
                    if(count == 0):
                        scorearray[i] += (1-C)
                        count += 1
                    else:
                        scorearray[i] += 1

                if(((i+(12-total)) < len(array)) and (array[i+(12-total)] == "A")):
                    if(count == 0):
                        scorearray[i] += (1-C)
                        count += 1
                    else:
                        scorearray[i] += 1
            else:
                if((i-(12-total) >= 0) and (array[i-(12-total)] == "A")):
                    if(count == 0):
                        scorearray[i] += (1-C)
                        count += 1
                    else:
                        scorearray[i] += 1

                if(((i+total) < len(array)) and (array[i+total] == "A")):
                    if(count == 0):
                        scorearray[i] += (1-C)
                        count += 1
                    else:
                        scorearray[i] += 1
                        
        else:
            ##Checking the left neighbor
            if((array[i-1] == "A") and ((i-1) >= 0) and ((i-1) != (5 or 11 or 17 or 23 or 29 or 35 or 41 or 47 or 530 or 6 or 12 or 18 or 24 or 30 or 36 or 42 or 48))):
                scorearray[i] += 1

            ##Checking the right neighbor
            if(((i+1) < len(array)) and (array[i+1] == "A") and ((i+1) != (0 or 6 or 12 or 18 or 24 or 30 or 36 or 42 or 48))):
                scorearray[i] += 1

            ##Checking for front and back neighborgs
            result = (i % 12)
            if(result >= 6):
                value = ((12 - result) - 1)
            else:
                value = result
            total = 11
            for j in range(value):
                total -= 2
                
            if(result >= 6):
                if((i-total >= 0) and (array[(i-total)] == "A")):
                    scorearray[i] += 1

                if(((i+(12-total)) < len(array)) and (array[i+(12-total)] == "A")):
                    scorearray[i] += 1
            else:
                if((i-(12-total) >= 0) and (array[i-(12-total)] == "A")):
                    scorearray[i] += 1

                if(((i+total) < len(array)) and (array[i+total] == "A")):
                    scorearray[i] += 1
        

    return scorearray


## Make the decision based-off the scores of the neighbors ##
## if each house in the array should change its characteristics or not ##
def ChangeAttitude3(array, U, scorearray):

    newarray = [0] * len(array)
    Avalue = 0
    Bvalue = 0
    Acount = 0
    Bcount = 0

    for i in range(len(newarray)):
        value = randrange(1,100)
        if(value <= U):
            Avalue = 0
            Bvalue = 0
            Acount = 0
            Bcount = 0

            if(i == (len(array)-1)):
                ##Checking for the left and right neighbors
                if(array[i-1] == "A"):
                    Avalue += scorearray[i-1]
                    Acount += 1
                else:
                    Bvalue += scorearray[i-1]
                    Bcount += 1
                if(array[i] == "A"):
                    Avalue += scorearray[i]
                    Acount += 1
                else:
                    Bvalue += scorearray[i]
                    Bcount += 1
                if(array[0] == "A"):
                    Avalue += scorearray[0]
                    Acount += 1
                else:
                    Bvalue += scorearray[0]
                    Bcount += 1

                ##Checking for front and back neighborgs
                result = (i % 12)
                if(result >= 6):
                    value = ((12 - result) - 1)
                else:
                    value = result
                total = 11
                for j in range(value):
                    total -= 2
                    
                if(result >= 6):
                    if((i-total >= 0) and (array[(i-total)] == "A")):
                        Avalue += scorearray[i-total]
                        Acount += 1
                    elif((i-total >= 0) and (array[(i-total)] == "E")):
                        Bvalue += scorearray[i-total]
                        Bcount += 1

                    if(((i+(12-total)) < len(array)) and (array[i+(12-total)] == "A")):
                        Avalue += scorearray[i+(12-total)]
                        Acount += 1
                    elif(((i+(12-total)) < len(array)) and (array[i+(12-total)] == "E")):
                        Bvalue += scorearray[i+(12-total)]
                        Bcount += 1
                else:
                    if((i-(12-total) >= 0) and (array[i-(12-total)] == "A")):
                        Avalue += scorearray[i-(12-total)]
                        Acount += 1
                    elif((i-(12-total) >= 0) and (array[i-(12-total)] == "E")):
                        Bvalue += scorearray[i-(12-total)]
                        Bcount += 1

                    if(((i+total) < len(array)) and (array[i+total] == "A")):
                        Avalue += scorearray[i+total]
                        Acount += 1
                    elif(((i+total) < len(array)) and (array[i+total] == "E")):
                        Bvalue += scorearray[i+total]
                        Bcount += 1
                    

            else:
                ##Checking for the left and right neighbors
                if(array[i-1] == "A"):
                    Avalue += scorearray[i-1]
                    Acount += 1
                else:
                    Bvalue += scorearray[i-1]
                    Bcount += 1
                if(array[i] == "A"):
                    Avalue += scorearray[i]
                    Acount += 1
                else:
                    Bvalue += scorearray[i]
                    Bcount += 1
                if(array[i+1] == "A"):
                    Avalue += scorearray[i+1]
                    Acount += 1
                else:
                    Bvalue += scorearray[i+1]
                    Bcount += 1

                ##Checking for front and back neighbors
                result = (i % 12)
                if(result >= 6):
                    value = ((12 - result) - 1)
                else:
                    value = result
                total = 11
                for j in range(value):
                    total -= 2
                    
                if(result >= 6):
                    if((i-total >= 0) and (array[(i-total)] == "A")):
                        Avalue += scorearray[i-total]
                        Acount += 1
                    elif((i-total >= 0) and (array[(i-total)] == "E")):
                        Bvalue += scorearray[i-total]
                        Bcount += 1

                    if(((i+(12-total)) < len(array)) and (array[i+(12-total)] == "A")):
                        Avalue += scorearray[i+(12-total)]
                        Acount += 1
                    elif(((i+(12-total)) < len(array)) and (array[i+(12-total)] == "E")):
                        Bvalue += scorearray[i+(12-total)]
                        Bcount += 1
                else:
                    if((i-(12-total) >= 0) and (array[i-(12-total)] == "A")):
                        Avalue += scorearray[i-(12-total)]
                        Acount += 1
                    elif((i-(12-total) >= 0) and (array[i-(12-total)] == "E")):
                        Bvalue += scorearray[i-(12-total)]
                        Bcount += 1

                    if(((i+total) < len(array)) and (array[i+total] == "A")):
                        Avalue += scorearray[i+total]
                        Acount += 1
                    elif(((i+total) < len(array)) and (array[i+total] == "E")):
                        Bvalue += scorearray[i+total]
                        Bcount += 1

                ## Average out neighbors score to know which kind the specific house should be between altruists and egoists ##
                if(Acount != 0):
                    Avalue = Avalue / Acount
                else:
                    Avalue = Avalue
                if(Bcount != 0):
                    Bvalue = Bvalue / Bcount
                else:
                    Bvalue = Bvalue

                ## Set the individual as an altruists or egoists depending on payouts ##
                if(Avalue > Bvalue):
                    newarray[i] = "A"
                elif(Bvalue > Avalue):
                    newarray[i] = "E"
                else:
                    newarray[i] = array[i]

        else:
            newarray[i] = array[i]

    return newarray

