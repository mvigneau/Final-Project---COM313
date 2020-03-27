################################################
##Final Project COM313
##Date: 2019-11-15
##Created by: Mathieu Vigneault
##
##File Description:
##
##    The file is used as a "main" for Game 1 as it takes care of all the logical aspect while inside Game 1.
##    The file also uses the Game1_Function file for calling various functions and the Game1_objects to add objects to the window etc.
##    The file is linked to the actual main function where it is called when Game 1 is being played.
#################################################

## Other files that this file uses for efficiency ##
from Button import *
from graphics import *
from random import *
from time import *
from Game1_Objects import *
from Game1_Functions import *


## The method below generates a random set of agents,        ##
## then it calculate the score and draw it on the GUI        ##
## It is called every time the game is reset or initialize.  ##
def Start1(win, N, C, U, abset, eqround, BigArray, BigArrayScore, HouseArray, Composition, NumAltruists_text, NumEgoists_text, Equilibrium_text, RoundNumber_text):

    RoundNumber_text.setText("Round Number: " + str(0))
    House_Undraw(HouseArray)
    array = RandomGenerate(N, Composition) ##creating an array of individuals
    scorearray = ScoreCalc(array,C) ##calculates the score of each individual
    HouseArray = House_Draw(win, array, N, HouseArray) ##draw the houses in the neighborhood
    Calc_Percentage(array, NumAltruists_text, NumEgoists_text) ##calculates the % of altruists versus egoists
    BigArray.append(array)
    BigArrayScore.append(scorearray)
    eqround = Equilibrium_Round(array, C, U, eqround) ##find the equilibrium of the given neighborhood
    abset = AbsorbingSet1(array, scorearray, N, C, U, abset, eqround) ##find the number of sub absorbing set at equilibrium in the given neighborhood

    return array, scorearray, BigArray, BigArrayScore, HouseArray, eqround, abset


## The following function finds the number of underlying subsets          ##
## in the current given set of individuals. (Not used in current version) ##
def AbsorbingSet(array, BigArray):

    
    for i in range(len(array)):

        count = 0

        if((array[i] == "A") and (array[i-1] != "A") and (i+1 != len(array))):
            count += 1
            j = i+1
            
            if(j < len(array)):
                while((j < len(array)) and (array[j] == "A")):
                    count += 1
                    j += 1

        elif((i+1 == len(array)) and (array[i] == "A")):
            count += 1


## The following function check if the various important game parameters  the number of underlying subsets ##
## are properly set and if the user are inserting valid information                                        ##              
def Important_Parameters(win, N_Entry, C_Entry, U_Entry, Composition_Entry, HouseArray, warning_text2):

    ### Important parameters for the game ###

    while(True):
        try:   ## Try, except, and finally
            N = int(N_Entry.getText())    ## Number of Individuals inside the game
            if(N <= 2 or N >30):
                raise ValueError(warning_text2.setText("Please Enter a Value Between 3 & 30"))

            C = float(C_Entry.getText())   ## Cost for  providing public good for altruists   
            if(C < 0 or C > 1):
                raise ValueError(warning_text2.setText("Please Enter a Value Between 0 & 1"))
            
            U = int(U_Entry.getText())    ## Probability to not retain a strategy for an agent in %
            if(U < 0 or U > 100):
                raise ValueError(warning_text2.setText("Please Enter a Value Between 0 & 100"))

            Composition = int(Composition_Entry.getText()) ## Composition of Altruists inside the game
            if(Composition < 0 or Composition > 100):
                raise ValueError(warning_text2.setText("Please Enter a Value Between 0 & 100"))

            Round = 0
            BigArray = [] ## Hold all the different arrays generated every turn
            BigArrayScore = [] ## Hold all the different arrays generated every turn
            House_Undraw(HouseArray)
            HouseArray = [""] * N
            eqround = 0
            abset = 0

            break
            
        except ValueError:
            warning_text2.setText("Please Enter a Correct Integer Value") ##warning to the user that some incorrect value/information has been inserted
            pt = win.getMouse()
        except TypeError:
            warning_text2.setText("Please Enter a Correct Integer Value")
            pt = win.getMouse()

    return N, C, U, Round, BigArray, BigArrayScore, Composition, HouseArray, eqround, abset


