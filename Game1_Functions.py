################################################
##Final Project COM313
##Date: 2019-11-15
##Created by: Mathieu Vigneault
##
##File Description:
##
##    The file support all the functions that allows the Game 1 main file to run and execute.
##    The file also uses the Button and graphics  files to help with object creation and button creation.
##    All these functions are outside of Game1 main to help with organization and shorter Game1 main method.
#################################################

## Other files that this file uses for efficiency ##
from Button import *
from graphics import *
from random import *
from time import *
from Game1_Objects import *

#################################################

## This method just add and remove house images that ##
## are printed on the GUI.                           ##
def HouseArray_Help1(HouseArray, house_image, i):

    #Check if the Housearray is empty or not
    # if not need to undraw current image before inserting new one
    if(HouseArray[i] != ""):
        HouseArray[i].undraw()
        HouseArray[i] = house_image
    else:
        HouseArray[i] = house_image

## The method below helps with the drawing of the house images on the GUI        ##
## Depending on the number of individuals, the house will be printed differently ##       
def HouseArray_Help2(N):

    #Original Setting with 30 individuals (max)
    Left_x = 50
    Left_y = 330
    Top_x = 50
    Top_y = 45
    Right_x = 750
    Right_y = 120
    Down_x = 750
    Down_y = 415
    horizontal = 11
    step = 70

    #Modify settings so that house are closer to lake and more spread out depending on N
    if(N <= 22):

        Left_x = 190
        Top_x = 190
        Right_x = 610
        Down_x = 610
        horizontal = 1
        step = 0
        
        if(N <= 4):
            Left_y -= 70
            Top_x += 210
            Right_y += 140
            Down_x -= 210
            
        elif(N > 4 and N <= 8):
            Top_x += 140
            Down_x -= 140
            horizontal = 2
            step = 140
            
        elif(N > 8 and N <= 11):
            horizontal = 3
            step = 140
            
        else:
            horizontal = 7
            step = 70

    if(N > 22 and N <= 28):

        Left_x = 120
        Top_x = 120
        Right_x = 680
        Down_x = 680
        if(N < 24):
            horizontal = 8
        else:
            horizontal = 9

    return Left_x, Left_y, Top_x, Top_y, Right_x, Right_y, Down_x, Down_y, horizontal, step

## The function below finds out which house picture is needed  ##
## and print it out on the GUI                                 ##
def House_Draw(win, array, N, HouseArray):
    
    Left_x, Left_y, Top_x, Top_y, Right_x, Right_y, Down_x, Down_y, horizontal, step = HouseArray_Help2(N)  

    if(step == 70):
        left = 3 
        top = horizontal + left
        right = top + left + 1
        down = right + horizontal
    elif(step == 0):
        left = 0 
        top = horizontal + left
        right = top + left + 1
        down = right + horizontal
    else:
        left = 1
        top = horizontal + left
        right = top + left + 1
        down = right + (horizontal/2)
    
    for i in range(len(array)):
        if(i <= left):
            if(array[i] == "A"):
                house_image = Image(Point(Left_x,Left_y), "Images/House2-Left.png") ##Draw the right type of house image onto the GUI
                house_image.draw(win) 
                Left_y -= step
                HouseArray_Help1(HouseArray, house_image, i) ## add image into an array to be able to undraw image later
                
            else:
                house_image = Image(Point(Left_x,Left_y), "Images/House1-Left.png")
                house_image.draw(win)
                Left_y -= step
                HouseArray_Help1(HouseArray, house_image, i)    
        elif(i > top and i <= right):
            if(array[i] == "A"):
                house_image = Image(Point(Right_x,Right_y), "Images/House2-Right.png")
                house_image.draw(win)
                Right_y += step
                HouseArray_Help1(HouseArray, house_image, i)    
            else:
                house_image = Image(Point(Right_x,Right_y), "Images/House1-Right.png")
                house_image.draw(win)
                Right_y += step
                HouseArray_Help1(HouseArray, house_image, i)    
                
        elif(i > left and i <= top):
            if(array[i] == "A"):
                house_image = Image(Point(Top_x,Top_y), "Images/House2-Top.png")
                house_image.draw(win)
                Top_x += step
                HouseArray_Help1(HouseArray, house_image, i)    
            else:
                house_image = Image(Point(Top_x,Top_y), "Images/House1-Top.png")
                house_image.draw(win)
                Top_x += step
                HouseArray_Help1(HouseArray, house_image, i)    

        else:
            if(array[i] == "A"):
                house_image = Image(Point(Down_x,Down_y), "Images/House2-Down.png")
                house_image.draw(win)
                Down_x -= step
                HouseArray_Help1(HouseArray, house_image, i)    
            else:
                house_image = Image(Point(Down_x,Down_y), "Images/House1-Down.png")
                house_image.draw(win)
                Down_x -= step
                HouseArray_Help1(HouseArray, house_image, i)    

    return HouseArray

