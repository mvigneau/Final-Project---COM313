################################################
##Final Project COM313
##Date: 2019-11-15
##Created by: Mathieu Vigneault
##
##File Description:
##
##    The file support all the drawing functions for the Game 1 objects.
##    The file also uses the Button and graphics files to help with object creation and button creation.
##    All these functions are outside of main to help with organization and shorter game1 file.
#################################################

## Other files that this file uses for efficiency ##
from Button import *
from graphics import *

## The follwing method prints out all parameters objects ##
## necessary for the game on the GUI.                    ##
def GameParameters_Draw(win):

    marble_image = Image(Point(400,400), "Images/marble.png") #Create an Image Object
    marble_image.draw(win)

    rect1 = Rectangle(Point(0, 392),Point(335, 657)) #Create a rectangle object
    rect1.setFill("Black")
    rect1.draw(win)

    steel_image = Image(Point(150,525), "Images/Steel.png") #Create an Image Object
    steel_image.draw(win)

    GameParameters_text = Text(Point(165, 485),"Game Parameters")
    GameParameters_text.setSize(20)
    GameParameters_text.draw(win)
    
    N_Entry = Entry(Point(250, 525), 3) #Create a Entry Object 
    N_Entry.setText(int(30))
    N_Entry.draw(win)

    N_text = Text(Point((N_Entry.getAnchor().getX()-105),N_Entry.getAnchor().getY()),"Number of Individuals (N):")
    N_text.setSize(14)
    N_text.draw(win)
    
    C_Entry = Entry(Point(250, 550), 3) #Create a Entry Object 
    C_Entry.setText(float(1/4))
    C_Entry.draw(win)

    C_text = Text(Point((C_Entry.getAnchor().getX()-125),C_Entry.getAnchor().getY()),"Cost of Altruists (C):")
    C_text.setSize(14)
    C_text.draw(win)
    
    U_Entry = Entry(Point(250, 575), 3) #Create a Entry Object 
    U_Entry.setText(int(100))
    U_Entry.draw(win)

    U_text = Text(Point((U_Entry.getAnchor().getX()-108),U_Entry.getAnchor().getY()),"Prob. Following Rule (U):")
    U_text.setSize(14)
    U_text.draw(win)

    Composition_Entry = Entry(Point(250, 600), 3) #Create a Entry Object 
    Composition_Entry.setText(int(50))
    Composition_Entry.draw(win)

    Composition_text = Text(Point((Composition_Entry.getAnchor().getX()-125),Composition_Entry.getAnchor().getY()),"Game Composition:")
    Composition_text.setSize(14)
    Composition_text.draw(win)

    warning_text2 = Text(Point(165, Composition_Entry.getAnchor().getY()+35),"")
    warning_text2.setSize(14)
    warning_text2.draw(win)

    return marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2

## The follwing method deletes all the game parameters ##
## objects for the game out of the GUI.                ##
def GameParameters_Undraw(marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2):

    marble_image.undraw()
    rect1.undraw()
    steel_image.undraw()
    GameParameters_text.undraw()
    N_Entry.undraw()
    N_text.undraw()
    C_Entry.undraw()
    C_text.undraw()
    U_Entry.undraw()
    U_text.undraw()
    Composition_Entry.undraw()
    Composition_text.undraw()
    warning_text2.undraw()

## The follwing method prints out all the objects ##
## necessary for the game on the GUI.             ##
def LakeHouse_Draw(win):

    lake_image = Image(Point(400,225), "Images/Lake2.png") #Create an Image Object
    lake_image.draw(win)

    NumAltruists_text = Text(Point(400,225),"") #Create a Text Object 
    NumAltruists_text.setSize(18)
    NumAltruists_text.setFill("white")
    NumAltruists_text.draw(win)

    NumEgoists_text = Text(Point(400,200),"")
    NumEgoists_text.setSize(18)
    NumEgoists_text.setFill("white")
    NumEgoists_text.draw(win)

    RoundNumber_text = Text(Point(400,175), "Round Number: " + str(0))
    RoundNumber_text.setSize(18)
    RoundNumber_text.setFill("white")
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

    Equilibrium_text = Text(Point(400,300),"")
    Equilibrium_text.setSize(18)
    Equilibrium_text.setFill("white")
    Equilibrium_text.draw(win)

    Absorbing_text = Text(Point(400,325),"")
    Absorbing_text.setSize(18)
    Absorbing_text.setFill("white")
    Absorbing_text.draw(win)

    Instruction_Button = Button(win, Point(400, 550), 100, 50, "Instruction") #Create a button 
    Instruction_Button.activate()
    
    Reset_Button = Button(win, Point(400, 650), 100, 25, "Reset") #Create a button 
    Reset_Button.activate()

    Menu_Button = Button(win, Point(400, 700), 100, 25, "Menu") #Create a button 
    Menu_Button.activate()
    
    Exit_Button = Button(win, Point(400, 750), 100, 25, "Exit") #Create a button 
    Exit_Button.activate()

    
    return lake_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button

