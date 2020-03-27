################################################
##Final Project COM313
##Date: 2019-11-15
##Created by: Mathieu Vigneault
##
##File Description:
##
##    The file support all the functions that allows the Game 2 main file to run and execute.
##    Most of the functions utilize the Game1_Functions since Game1 and Game2 are similar. 
##    The file also uses the Button and graphics  files to help with object creation and button creation.
##    All these functions are outside of Game2 main to help with organization and shorter Game2 main method.
#################################################

## Other files that this file uses for efficiency ##
from Button import *
from graphics import *
from random import *
from time import *
from Game2_Objects import *
from Game1_Functions import *


## Change the array to the next round and displays it on the GUI ##
def Round_Next2(win, array, scorearray, N, C, U, Round, BigArray, BigArrayScore, HouseArray, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Round_Entry):

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
            array = ChangeAttitude2(array, U, scorearray)
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

## The following function finds the round at which the game reaches an equilibrium ##
## or an absorbing set in other words. User can click on a Button to find out      ##
def Equilibrium_Round2(array, C, U, Equilibrium_Round):

    FakeBigArray = []
    FakeBigArray.append(array)
    Equilibrium_Round = 0
    
    for i in range(1000): ##Run rounds for almost infinite amount
        fakescorearray = ScoreCalc(FakeBigArray[i],C)
        fakearray = ChangeAttitude2(FakeBigArray[i], U, fakescorearray)
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
def AbsorbingSet2(array, scorearray, N, C, U, abset, eqround):

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

## The following method check for the type of neighbor around each individual                          ##
## and average out the payouts depending on the type of neighbors. It then decide                      ##
## if the current individual should turned into the other type of individual or remain the same type.  ##
def ChangeAttitude2(array, U, scorearray):

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
                ## check the neighbors surrounding the selected individual and calculate the average ##
                ## payout of egoists and altruists.                                                  ##
                if(i == (len(array)-2)):
                    if(array[len(array)-2] == "A"):
                        Avalue += scorearray[i-2]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i-2]
                        Bcount += 1
                    if(array[len(array)-1] == "A"):
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
                    if(array[0] == "A"):
                        Avalue += scorearray[0]
                        Acount += 1
                    else:
                        Bvalue += scorearray[0]
                        Bcount += 1
                        
                elif(i == (len(array)-1)):
                    if(array[i-2] == "A"):
                        Avalue += scorearray[i-2]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i-2]
                        Bcount += 1
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
                    if(array[1] == "A"):
                        Avalue += scorearray[1]
                        Acount += 1
                    else:
                        Bvalue += scorearray[1]
                        Bcount += 1
                        
                else:
                    if(array[i-2] == "A"):
                        Avalue += scorearray[i-2]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i-2]
                        Bcount += 1
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
                    if(array[i+2] == "A"):
                        Avalue += scorearray[i+2]
                        Acount += 1
                    else:
                        Bvalue += scorearray[i+2]
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