#################################################

## The following function builds an array of altruists and egoists at random ## 
def RandomGenerate(N, composition):

    array = []

    ## Generate a random number between 0 and 99 and depending on over or under 49
    ## An algoist or egoist is appended tothe array
    for i in range(N):
        value = randrange(0,99)
        if(value < composition):
            array.append("A")
        else:
            array.append("E")

    return array

## This function keeps track of the number of altruists and egoists inside the game   ##
## It also prints out the number of each type of player for the current round         ## 
def Calc_Percentage(array, NumAltruists_text, NumEgoists_text):

    Num_Altruists = 0
    Num_Egoists = 0

    #Go through the array of individuals
    #and count number of egoists and altruists
    for i in range(len(array)):
        if(array[i] == "A"):
            Num_Altruists += 1
        else:
            Num_Egoists += 1

    Percentage_A = (Num_Altruists / (Num_Altruists + Num_Egoists)) * 100
    Percentage_B = (Num_Egoists / (Num_Altruists + Num_Egoists)) * 100

    NumAltruists_text.setText("Altruists: " + str(Num_Altruists))
    NumEgoists_text.setText("Egoists: " + str(Num_Egoists))
    

## The following method creates an array the same length as number ##
## of individuals in game and fills it with their respective score ##
def ScoreCalc(array, C):

    ## Creating and Filling the array that keeps track fo the score of all individuals
    scorearray = [0] * len(array)
    
    for i in range(len(scorearray)):

        if(i == len(array)-1):
            if(array[i] == "A"):
                ##Checking the left neighbor
                if(array[i-1] == "A"):
                    scorearray[i] = scorearray[i] + (1-C)

                    ##Checking the right neighbor
                    if(array[0] == "A"):
                        scorearray[i] = scorearray[i] + 1
                    else:
                        scorearray[i] = scorearray[i] 
                    
                else:
                    scorearray[i] = scorearray[i] - C
                    
                    ##Checking the right neighbor
                    if(array[0] == "A"):
                        scorearray[i] = scorearray[i] + 1
                    else:
                        scorearray[i] = scorearray[i]
            else:
                ##Checking the left neighbor
                if(array[i-1] == "A"):
                    scorearray[i] = scorearray[i] + 1
                else:
                    scorearray[i] = scorearray[i] + 0

                ##Checking the right neighbor
                if(array[0] == "A"):
                    scorearray[i] = scorearray[i] + 1
                else:
                    scorearray[i] = scorearray[i] + 0

        else:
            if(array[i] == "A"):
                ##Checking the left neighbor
                if(array[i-1] == "A"):
                    scorearray[i] = scorearray[i] + (1-C)

                    ##Checking the right neighbor
                    if(array[i+1] == "A"):
                        scorearray[i] = scorearray[i] + 1
                    else:
                        scorearray[i] = scorearray[i] 
                    
                else:
                    scorearray[i] = scorearray[i] - C

                    ##Checking the right neighbor
                    if(array[i+1] == "A"):
                        scorearray[i] = scorearray[i] + 1
                    else:
                        scorearray[i] = scorearray[i]
            else:
                ##Checking the left neighbor
                if(array[i-1] == "A"):
                    scorearray[i] = scorearray[i] + 1
                else:
                    scorearray[i] = scorearray[i] + 0

                ##Checking the right neighbor
                if(array[i+1] == "A"):
                    scorearray[i] = scorearray[i] + 1
                else:
                    scorearray[i] = scorearray[i] + 0

    scorearray2 = [0] * len(scorearray)

    for j in range(len(scorearray2)):
        if(j == 0):
            scorearray2[j] = scorearray

    return scorearray