## The follwing method deletes all the objects ##
## for the game out of the GUI.                ##
def LakeHouse_Undraw(lake_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button):

    lake_image.undraw()
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

## The follwing method deletes all the house ##
## images around the lake out of the GUI.    ##
def House_Undraw(HouseArray):

    ##Go through the list and undraw every house
    ##object inside the list
    for i in range(len(HouseArray)):
        if(HouseArray[i] != ""):
            HouseArray[i].undraw()



def Functions_Draw(win):

    rect2 = Rectangle(Point(800, 392),Point(465, 657)) #Create a rectangle object
    rect2.setFill("Black")
    rect2.draw(win)

    steel_image2 = Image(Point(650,525), "Images/Steel.png") #Create an Image Object
    steel_image2.draw(win)

    GameFunctions_text = Text(Point(650, 485),"Possible Functions")
    GameFunctions_text.setSize(20)
    GameFunctions_text.draw(win)

    Equilibrium_Button = Button(win, Point(575, 535), 100, 25, "Equilibrium") #Create a button 
    Equilibrium_Button.activate()

    AbsorbingSet_Button = Button(win, Point(725, 535), 100, 25, "Absorbing Set") #Create a button 
    AbsorbingSet_Button.activate()

    return rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button


def Functions_Undraw(rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button):

    rect2.undraw()
    steel_image2.undraw()
    GameFunctions_text.undraw()
    Equilibrium_Button.deactivate()
    Equilibrium_Button.undraw()
    AbsorbingSet_Button.deactivate()
    AbsorbingSet_Button.undraw()


def Instruction_Draw(win, N_Entry, C_Entry, U_Entry, Composition_Entry, Round_Entry):

    N_Entry.undraw()
    C_Entry.undraw()
    U_Entry.undraw()
    Composition_Entry.undraw()
    Round_Entry.undraw()
    
    marble2_image = Image(Point(400,400), "Images/marble.png") #Create an Image Object
    marble2_image.draw(win)

    instruction_title = Text(Point(400, 25), "INSTRUCTIONS")
    instruction_title.setSize(28)
    instruction_title.setStyle("bold")
    instruction_title.draw(win)

    text1 = Text(Point(400, 600), "Generic Buttons")
    text1.setSize(18)
    text1.setStyle("bold")
    text1.draw(win)

    title1 = Text(Point(400, text1.getAnchor().getY()+25), "Reset Button")
    title1.setSize(16)
    title1.draw(win)

    label1 = Text(Point(400, title1.getAnchor().getY()+25), "The button resets to a new game with a new population, specified and valid parameters.")
    label1.draw(win)

    title2 = Text(Point(400, label1.getAnchor().getY()+25), "Menu Button")
    title2.setSize(16)
    title2.draw(win)

    label2 = Text(Point(400, title2.getAnchor().getY()+30), "The button will take you back to the main menu or introduction, where you can select which game you want to play again.\nIt should be used if you want to experience another one of the games.")
    label2.draw(win)

    title3 = Text(Point(400, label2.getAnchor().getY()+30), "Exit Button")
    title3.setSize(16)
    title3.draw(win)

    label3 = Text(Point(400, title3.getAnchor().getY()+25), "The exit button will terminate the program and close the GUI.")
    label3.draw(win)

    text2 = Text(Point(400, 325), "Game Functions Buttons")
    text2.setSize(18)
    text2.setStyle("bold")
    text2.draw(win)
    
    title4 = Text(Point(400, text2.getAnchor().getY()+25), "Next Button")
    title4.setSize(16)
    title4.draw(win)

    label4 = Text(Point(400, title4.getAnchor().getY()+30), "The button will show the composition of the population at the next “x” iteration.\nIt allows you to visually see how the population evolves over time as well as the number of altruists and egoists. (default: x = 1)")
    label4.draw(win)

    title5 = Text(Point(400, label4.getAnchor().getY()+25), "Previous Buttons")
    title5.setSize(16)
    title5.draw(win)

    label5 = Text(Point(400, title5.getAnchor().getY()+35), "The button will show the composition of the population at the previous “x” iteration.\nIt allows you to visually see how the population evolves over time as well as the number of altruists and egoists. (default: x = 1).\nIf the previous does not exist, it will tell you.")
    label5.draw(win)

    title6 = Text(Point(400, label5.getAnchor().getY()+35), "Equilibrium Button")
    title6.setSize(16)
    title6.draw(win)

    label6 = Text(Point(400, title6.getAnchor().getY()+30), "The button will display an integer that denotes the number of rounds it takes for the population to reach\nan equilibrium in the current game or in other words an absorbing set for the entire population.")
    label6.draw(win)
    
    title7 = Text(Point(400, label6.getAnchor().getY()+30), "Absorbing Set Button")
    title7.setSize(16)
    title7.draw(win)

    label7 = Text(Point(400, title7.getAnchor().getY()+25), "The button will show how many “sub” absorbing sets within the absorbing set for the population at the equilibrium round itself. ")
    label7.draw(win)

    text3 = Text(Point(400, 75), "Game Parameters Buttons")
    text3.setSize(18)
    text3.setStyle("bold")
    text3.draw(win)

    title8 = Text(Point(400, text3.getAnchor().getY()+25), "Number of Individuals (N) Entry Box")
    title8.setSize(16)
    title8.draw(win)

    label8 = Text(Point(400, title8.getAnchor().getY()+25), "The entry box denotes the number of agents (houses) in the program. The maximum number is 30 and the minimum is 3.\nIf any other value is inserted, you will have an error message until you fix it.")
    label8.draw(win)
    
    title9 = Text(Point(400, label8.getAnchor().getY()+25), "Cost of Altruists (C) Entry Box")
    title9.setSize(16)
    title9.draw(win)

    label9 = Text(Point(400, title9.getAnchor().getY()+25), "The entry box takes in a float between 0 and 1. The cost of altruists represent the cost it takes for the altruists to share the public good.")
    label9.draw(win)

    title10 = Text(Point(400, label9.getAnchor().getY()+25), "Prob. Following Rules (U) Entry Box")
    title10.setSize(16)
    title10.draw(win)

    label10 = Text(Point(400, title10.getAnchor().getY()+30), "The entry box is the percentage or likelihood that the algorithm will follow the rules that we have set up for it.\nAt default U = 100% meaning that there are no chance of error.")
    label10.draw(win)
    
    title11 = Text(Point(400, label10.getAnchor().getY()+30), "Game Composition Entry Box")
    title11.setSize(16)
    title11.draw(win)

    label11 = Text(Point(400, title11.getAnchor().getY()+30), "It represents the number of altruists in percentage within the game.\nInsert a number between 0 and 100, where 0 is all egoists and 100 is all altruists.")
    label11.draw(win)
    
    return marble2_image, instruction_title, text1, text2, text3, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7, title8, label8, title9, label9, title10, label10, title11, label11 