## This is the function that handles allow the button logic in the game ##
## It allows the game to be played in an efficient manner and let the user do what he/she desires ##
def Game1(win):

    ### Draw Game 1 ###
    lake_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button, marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2, rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button = Game1_Draw(win)

    ### Set Important Parameters ###
    HouseArray = [""]
    N, C, U, Round, BigArray, BigArrayScore, Composition, HouseArray, eqround, abset = Important_Parameters(win, N_Entry, C_Entry, U_Entry, Composition_Entry, HouseArray, warning_text2)

    ### Initializing the Game (Population + Calculations) ###
    array, scorearray, BigArray, BigArrayScore, HouseArray, eqround, abset = Start1(win, N, C, U, abset, eqround, BigArray, BigArrayScore, HouseArray, Composition, NumAltruists_text, NumEgoists_text, Equilibrium_text, RoundNumber_text)

    pt = win.getMouse()
    
    while(Menu_Button.isClicked(pt) == False):
        while(Reset_Button.isClicked(pt) == False):

            ## Check if the next button is clicked and if so it prints out the next state of the neighborhood in the GUI ##
            if(Next_Button.isClicked(pt)):
                array, BigArray, BigArrayScore, HouseArray, Round = Round_Next(win, array, scorearray, N, C, U, Round, BigArray, BigArrayScore, HouseArray, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Round_Entry)

            ## Check if the previous button is clicked and if so it prints out the previous state of the neighborhood in the GUI ##
            elif(Previous_Button.isClicked(pt)):
                array, BigArray, BigArrayScore, HouseArray, Round = Round_Previous(win, array, scorearray, N, C, U, Round, BigArray, BigArrayScore, HouseArray, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Round_Entry)

            ## Display the round number at which equilibrium is reached onto the GUI ##
            elif(Equilibrium_Button.isClicked(pt)):
                Equilibrium_text.setText("Equilibrium Round: " + str(eqround))

            ## Display the number of sub absorbing sets with the neighborhood at equilibrium onto the GUI ##
            elif(AbsorbingSet_Button.isClicked(pt)):
                Absorbing_text.setText("Absorbing Sets: " + str(abset))

            elif(Instruction_Button.isClicked(pt)):
                ## Draw an Instruction Interface ##
                marble2_image, instruction_title, text1, text2, text3, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7, title8, label8, title9, label9, title10, label10, title11, label11 = Instruction_Draw(win, N_Entry, C_Entry, U_Entry, Composition_Entry, Round_Entry)
                pt2 = win.getMouse()
                ## Undraw Instruction Interface ##
                Instruction_Undraw(win, N_Entry, C_Entry, U_Entry, Composition_Entry, Round_Entry, marble2_image, instruction_title, text1, text2, text3, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7, title8, label8, title9, label9, title10, label10, title11, label11)

            elif(Menu_Button.isClicked(pt)):
                break
            
            elif(Exit_Button.isClicked(pt)):
                ## Closes and ends the program ##
                win.close()
                sys.exit()

            pt = win.getMouse()

        if(Menu_Button.isClicked(pt)):
            break

        Equilibrium_text.setText("")
        Absorbing_text.setText("")
  
        ### Set Important Parameters ###
        N, C, U, Round, BigArray, BigArrayScore, Composition, HouseArray, eqround, abset = Important_Parameters(win, N_Entry, C_Entry, U_Entry, Composition_Entry, HouseArray, warning_text2)

        ### Initializing the Game (Population + Calculations) ###
        array, scorearray, BigArray, BigArrayScore, HouseArray, eqround, abset = Start1(win, N, C, U, abset, eqround, BigArray, BigArrayScore, HouseArray, Composition, NumAltruists_text, NumEgoists_text, Equilibrium_text, RoundNumber_text)

        pt = win.getMouse()

        if(Menu_Button.isClicked(pt)):
            break
        if(Exit_Button.isClicked(pt)):
            ## Closes and ends the program ##
            win.close()
            sys.exit()

    if(Menu_Button.isClicked(pt)):
        ## Undraw All Components of Game 1 ## 
        Game1_Undraw(lake_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button, marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2, HouseArray, rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button)
    if(Exit_Button.isClicked(pt)):
        ## Closes and ends the program ##
        win.close()
        sys.exit()



