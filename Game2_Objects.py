################################################
##Final Project COM313
##Date: 2019-11-15
##Created by: Mathieu Vigneault
##
##File Description:
##
##    The file support all the drawing functions for the Game 2 objects.
##    The file also uses the Button and graphics files to help with object creation and button creation.
##    All these functions are pulled from Game1_Objects file since the Game 2 GUI doesn't vary at all.
#################################################

## Other files that this file uses for efficiency ##
from Button import *
from graphics import *
from Game1_Objects import *

## Draw All Components of Game 2 ##
def Game2_Draw(win):

    lake_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button, marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2, rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button = Game1_Draw(win)
    return lake_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button, marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2, rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button


## Undraw All Components of Game 2 ## 
def Game2_Undraw(lake_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button, marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2, HouseArray, rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button):

    Game1_Undraw(lake_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button, marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2, HouseArray, rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button)