## The following method check for the type of neighbor around each individual                          ##
## and average out the payouts depending on the type of neighbors. It then decide                      ##
## if the current individual should turned into the other type of individual or remain the same type.  ##
def ChangeAttitude1(array, U, scorearray):

    ## Setup some variables to calculate the egoist and altruist scores for a specific individual ##
    newarray = [0] * len(array)
    Avalue = 0
    Bvalue = 0
    Acount = 0
    Bcount = 0

    ## Go through the whole list of individuals ##
    for i in range(len(newarray)):
        value = randrange(1,100)
        if(value <= U):
    
            for i in range(len(array)):
                Avalue = 0
                Bvalue = 0
                Acount = 0
                Bcount = 0
                if(i == 0):
                    ## check the neighbors surrounding the selected individual and calculate the average ##
                    ## payout of egoists and altruists.                                                  ##
                    if(array[len(array)-1] == "A"):
                        Avalue += scorearray[len(array)-1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[len(array)-1]
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
                elif(i == (len(array)-1)):
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
                else:
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

                ## Average out the payouts of egoists and altruists. ##
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


## Change the array to the next round and displays it on the GUI ##
def Round_Next(win, array, scorearray, N, C, U, Round, BigArray, BigArrayScore, HouseArray, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Round_Entry):

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
            scorearray = ScoreCalc(array,C)
            array = ChangeAttitude1(array, U, scorearray)
            BigArray.append(array)
            BigArrayScore.append(scorearray)

        HouseArray = House_Draw(win, array, N, HouseArray)
        Calc_Percentage(array, NumAltruists_text, NumEgoists_text)

        Round += round_value
        RoundNumber_text.setText("Round Number: " + str(Round))

    except ValueError:
        warning_text1.setText("Please Enter an Integer Value")
    finally:
        return array, BigArray, BigArrayScore, HouseArray, Round


## Change the array to the previous round and displays it on the GUI ##
def Round_Previous(win, array, scorearray, N, C, U, Round, BigArray, BigArrayScore, HouseArray, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Round_Entry):

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

        scorearray = ScoreCalc(newarray,C)
        Calc_Percentage(newarray, NumAltruists_text, NumEgoists_text)
        HouseArray = House_Draw(win, newarray, N, HouseArray)
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
def Equilibrium_Round(array, C, U, Equilibrium_Round):

    FakeBigArray = []
    FakeBigArray.append(array)
    Equilibrium_Round = 0
    
    for i in range(1000): ##Run rounds for almost infinite amount
        fakescorearray = ScoreCalc(FakeBigArray[i],C)
        fakearray = ChangeAttitude1(FakeBigArray[i], U, fakescorearray)
        FakeBigArray.append(fakearray) ## add new array inside another big array 

        ##Check different cases where it is possible that we have reach equilibrium
        ##If equilibrium set is reached, then quit and return the round value
        if(i-1 >=0 and i-2 <0):
            if(FakeBigArray[i] == FakeBigArray[i-1]):
                Equilibrium_Round = i-1
                break
        if(i-2 >=0 and i-1 >=0):
            if(FakeBigArray[i] == FakeBigArray[i-1]):
                Equilibrium_Round = i-1
                break
            if(FakeBigArray[i] == FakeBigArray[i-2]):
                Equilibrium_Round = i-1
                break

    return Equilibrium_Round

## The following function use the round at which the game reaches an equilibrium ##
## and look for the number of absorbing set present at that state.               ##
## User can click on a Button to find out                                        ##
def AbsorbingSet1(array, scorearray, N, C, U, abset, eqround):

    FakeBigArray = []
    FakeBigArray.append(array)

    if(eqround != 0):
        for i in range(eqround): ##Run until it reaches an equilirium round
            fakescorearray = ScoreCalc(FakeBigArray[i],C)
            fakearray2 = ChangeAttitude1(FakeBigArray[i], U, fakescorearray)
            FakeBigArray.append(fakearray2) ## add new array inside another big array
    else:
        fakearray2 = array


    abset = 0
    for j in range(len(fakearray2)):

        if((j < (len(fakearray2)-1) and (fakearray2[j] == "E") and (fakearray2[j+1] == "A"))):
            #print("Option 1 " + str(j))
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "A") and (fakearray2[j+1] == "A")):
                #print("AEA")
                abset += 1
                
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "E") and (fakearray2[j-2] == "A") and (fakearray2[j+1] == "A")):
                #print("AEEA")
                abset += 1
                
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "E") and (fakearray2[j+1] == "A") and (fakearray2[j-2] == "E") and (fakearray2[j-3] == "A")):
                #print("AEEEA")
                abset += 1
                
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "E") and (fakearray2[j+1] == "E") and (fakearray2[j-2] == "E") and (fakearray2[j-3] == "E")):
                #print("EEEEE")
                abset += 1
                break
            
        if((j == (len(fakearray2)-1) and (fakearray2[j] == "E") and (fakearray2[0] == "A"))):
            #print("Option 2 " + str(j))
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "A") and (fakearray2[0] == "A")):
                #print("AEA")
                abset += 1
                
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "E") and (fakearray2[j-2] == "A") and (fakearray2[0] == "A")):
                #print("AEEA")
                abset += 1
                
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "E") and (fakearray2[0] == "A") and (fakearray2[j-2] == "E") and (fakearray2[j-3] == "A")):
                #print("AEEEA")
                abset += 1
                
            if((fakearray2[j] == "E") and (fakearray2[j-1] == "E") and (fakearray2[0] == "E") and (fakearray2[j-2] == "E") and (fakearray2[j-3] == "E")):
                #print("EEEEE")
                abset += 1
                break

    if(abset == 0):
        abset += 1
    
    return abset