def Instruction_Undraw(win, N_Entry, C_Entry, U_Entry, Composition_Entry, Round_Entry, marble2_image, instruction_title, text1, text2, text3, title1, label1, title2, label2, title3, label3, title4, label4, title5, label5, title6, label6, title7, label7, title8, label8, title9, label9, title10, label10, title11, label11):
    
    instruction_title.undraw()
    text1.undraw()
    text2.undraw()
    text3.undraw()
    title1.undraw()
    label1.undraw()
    title2.undraw()
    label2.undraw()
    title3.undraw()
    label3.undraw()
    title4.undraw()
    label4.undraw()
    title5.undraw()
    label5.undraw()
    title6.undraw()
    label6.undraw()
    title7.undraw()
    label7.undraw()
    title8.undraw()
    label8.undraw()
    title9.undraw()
    label9.undraw()
    title10.undraw()
    label10.undraw()
    title11.undraw()
    label11.undraw()
    marble2_image.undraw()

    N_Entry.draw(win)
    C_Entry.draw(win)
    U_Entry.draw(win)
    Composition_Entry.draw(win)
    Round_Entry.draw(win)


## Draw All Components of Game 1 ##
def Game1_Draw(win):

    marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2 = GameParameters_Draw(win)
    rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button = Functions_Draw(win)
    lake_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button = LakeHouse_Draw(win)

    return lake_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button, marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2, rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button


## Undraw All Components of Game 1 ## 
def Game1_Undraw(lake_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button, marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2, HouseArray, rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button):

        LakeHouse_Undraw(lake_image, NumAltruists_text, NumEgoists_text, RoundNumber_text, warning_text1, Equilibrium_text, Absorbing_text, Instruction_Button, Previous_Button, Next_Button, Round_Entry, Reset_Button, Menu_Button, Exit_Button)
        GameParameters_Undraw(marble_image, rect1, steel_image, GameParameters_text, N_Entry, N_text, C_Entry, C_text, U_Entry, U_text, Composition_Entry, Composition_text, warning_text2)
        House_Undraw(HouseArray)
        Functions_Undraw(rect2, steel_image2, GameFunctions_text, Equilibrium_Button, AbsorbingSet_Button)
