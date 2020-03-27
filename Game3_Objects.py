################################################
##Final Project COM313
##Date: 2019-11-15
##Created by: Mathieu Vigneault
##
##File Description:
##
##    The file support all the drawing functions for the Game 3 objects.
##    The file also uses the Button and graphics files to help with object creation and button creation.
##    All these functions are outside of main to help with organization and shorter game3 file.
#################################################

## Other files that this file uses for efficiency ##
from Button import *
from graphics import *
from Game1_Objects import *


## The follwing method prints out all the objects ##
## necessary for the game on the GUI.             ##
def Grass_Draw(win):

    grass_image = Image(Point(400,225), "Images/Grass.png") #Create an Image Object
    grass_image.draw(win)

    NumAltruists_text = Text(Point(650,700),"") #Create a Text Object 
    NumAltruists_text.setSize(18)
    NumAltruists_text.setFill("black")
    NumAltruists_text.draw(win)

    NumEgoists_text = Text(Point(650,725),"")
    NumEgoists_text.setSize(18)
    NumEgoists_text.setFill("black")
    NumEgoists_text.draw(win)

    RoundNumber_text = Text(Point(650,675), "Round Number: " + str(0))
    RoundNumber_text.setSize(18)
    RoundNumber_text.setFill("black")
    RoundNumber_text.draw(win)

    Previous_Button = Button(win, Point(575, 600), 100, 25, "Previous") #Create a button 
    Previous_Button.activate()
    
    Next_Button = Button(win, Point(725, 600), 100, 25, "Next") #Create a button 
    Next_Button.activate()

    Round_Entry = Entry(Point(650, 600), 3) #Create a Entry Object 
    Round_Entry.setText(int(1))
    Round_Entry.draw(win)

    warning_text1 = Text(Point(Round_Entry.getAnchor().getX(),(Round_Entry.getAnchor().getY()+35)),"")
    warning_text1.setSize(14)
    warning_text1.draw(win)

    Equilibrium_text = Text(Point(650,750),"")
    Equilibrium_text.setSize(18)
    Equilibrium_text.setFill("black")
    Equilibrium_text.draw(win)

    Absorbing_text = Text(Point(650,775),"")
    Absorbing_text.setSize(18)
    Absorbing_text.setFill("black")
    Absorbing_text.draw(win)

    Instruction_Button = Button(win, Point(400, 550), 100, 50, "Instruction") #Create a button 
    Instruction_Button.activate()
    
    Reset_Button = Button(win, Point(400, 650), 100, 25, "Reset") #Create a button 
    Reset_Button.activate()

    Menu_Button = Button(win, Point(400, 700), 100, 25, "Menu") #Create a button 
    Menu_Button.activate()
    
    Exit_Button = Button(win, Point(400, 750), 100, 25, "Exit") #Create a button 
    Exit_Button.activate()
    
    return grass_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button

## The follwing method deletes all the objects ##
## for the game out of the GUI.                ##
def Grass_Undraw(grass_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button):

    grass_image.undraw() ##Undrawing objects
    NumAltruists_text.undraw()
    NumEgoists_text.undraw()
    RoundNumber_text.undraw()
    warning_text1.undraw()
    Equilibrium_text.undraw()
    Absorbing_text.undraw()
    Previous_Button.deactivate()
    Previous_Button.undraw()
    Next_Button.deactivate()
    Next_Button.undraw()
    Round_Entry.undraw()
    Instruction_Button.deactivate()
    Instruction_Button.undraw()
    Reset_Button.deactivate()
    Reset_Button.undraw()
    Menu_Button.deactivate()
    Menu_Button.undraw()
    Exit_Button.deactivate()
    Exit_Button.undraw()

## Draw All Components of Game 3 ##
def Game3_Draw(win):

    marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2 = GameParameters_Draw(win)
    rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button = Functions_Draw(win)
    grass_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button = Grass_Draw(win)

    N_Entry.setText(int(54)) ##set the number of individuals (N) to 54

    return grass_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button, marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2, rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button


## Undraw All Components of Game 3 ## 
def Game3_Undraw(grass_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button, marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2, rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button, HouseArray):

        Grass_Undraw(grass_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button)
        GameParameters_Undraw(marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2)
        House_Undraw(HouseArray)
        Functions_Undraw(rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button)

